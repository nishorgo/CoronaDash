from dash import dash_table, dcc, html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date

app = DjangoDash('Tests', external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('owid-covid-data.csv')
df = df[['location', 'new_tests', 'new_tests_per_thousand', 'total_tests', 'total_tests_per_thousand', 
         'positive_rate', 'tests_per_case', 'date']].copy()


PAGE_SIZE = 5


app.layout = html.Div(children=
    [
        html.Div(className='d-flex justify-content-center', children=
            [   
                dbc.Card(
                    [
                        dbc.CardBody(
                            dcc.DatePickerSingle(
                                id='date-picker',
                                min_date_allowed=date(2020, 1, 1),
                                max_date_allowed=date(2023, 3, 1),
                                initial_visible_month=date(2021, 1, 1),
                                month_format='MMM D, YYYY',
                                display_format='MMM D, YYYY',
                                date=date(2021, 1, 1),
                            ),
                        ),

                        dbc.CardBody(
                            [
                                html.Div(
                                    dash_table.DataTable(
                                        id='table-paging-with-graph',
                                        columns=[
                                            {"name": i, "id": i} for i in sorted(df.columns) if i != 'date'
                                        ],
                                        page_current=0,
                                        page_size=20,
                                        page_action='custom',

                                        filter_action='custom',
                                        filter_query='',

                                        sort_action='custom',
                                        sort_mode='multi',
                                        sort_by=[],
                                    ),
                                    className='five columns'
                                ),
                            ]
                        ),

                        dbc.CardBody(
                            [
                                html.Div(
                                    id='table-paging-with-graph-container',
                                    className="five columns"
                                )
                            ]
                        )

                    ], color="dark", outline=True
                    
                ),
            ],
        )
    ]
)

    

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-paging-with-graph', "data"),
    Input('date-picker', 'date'),
    Input('table-paging-with-graph', "page_current"),
    Input('table-paging-with-graph', "page_size"),
    Input('table-paging-with-graph', "sort_by"),
    Input('table-paging-with-graph', "filter_query"))
def update_table(selected_date, page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')

    dff = df[df['date'] == selected_date]

    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    return dff.iloc[
        page_current*page_size: (page_current + 1)*page_size
    ].to_dict('records')


@app.callback(
    Output('table-paging-with-graph-container', "children"),
    Input('table-paging-with-graph', "data"))
def update_graph(rows):
    dff = pd.DataFrame(rows)
    return html.Div(
        [
            dcc.Graph(
                id=column,
                figure={
                    "data": [
                        {
                            "x": dff["location"],
                            "y": dff[column] if column in dff else [],
                            "type": "bar",
                            "marker": {"color": "#fff023"},
                        }
                    ],
                    "layout": {
                        "title": " ".join(word.capitalize() for word in column.split("_")),
                        "xaxis": {"automargin": True},
                        "yaxis": {"automargin": True},
                        "height": 250,
                        "margin": {"t": 50, "l": 10, "r": 10},
                    },
                },
            )
            for column in ['new_tests', 'new_tests_per_thousand', 'total_tests', 'total_tests_per_thousand', 
                            'positive_rate', 'tests_per_case']
        ]
    )

