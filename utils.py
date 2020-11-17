from datetime import datetime
import time
def filter_records(data, type):
    if type == 'daily':
        dict = {}
        # For all records we need to know all the days there are (unique dates per day)
        datetimes = [datetime.get('createdAt') for datetime in data]
        # Covnert all datetimes to just dates
        dates = [get_date(date) for date in datetimes]
        # Exclude duplicates
        unique_dates = list(set(dates))
        # Sort them ascending
        unique_dates.sort()

        # Create property in dictionary for each unique date, initialized with an empty array
        for unique_date in unique_dates:
            dict[unique_date] = []

        # Add each record into the right array in the dict (matching dates)
        for record in data:
            for date in unique_dates:
                if date == get_date(record.get('createdAt')):
                    dict[date].append(record)

        new_list = []

        # Create new list with dicts containing the date and the avg amountOfFollowers
        for key in dict:
            sum_avg = sum(x['amountOfFollowers'] for x in dict[key]) / len(dict[key])
            sum_avg = round(sum_avg)

            new_list.append({
                "amountOfFollowers": sum_avg,
                "createdAt": key
            })
        
        return new_list

        
                    

def get_date(datetime):
    return datetime[:10]

def get_unix_timestamp(date):
    s = get_date(date)
    print(s)
    unix = time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple())
    print(unix)