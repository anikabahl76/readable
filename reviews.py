import requests
import pandas as pd
from creds import CLIENT_ID, CLIENT_SECRET

BASE_URL = 'https://api.nytimes.com/svc/books/v3'
START_YEAR = 2020
START_MONTH = 12
START_DAY = 28
PREDICTIVE_CHARACTERISTICS = ["rank_last_week", "weeks_on_list", "publisher", "author"]
PREDICTION_CHARACTERISTIC = "rank"
ALL_CHARACTERISTICS = PREDICTIVE_CHARACTERISTICS + [PREDICTION_CHARACTERISTIC]



def get_reviewed_books(list_name):
    error_count = 0
    all_reviewed_books = []
    for i in range(20):
        if error_count > 20:
            break
        year_string = str(START_YEAR - i)
        for j in range(12):
            if error_count > 50:
                break
            month_string = str(START_MONTH - j)
            if len(month_string) < 2:
                month_string = "0" + month_string
            for k in range(28):
                if error_count > 20:
                    break
                day_string = str(START_DAY - k)
                if len(day_string) < 2:
                        day_string = "0" + day_string
                date_string = year_string + "-" + month_string + "-" + day_string
                try:
                    r = requests.get(BASE_URL + '/lists/' + date_string + '/' + list_name + '.json?api-key=' + CLIENT_ID)
                    for book in r.json()["results"]["books"]:
                        characteristics = []
                        for characteristic in ALL_CHARACTERISTICS:
                            characteristics.append(book[characteristic])
                        all_reviewed_books.append(characteristics)
                except:
                    error_count +=1
    all_reviewed_books_df = pd.DataFrame(all_reviewed_books, columns=ALL_CHARACTERISTICS)
    return all_reviewed_books_df