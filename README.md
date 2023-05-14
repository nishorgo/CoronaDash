# CoronaDash

This project provides a COVID-19 dashboard that displays map, chart and table views of confirmed cases, deaths, tests, vaccinations, and a symptom analysis feature using machine learning. The dashboard is built with Plotly Dash, a Python framework for building analytical web applications.

## Prerequisites

- Python 3.7 or higher
- Django 3.2 or higher
- Plotly Dash 2.0 or higher
- Pandas 1.1.5 or higher
- Scikit-learn 0.24.2 or higher

## Installation

1. Clone the repository:

```
git clone https://github.com/<username>/<repository>.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Set up the database:

```
python manage.py migrate
```

4. Run the server:

```
python manage.py runserver
```

## Usage

Open your web browser and go to http://localhost:8000/ to access the COVID-19 dashboard. 

The dashboard allows you to view the COVID-19 data in different ways, including:

- Map view: Shows the distribution of confirmed cases, deaths, tests, and vaccinations on a world map.
- Chart view: Shows the trend of confirmed cases, deaths, tests, and vaccinations over time in line charts.
- Table view: Shows the detailed COVID-19 data in a table format.
- Symptom analysis: Allows users to input their symptoms and receive a prediction of whether they may have COVID-19 using machine learning. They may also download the reports of their tests.
- Update Guidelines: Allows the superuser to set and update symptom based guidelines that shows under the report of each test.
- Update Dashboard Data: Allows the superuser to update the dataset from the source.

## Credits

It uses data from [Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data) and the [scikit-learn](https://scikit-learn.org/stable/) library for symptom analysis.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for details.
