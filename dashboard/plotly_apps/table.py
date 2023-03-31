from dash import dash_table, dcc, html
from datetime import date

from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc

import pandas as pd


df = pd.read_csv('owid-covid-data.csv')
df = df[['location', 'new_cases', 'new_cases_per_million', 'total_cases', 'total_cases_per_million', 'continent', 'date']].copy()

df['id'] = df['location']
df.set_index('id', inplace=True, drop=False)

app = DjangoDash('Cases', external_stylesheets=[dbc.themes.LUX])

selected_date = '2021-01-01'
df = df[df['date'] == selected_date]


app.layout = html.Div(className='w-75 mb-3', children=
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
                        dash_table.DataTable(
                            id='casetable-row-ids',
                            columns=[
                                {'name': i, 'id': i, 'deletable': True} for i in df.columns
                                if i != 'id'
                            ],
                            data=df.to_dict('records'),
                            editable=False,
                            filter_action="native",
                            sort_action="native",
                            sort_mode='multi',
                            row_selectable='multi',
                            selected_rows=[],
                            page_action='native',
                            page_current= 0,
                            page_size= 10,
                            style_as_list_view=True,
                            style_cell={'padding': '5px'},
                            style_header={
                                'backgroundColor': 'black',
                                'color': 'white',
                                'fontWeight': 'bold'
                            },
                        ),

                        
                        html.Div(id='casetable-row-ids-container')
                    ]
                ),

            ]
            
        )
    ]
)


@app.callback(
    #Output('casetable-row-ids', 'data'),
    Output('casetable-row-ids-container', 'children'),
    #Input('date-picker', 'date'),
    Input('casetable-row-ids', 'derived_virtual_row_ids'),
    Input('casetable-row-ids', 'selected_row_ids'),
    Input('casetable-row-ids', 'active_cell'))

def update_graphs(row_ids, selected_row_ids, active_cell):
    # When the table is first rendered, `derived_virtual_data` and
    # `derived_virtual_selected_rows` will be `None`. This is due to an
    # idiosyncrasy in Dash (unsupplied properties are always None and Dash
    # calls the dependent callbacks when the component is first rendered).
    # So, if `rows` is `None`, then the component was just rendered
    # and its value will be the same as the component's dataframe.
    # Instead of setting `None` in here, you could also set
    # `derived_virtual_data=df.to_rows('dict')` when you initialize
    # the component.

    # df = df[df['date'] == selected_date]
    # table = df.to_dict('records')

    selected_id_set = set(selected_row_ids or [])

    if row_ids is None:
        dff = df
        # pandas Series works enough like a list for this to be OK
        row_ids = df['id']
    else:
        dff = df.loc[row_ids]

    active_row_id = active_cell['row_id'] if active_cell else None

    colors = ['#FF69B4' if id == active_row_id
              else '#7FDBFF' if id in selected_id_set
              else '#0074D9'
              for id in row_ids]
    
    column_graphs= [
        dcc.Graph(
            id=column + '--row-ids',
            figure={
                'data': [
                    {
                        'x': dff['location'],
                        'y': dff[column],
                        'type': 'bar',
                        'marker': {'color': colors},
                    }
                ],
                'layout': {
                    'xaxis': {'automargin': True},
                    'yaxis': {
                        'automargin': True,
                        'title': {'text': column}
                    },
                    'height': 250,
                    'margin': {'t': 10, 'l': 10, 'r': 10},
                },
            },
        )
        # check if column exists - user may have deleted it
        # If `column.deletable=False`, then you don't
        # need to do this check.
        for column in ['new_cases', 'new_cases_per_million', 'total_cases', 'total_cases_per_million'] if column in dff
    ]

    return column_graphs
