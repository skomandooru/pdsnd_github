import time
import pandas as pd
import numpy as np

# Dictionary of city data files by name
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    #  get user input for city (chicago, new york city, washington).
    while True:
        # strip the input value so spaces before and after the city name can be considered valid inputs
        city = input("Select a city to explore bikeshare data (choose from chicago, new york city, washington):\n").strip()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Please select a different city\n")
        else:
            break

    #  get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nSelect the name of the month to filter by: all, january, february, march, april, may, june :\n").strip()
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Please select from the provided choices")
        else:
            break

    #  get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nSelect the day of the week to filter by:all, monday, tuesday, wednesday, thursday, friday, saturday, sunday :\n").strip()
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Please select from the provided choices")
        else:
            break

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular hour
    popular_month = df['month'].mode()[0]
    # display the most common month
    print("Most Common Month:",popular_month)

    # extract month from the Start Time column to create an month column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # find the most popular hour
    popular_day_of_week = df['day_of_week'].mode()[0]
    # display the most common day of week
    print("Most Common Day of Week:",popular_day_of_week)

    # extract month from the Start Time column to create an month column
    df['start_hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_start_hour = df['start_hour'].mode()[0]
    # display the most common start hour
    print("Most Common Hour:",popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display the most commonly used start station
    print("Most Common Start Station:",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most Common End Station:",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'].str.cat(df['End Station'], sep=" ")
    print("Most Common Start and End Station Trip:",df['start_end_combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Trip Duration:",df['Trip Duration'].sum())

    # display mean travel time
    print("Mean Trip Duration:",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types: \n", df['User Type'].value_counts())

    # Washington city does not have data for Gender; check for column
    if 'Gender' in df.columns:
        # Display counts of gender
        print("\nCounts of gender: \n", df['Gender'].value_counts())

    # Washington city does not have data for Birth Year; check for column
    print_birth_year_stats(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_birth_year_stats(df)
    #print birth year statistis if the data frame has the 'Birth Year' column in its data
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print("\nEarliest year of birth: ", int(df['Birth Year'].min()))
        print("Recent year of birth: ", int(df['Birth Year'].max()))
        print("Most common year of birth: ", int(df['Birth Year'].mode()[0]))

def print_raw_data(df)
    # Print the raw data to console.
    #get the dataframe row count
    row_count = len(df.index)
    counter = 0
    msg = ""
    # prompt user for data view
    while counter < row_count:
        view_raw_data = input("\nWould you like to see " + msg + " raw data? Enter yes or no.\n")
        if view_raw_data.lower() != 'yes':
            break
        counter += 5
        msg = "more"
        print(df.head(counter))

def main():
    """Main function called when this module is executed from python."""
    while True:
        #collect city, month, and day
        city, month, day = get_filters()

        #load city data
        df = load_data(city, month, day)

        #display time statistics
        time_stats(df)

        #display station statistics
        station_stats(df)

        #display trip duration statistics
        trip_duration_stats(df)

        #display user statistics
        user_stats(df)

        #print raw data if the user chooses to see it
        print_raw_data(df)

        # prompt user if he/she wants to start analyzing other city data
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
