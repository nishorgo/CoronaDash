import os
import pandas as pd
import joblib
import numpy as np

def SelectColumns(column_names, filename='selected_columns'):
    # Load the dataset into a pandas dataframe
    df = pd.read_csv('dataset/owid-covid-data.csv')
    
    # Select the columns specified in the input list
    selected_columns = df[column_names]
    
    # Create a new dataframe with the selected columns plus 'iso_code', 'date', and 'location'
    new_df = pd.concat([df[['iso_code', 'date', 'location']], selected_columns], axis=1)

    mask = (new_df['location'] == 'World') | (new_df['location'] == 'Europe') | (new_df['location'] == 'Asia') | (new_df['location'] == 'Africa') | (new_df['location'] == 'South America') | (new_df['location'] == 'North America') | (new_df['location'] == 'Oceania')
    new_df = new_df[~mask]
    
    # Remove rows where any of the selected columns is NaN
    new_df = new_df.dropna(subset=column_names)
    
    # Add the .csv extension if no extension was specified in the filename
    filename, extension = os.path.splitext(filename)
    if not extension:
        filename += '.csv'
    
    # Save the new dataframe as a CSV file with the specified filename inside the 'dataset' folder
    filepath = os.path.join('dataset', filename)
    new_df.to_csv(filepath, index=False)


def SeparateDataframes():
    SelectColumns(['new_cases', 'new_cases_smoothed'], 'daily_case')
    SelectColumns(['new_cases_per_million', 'new_cases_smoothed_per_million'], 'daily_per_million')
    SelectColumns(['total_cases'], 'total_cases')
    SelectColumns(['total_cases_per_million'], 'total_per_million')
    print('Done with cases')

    SelectColumns(['new_deaths', 'new_deaths_smoothed'], 'daily_deaths')
    SelectColumns(['new_deaths_per_million', 'new_deaths_smoothed_per_million'], 'daily_deaths_per_million')
    SelectColumns(['total_deaths'], 'total_deaths')
    SelectColumns(['total_deaths_per_million'], 'total_deaths_per_million')
    print('Done with deaths')

    SelectColumns(['new_vaccinations', 'new_vaccinations_smoothed'], 'daily_vaccinations')
    SelectColumns(['new_vaccinations_smoothed_per_million'], 'daily_vaccinations_per_million')
    SelectColumns(['total_vaccinations'], 'total_vaccinations')
    SelectColumns(['total_vaccinations_per_hundred'], 'total_vaccinations_per_hundred')
    SelectColumns(['total_boosters'], 'total_boosters')
    SelectColumns(['total_boosters_per_hundred'], 'total_boosters_per_hundred')
    print('Done with vaccinations')
    
    SelectColumns(['new_people_vaccinated_smoothed'], 'daily_people_vaccinated')
    SelectColumns(['new_people_vaccinated_smoothed_per_hundred'], 'daily_vaccinated_per_hundred')
    SelectColumns(['people_fully_vaccinated'], 'people_fully_vaccinated')
    SelectColumns(['people_fully_vaccinated_per_hundred'], 'people_fully_vaccinated_per_hundred')
    SelectColumns(['people_vaccinated'], 'people_vaccinated')
    SelectColumns(['people_vaccinated_per_hundred'], 'people_vaccinated_per_hundred')
    print('Done with people vaccinated')

    SelectColumns(['hosp_patients'], 'hosp_patients')
    SelectColumns(['hosp_patients_per_million'], 'hosp_patients_per_million')
    SelectColumns(['icu_patients'], 'icu_patients')
    SelectColumns(['icu_patients_per_million'], 'icu_patients_per_million')
    SelectColumns(['weekly_hosp_admissions'], 'weekly_hosp_admissions')
    SelectColumns(['weekly_icu_admissions'], 'weekly_icu_admissions')
    print('Done with hospitalizations')

    SelectColumns(['new_tests', 'new_tests_smoothed'], 'daily_tests')
    SelectColumns(['new_tests_per_thousand', 'new_tests_smoothed_per_thousand'], 'daily_tests_per_thousand')
    SelectColumns(['total_tests'], 'total_tests')
    SelectColumns(['total_tests_per_thousand'], 'total_tests_per_thousand')
    SelectColumns(['positive_rate'], 'positive_rate')
    SelectColumns(['tests_per_case'], 'tests_per_case')
    print('Done with tests')

    df = pd.read_csv('dataset/owid-covid-data.csv')

    vaccination_table = df[['location', 'new_vaccinations', 'new_vaccinations_smoothed_per_million', 'total_vaccinations', 'total_vaccinations_per_hundred', 'total_boosters', 'total_boosters_per_hundred', 'date']]
    vaccination_table = vaccination_table.dropna(subset=['new_vaccinations', 'new_vaccinations_smoothed_per_million', 'total_vaccinations', 'total_vaccinations_per_hundred', 'total_boosters', 'total_boosters_per_hundred'])
    vaccination_table.to_csv('dataset/vaccination_table.csv', index=False)

    vaccinated_people_table = df[['location', 'people_vaccinated', 'people_fully_vaccinated', 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred', 'date']]
    vaccinated_people_table = vaccinated_people_table.dropna(subset=['people_vaccinated', 'people_fully_vaccinated', 'people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred', 'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred'])
    vaccinated_people_table.to_csv('dataset/vaccinated_people_table.csv', index=False)

    tests_table = df[['location', 'new_tests', 'new_tests_per_thousand', 'total_tests', 'total_tests_per_thousand', 'positive_rate', 'tests_per_case', 'date']]
    tests_table = tests_table.dropna(subset=['new_tests', 'new_tests_per_thousand', 'total_tests', 'total_tests_per_thousand', 'positive_rate', 'tests_per_case'])
    tests_table.to_csv('dataset/tests_table.csv', index=False)

    hospitalization_table = df[['location', 'icu_patients', 'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_hosp_admissions', 'date']]
    hospitalization_table = hospitalization_table.dropna(subset=['icu_patients', 'icu_patients_per_million', 'hosp_patients', 'hosp_patients_per_million', 'weekly_icu_admissions', 'weekly_hosp_admissions'])
    hospitalization_table.to_csv('dataset/hospitalization_table.csv', index=False)

    deaths_table = df[['location', 'new_deaths', 'new_deaths_per_million', 'total_deaths', 'total_deaths_per_million', 'date']]
    deaths_table = deaths_table.dropna(subset=['new_deaths', 'new_deaths_per_million', 'total_deaths', 'total_deaths_per_million'])
    deaths_table.to_csv('dataset/deaths_table.csv', index=False)

    cases_table = df[['location', 'new_cases', 'new_cases_per_million', 'total_cases', 'total_cases_per_million', 'continent', 'date']]
    cases_table = cases_table.dropna(subset=['new_cases', 'new_cases_per_million', 'total_cases', 'total_cases_per_million'])
    cases_table.to_csv('dataset/cases_table.csv', index=False)

    print('Done with all tables')




def FindHomePageData():
    df = pd.read_csv('dataset/owid-covid-data.csv')
    country = 'World'

    most_recent_date = df.loc[df['location'] == country, 'date'].max()

    row = df.loc[(df['location'] == country) & (df['date'] == most_recent_date)]

    cases = row.loc[:, 'total_cases'].values[0]
    deaths = row.loc[:, 'total_deaths'].values[0]
    vaccinations = row.loc[:, 'people_vaccinated'].values[0]

    if np.isnan(cases):  
        non_nan_cases = df.loc[~np.isnan(df['total_cases']) & (df['location'] == country)]
        most_recent_non_nan_cases = non_nan_cases.loc[non_nan_cases['date'] == non_nan_cases['date'].max()]
        cases = most_recent_non_nan_cases['total_cases'].values[0]

    if np.isnan(deaths):  
        non_nan_deaths = df.loc[~np.isnan(df['total_deaths']) & (df['location'] == country)]
        most_recent_non_nan_deaths = non_nan_deaths.loc[non_nan_deaths['date'] == non_nan_deaths['date'].max()]
        deaths = most_recent_non_nan_deaths['total_deaths'].values[0]
        
    if np.isnan(vaccinations):  
        non_nan_vaccinations = df.loc[~np.isnan(df['people_vaccinated']) & (df['location'] == country)]
        most_recent_non_nan_vaccinations = non_nan_vaccinations.loc[non_nan_vaccinations['date'] == non_nan_vaccinations['date'].max()]
        vaccinations = most_recent_non_nan_vaccinations['people_vaccinated'].values[0]

    joblib.dump((cases, deaths, vaccinations), 'dataset/total_numbers.joblib')