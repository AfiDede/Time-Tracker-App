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


