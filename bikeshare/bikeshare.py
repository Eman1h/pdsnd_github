# -*- coding: utf-8 -*-
"""bikeshare.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tBSF-q0ddQ_WPrVewvyGQe8FaNZKCCGh

# **Bikeshare Project**

Importent resourses help me:

*   Pandas documents [https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html]
*   Stack Overflow and chatGPT [to search about error & the correction in code and explain]

### import the dependency
"""

import time
import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

print("First Project")
print("Welcome")
CITY_DATA = { 'chicago': '/content/drive/MyDrive/Courses/Programming for DS/all-project-files/chicago.csv',
              'new york city': '/content/drive/MyDrive/Courses/Programming for DS/all-project-files/new_york_city.csv',
              'washington': '/content/drive/MyDrive/Courses/Programming for DS/all-project-files/washington.csv' }

def get_filters():

    print('Hello! Let\'s explore US BIKESHARE data!')
    print("\nWelcome to this program. Please choose your city:")

    while True:
        try:
            city = input("input for city (chicago, new york city, washington)").lower()

            if city not in CITY_DATA.keys():
                print("Error: city not in list. Please try again.")
                continue

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
#######

    month_data = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in month_data.keys():
        month = input("Please enter the month, from January to June:").lower()

        if month not in month_data.keys():
            print("Error: month not in list. Please try again")

#######

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    day = ''
    while day not in days:
        print("Please enter the day :")
        day = input('Input the day: ').lower()

        if day not in days:
            print("Error: day not in list. Please try again")



    print(f"\nYou have chosen to view data for city: {city.upper()}, month: {month.upper()} and day: {day.upper()}.")
    print('-'*40)
    return city, month, day

"""### 1- Popular times of travel"""

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df.head()


    #Create a new column and Convert it to datetime
    df['Date'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Date'].dt.month
    df['day_of_week'] = df['Date'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]


    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()
    print(f"Most Popular Month : {most_common_month}")

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()
    print(f"\nMost Popular Day: {most_common_day}")



    # display the most common start hour
    df['hour'] = df['Date'].dt.hour
    most_common_hour = df['hour'].mode()
    print(f"\nMost Popular Day: {most_common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""### 2- Popular stations and trip"""

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used (start station)
    most_common_start = df['Start Station'].mode()
    print(f"The most commonly used start station: {most_common_start}")


    # display most commonly used (end station)
    most_common_end = df['End Station'].mode()
    print(f"\nThe most commonly used end station: {most_common_end}")

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    frequent_combination = df['Start To End'].mode()[0]

    print(f"\nThe most frequent combination of trips are from {frequent_combination}.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""### 3- Trip duration"""

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()

    #duration in min and sec
    minute, second = divmod(total_duration, 60)

    #duration in hour and min
    hour, minute = divmod(minute, 60)

    #avg trip duration
    average_duration = round(df['Trip Duration'].mean())

    #avg in min and sec
    mins, sec = divmod(average_duration, 60)

    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration {mins} minutes and {sec} seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""### 4- User info"""

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()

    print(f"The types of users:\n\n{user_type}")

    #gender

    gender = df['Gender'].value_counts()
    print(f"\nThe types of users by gender:\n\n{gender}")


    earliest = int(df['Birth Year'].min())
    recent = int(df['Birth Year'].max())
    common_year = int(df['Birth Year'].mode()[0])
    print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    while True:
        raw_data = input("If you wish to view the raw data, enter 'yes'; otherwise, enter 'no': ").lower()
        start_loc = 0
        if raw_data == "yes":
            print(df.head())
            break
        elif raw_data == "no":
            break
        else:
            print("\nPlease check your input.")

    while raw_data == 'yes':
      print("nWould you like to view 5 rows of individual trip data? Enter yes or no: ")
      start_loc += 5
      raw_data = input().lower()
      #If user opts for it, this displays next 5 rows of data
      if raw_data == "yes":
            print(df[start_loc:start_loc+5])
      elif raw_data != "yes":
            break

    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()