# import libraries
from datetime import datetime
import csv, os, sys
import pandas as pd

# create file.csv
def createCSV():
    # check if file.csv exists already
    if os.path.exists('./tracking.csv'):
        return
    # creates file.csv with columns only
    else:
        columns = pd.DataFrame(columns=['Client Name', 'Start Date', 'Start Time', 'End Date',
                                        'End Time', 'Total Time Elasped (in hrs)', 'Expected Pay (in $)'])
        # save file.csv
        columns.to_csv('./tracking.csv')
        return

# get the date and time from the system and return them as a tuple
def getDate():
    date_time = datetime.now()
    date = date_time.date()
    return date

# combine the date and time
def combineDateTime(date, time):
    date_time = datetime.combine(date, time)
    return date_time

# calculate the time elasped
def calcTime(start, end):
    # verify that the end time is greater than the start time
    if start > end:
        sys.exit("Start time is greater than end time. \nPls check and try again")
    else:
        return end - start

# calculate how much pay Nana (the Consultant) should expect
def calcPay(time):
    pay = time * 5
    return round(pay, 2)

# add parameters to file.csv
def addToCSV(name, startDate, startTime, endDate, endTime, time, pay):
    csv_list = ['',name, startDate, startTime, endDate, endTime, time, pay]
    my_file = open('./tracking.csv', 'a')
    writer = csv.writer(my_file, delimiter=',')
    writer.writerow(csv_list)
    my_file.flush()
    my_file.close()
    return 1

# convert users input time to seconds
def getDateTimeSeconds(inputDate, inputTime):
     date_time = combineDateTime(inputDate, inputTime)
     result = datetime.timestamp(date_time)
     return result

# Take users date and time input and convert it to date time object
def inputDateTime(var):
    date = input(f"Enter the {var} date in the format (YYYY-MM-DD): \n")
    time = input(f"Enter the {var} time in 24hr format (HH:MM): \n")
    date = datetime.strptime(date, '%Y-%m-%d').date()
    time = datetime.strptime(time, '%H:%M').time()
    return date, time

# Take users time and use system date to generate date time object
def inputTime(var):
    date = getDate()
    time = input(f"Enter the {var} time in 24hr format (HH:MM): \n")
    time = datetime.strptime(time, '%H:%M').time()
    return date, time

# Use dates and times for calculations then append to csv file
def endProcess(name, startDate, startTime, endDate, endTime, start, end):
    startDate = startDate.strftime('%Y-%m-%d')
    startTime = startTime.strftime('%H:%M')
    endDate = endDate.strftime('%Y-%m-%d')
    endTime = endTime.strftime('%H:%M')
    time_elasped = calcTime(start, end)/3600
    pay = calcPay(time_elasped)
    addToCSV(name, startDate, startTime, endDate, endTime, round(time_elasped, 2), round(pay, 2))
    print("Entry appended to file")
    return 1

def main():
    createCSV()
    name = input("Enter the name of the client: ")

    print("\nSTART TIME")
    resp = int(input("1. Enter your own start date and time? \n2. Enter your time and use system date?\n"))

    if (resp == 1):
        # let user enter their date and time
        var = "start"
        start_val = inputDateTime(var)
        start = getDateTimeSeconds(start_val[0], start_val[1])

        print("\nEND TIME")
        resp = int(input("1. Enter your own start date and time? \n2. Enter your time and use system date?\n"))

        if (resp == 1):
            # let user enter their date and time
            var = "end"
            end_val = inputDateTime(var)
            end = getDateTimeSeconds(end_val[0], end_val[1])
            endProcess(name, start_val[0], start_val[1], end_val[0], end_val[1], start, end)
        elif (resp == 2):
            # let user end time and use system date
            var = "end"
            end_val = inputTime(var)
            end = getDateTimeSeconds(end_val[0], end_val[1])
            endProcess(name, start_val[0], start_val[1], end_val[0], end_val[1], start, end)
        else:
            print("Invalid input. \nPlease try again")
    elif (resp == 2):
        # let user end time and use system date
        var = "start"
        start_val = inputTime(var)
        start = getDateTimeSeconds(start_val[0], start_val[1])

        print("\nEND TIME")
        resp = int(input("1. Enter your own start date and time? \n2. Enter your time and use system date?\n"))

        if (resp == 1):
            # let user enter their date and time
            var = "end"
            end_val = inputDateTime(var)
            end = getDateTimeSeconds(end_val[0], end_val[1])
            endProcess(name, start_val[0], start_val[1], end_val[0], end_val[1], start, end)
        elif (resp == 2):
            # let user end time and use system date
            var = "end"
            end_val = inputTime(var)
            end = getDateTimeSeconds(end_val[0], end_val[1])
            endProcess(name, start_val[0], start_val[1], end_val[0], end_val[1], start, end)
        else:
            print("Invalid input. \nPlease try again")
    else:
        print("Invalid input. \nPlease try again")

    return 1

if __name__ == '__main__': main()
