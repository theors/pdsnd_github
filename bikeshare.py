import time
import pandas as pd

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

    """
    get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """

    while True:
        try:
            city = input('\nWhich city would you like to know about? Type in any one of the following: Chicago, New York City, Washington:\n').lower()
            cities = ('chicago', 'new york city', 'washington')
            if city.lower() not in cities:
                print('That\'s not a valid city. Try again!')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print('\nNo input taken.')
            continue

    """
    get user input for month (all, january, february, ... , june)
    """

    while True:
        try:
            month = input('\nWhich month would you like to know about (all, January, February, ... , June)?:\n').lower()
            months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
            if month.lower() not in months:
                print('This is not a valid month. Try again!')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print('\nNo input taken.')
            continue


    """
    get user input for day of week
    """

    while True:
        try:
            day = input('and for which day (all, monday, tuesday, ... sunday)? : ').lower()
            days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
            if day.lower() not in days:
                print('This is not a valid day. Try again!')
            else:
                break
        except (ValueError, KeyboardInterrupt):
            print('\nNo input taken.')
            continue

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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # extract hour from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour

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

    # display the most common month
    popular_month = df['month'].mode()[0]
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    for i in months:
        if popular_month == i:
            print('\nThe most popular month is:\n', months[i])


    # display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('\nThe most popular day of the week is:\n', popular_dayofweek)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station is:\n',popular_start_station)


    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is:\n',popular_end_station)


    # display most frequent combination of start station and end station trip
    df['Start to End Stations'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combo_startend = df['Start to End Stations'].mode()[0]
    print('\nThe most popular trip is from:\n',popular_combo_startend)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is:\n','{:,}'.format(total_travel_time), 'minutes')


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time is:\n','{:,}'.format(mean_travel_time), 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe total number corresponding to each user types is:\n', user_types)

    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    print('\nThe total number corresponding to each gender is:\n', gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_yearofbirth = df['Birth Year'].min()
    print('\nThe earliest year of birth recorded is:\n', earliest_yearofbirth)

    most_recent_yearofbirth = df['Birth Year'].max()
    print('\nThe most recent year of birth recorded is:\n', most_recent_yearofbirth)

    most_common_yearofbirth = df['Birth Year'].mode()[0]
    print('\nThe most frequent year of birth recorded is:\n', most_common_yearofbirth)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def was_user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe total number corresponding to each user types is:\n', user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def hour_stats(df):
    """Displays statistics on the most frequent hour of travel when a specific month and day have been selected."""

    print('\nCalculating The Most Popular hour of Travel...\n')
    start_time = time.time()

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def day_hour_stats(df):
    """Displays statistics on the most frequent day and hour of travel when a specific month (different to 'all') has been selected."""

    print('\nCalculating The Most Popular Day and Hour of Travel...\n')
    start_time = time.time()

    # display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print('\nThe most popular day of the week is:\n', popular_dayofweek)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def month_hour_stats(df):
    """Displays statistics on the most frequent month and hour of travel when a specific day (different to 'all') has been selected."""

    print('\nCalculating The Most Popular Month and Hour of Travel...\n')
    start_time = time.time()

 # display the most common month
    popular_month = df['month'].mode()[0]
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    for i in range(len(months)):
        if popular_month == i:
            print('\nThe most popular month is:\n', months[i])

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is:\n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        """Based on the user's selection of month and day, in the below IF statements we pick which time-related statistics
        are not repeating our selections of month/day unnecessarily."""

        if month != 'all' and day != 'all':
            print('For your selection of month:', month.title(),' & day:', day.title())
            hour_stats(df)
        elif month != 'all' and day == 'all':
            print('For your selection of month:', month.title())
            day_hour_stats(df)
        elif month == 'all' and day != 'all':
            print('For your selection of day:', day.title())
            month_hour_stats(df)
        else:
            time_stats(df)
        """ Due to the fact the Washington.csv file is missing data on gender and birth year, I define a new function was_user_stats() which
        estimates user statistics if the city selected is that of Washington."""
        if city == 'washington':
            station_stats(df)
            trip_duration_stats(df)
            was_user_stats(df)
        else:
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)


        """Prompting the user to choose whether or not they want to see individual trip data
        and providing a sample of 5 rows of raw input each time while validating that the user input is yes or no."""
        while True:
            try:
                individual_trip_data = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\': \n').lower()
                if individual_trip_data == 'yes':
                    pd.set_option('display.max_columns', None)
                    pd.set_option('max_colwidth', None)
                    print(df.sample(n=5))
                elif individual_trip_data == 'no':
                    break
                else:
                    print('This is not a valid answer. Please answer with either \'yes\' or \'no\'')
            except (ValueError, KeyboardInterrupt):
                print('\nNo input taken.')
                continue


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
