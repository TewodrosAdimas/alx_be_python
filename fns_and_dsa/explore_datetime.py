from datetime import datetime, timedelta, date
def display_current_datetime():
    current_dat = datetime.now()
    current_date = current_dat.strftime("%Y-%m-%d %H:%M:%S")
    print ("Current date and time: ", current_date) #"YYYY-MM-DD HH:MM:SS."

def calculate_future_date():
    add = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=add)
    print(delta)
    current_date = date.today()
    future_dat = current_date + delta
    future_date = future_dat.strftime("%Y-%m-%d ")
    print("Future date:", future_date)  #YYYY-MM-DD

display_current_datetime()
calculate_future_date()