from datetime import datetime , timedelta
# Create a funcion called display_current_datetime.
def display_current_datetime():
# inside the function add a variable namely current_datetime to store current date and time
    current_date = datetime.now()
# print current date and time in a format of yyy-mm-d, h:m:s.
    print("Current datetime: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
# create another function namely calculate_future_date
def calculate_future_date():
# prompt the user to enter the number of days but they should be in an int form
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    #call current_date variable
    current_date = datetime.now()
    # use current_date to calculate future date
    future_date = current_date + timedelta(days=number_of_days)
    # print future date in form of Y-m-d
    print("Future date: ",future_date.strftime("%Y-%m-%d"))
if __name__== "_main_":
     display_current_datetime()
     calculate_future_date()

    


