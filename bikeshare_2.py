import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        set_of_cities= ['chicago','new york city','washington']
        city = input("\n Please choose one of these cities: Chicago, New York City, Washington \n").lower()
        if city in set_of_cities:
            break
        else:
            #print("\n Your input is not valid. Please choose one of the three options: Chicago, New York City or Washington")
            print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        set_of_months= ['january','february','march','april','may','june', 'all']
        month = input("\n Please type the month of the following list: January, February, March, April, May, June or All \n").lower()
        if month in set_of_months:
            break
        else:
            print("\n Your input is not valid. Please type a month from January to June (or 'All')")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekdays= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']
        day = input("\n Please type the day of the week you wish to work on (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All)? \n").lower()
        if day in weekdays:
            break
        else:
            print("\n Your input is not valid. Please type a day of the week (or 'All') ")


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name


    if month != 'All':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':
        #Filter by day of week to create the new dataframe
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.\n"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # Using the mode function to get the value that appears more often
    most_pop_month = df['month'].mode()[0]
    print("\nThe most popular of the 12 months of the year is month number: {}\n".format(most_pop_month))

    # TO DO: display the most common day of week
    most_pop_day = df['weekday'].mode()[0]
    print("\nThe most popular day of the week is: {}\n".format(most_pop_day))

    # TO DO: display the most common start hour

    df['Start_hour'] = df['Start Time'].dt.hour

    most_pop_hour = df['Start_hour'].mode()[0]

    print("\nThe most popular start hour is: {}\n".format(most_pop_hour))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # Again using the mode function to get the value that appears more often
    most_pop_start_station = df['Start Station'].mode()[0]

    print("\nThe most commonn start station is: {}\n".format(most_pop_start_station))

    # TO DO: display most commonly used end station

    most_pop_end_station = df['End Station'].mode()[0]

    print("\nThe most commonn end station is: {}\n".format(most_pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip

    # This requires to first concatenate the start and end station columns into a new column
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep='-')

    # Then the logic is the same as in the two previous questions; find the most popular value of the new column
    start_end = df['Start_End'].mode()[0]

    print("\nThe most popular combination of start and end stations are: {}\n".format(start_end))

    print("\nThis took %s seconds.\n" % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # Calculate the sum of travel durations
    total_travel_duration = df['Trip Duration'].sum()

    # Divide the result by 3600 to present a reasonable number expressed in hours
    print("\nThe total travel time in hours is: {}\n".format(total_travel_duration/3600))


    # TO DO: display mean travel time

    # Calculate the mean of travel durations
    mean_travel_duration = df['Trip Duration'].mean()

    # Divide the result by 60 to present a reasonable number expressed in minutes
    print("\nThe mean travel time in minutes is: {}\n".format(mean_travel_duration/60))


    print("\nThis took %s seconds.\n" % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # Using the value_counts function to return counts of unique values
    count_user_types = df['User Type'].value_counts()

    print("\nThe count of users by type are: {}\n".format(count_user_types))


    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df['Gender'].value_counts()
        print("\nThe count of users by gender are: {}\n".format(count_gender))
    else:
        print('\nGender stats cannot be calculated because Gender does not appear in the dataframe\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df:
        # Using the min function to find the smallest year number
        earliest_birth_year = df['Birth Year'].min()
        print("\nThe earliest birth year is: {}\n".format(int(earliest_birth_year)))

        # Using the max function to find the biggest year number
        recent_birth_year = df['Birth Year'].max()
        print("\nThe most recent birth year is: {}\n".format(int(recent_birth_year)))

        # As previously using the mode function to get the value that appears more often
        common_birth_year = df['Birth Year'].mode()
        print("\nThe most common birth year is: {}\n".format(int(common_birth_year)))

    else:
          print('\nBirth Year stats cannot be calculated because Birth Year does not appear in the dataframe\n')



    print("\nThis took %s seconds.\n" % (time.time() - start_time))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
        start_loc = 0
        while (start_loc<df.shape[0]-5):
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("\nDo you wish to continue?: Yes or No\n").lower()
            if view_display.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
