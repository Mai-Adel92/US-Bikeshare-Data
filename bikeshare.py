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
    while True :
        try :
            city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
            break
        except : 
            print("That's not one of the choises above!")
       
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        try :
            month = input("Which month you want? January, February, March, April, May, June, or all of them? Type 'All' if you want all of them.\n").lower()
            break
        except :
            print("write the month as a word not as a number")
        
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        try :
            day = input("Which day of week you want? Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or all of them? Type 'All' if you want all of them.\n").lower()
            break
        except :
            print("That's not a day!")
      
                                              
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        df =  df[df['month'] == month]

    if day != 'all':       
        df = df[df['day_of_week'] == day.title()] 
        
    return df


def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df = pd.read_csv(CITY_DATA[city])
      
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    
    popular_month = df['month'].mode()[0]

    import calendar

    popular_month = calendar.month_name[popular_month]
    
    print('The most frequent start month is :', popular_month)


    # TO DO: display the most common day of week
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    popular_day = df['day_of_week'].mode()[0]
    
    print('The most frequent day of week is :', popular_day)
    
    
    # TO DO: display the most common start hour
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    
    popular_hour = df['hour'].mode()[0]
    
    print('The most frequent start hour is :', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df = pd.read_csv(CITY_DATA[city])
    
    popular_start_station = df['Start Station'].mode()[0]
    
    print('The most frequent start station is :', popular_start_station)
    

    # TO DO: display most commonly used end station
    df = pd.read_csv(CITY_DATA[city])
    
    popular_end_station = df['End Station'].mode()[0]
    
    print('The most frequent end station is :', popular_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start End Station'] = df['Start Station'] + df['End Station']
    
    most_frequent_combination = df['Start End Station'].mode()[0] 

    print('The most frequent combination of start station and end station is :\n', most_frequent_combination)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df = pd.read_csv(CITY_DATA[city])
    
    total_travel_time = df['Trip Duration'].sum() 
  
    print('The total travel time is :', total_travel_time)


    # TO DO: display mean travel time
    df = pd.read_csv(CITY_DATA[city])
    
    average_travel_time = df['Trip Duration'].sum() 
  
    print('The average travel time is :', average_travel_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df = pd.read_csv(CITY_DATA[city])
    
    user_count = df['User Type'].value_counts()
    
    print('Counts of each user type are :\n', user_count)


    # TO DO: Display counts of gender
    df = pd.read_csv(CITY_DATA[city])
    if 'Gender' in df.columns :
        gender_count = df['Gender'].value_counts()

        print('Counts of each gender type are :\n', gender_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    df = pd.read_csv(CITY_DATA[city])
    if 'Birth Year' in df.columns :
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]

        print('The earliest year of birth is : {} \n The most recent year of birth is : {} \n The most common year of birth is :{}'.format(earliest_birth_year, recent_birth_year, common_birth_year))
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    display_data = input("Do ychou want to see the first 5 rows of data ?\n Enter yes or no\n").lower()
    start_loc = 0        
    while display_data != 'no' :
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        display_data = input("Do you want to see the next 5 rows of data ?\n Enter yes or no\n").lower()
         
           

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city)
        station_stats(df, city)
        trip_duration_stats(df, city)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()