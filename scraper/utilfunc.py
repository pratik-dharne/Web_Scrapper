import pandas as pd
from datetime import datetime, timedelta

def dates(x):
    if len(x) != 0:
        if pd.to_datetime(x).dt.weekday.iloc[0] == 0:

            three_days_ago = pd.to_datetime(x).iloc[0] - timedelta(days=3)

            output_start_date = three_days_ago.strftime("%d/%m/%Y")
            output_end_date = datetime.now().strftime("%d/%m/%Y")

            return f'{output_start_date}, "to", {output_end_date}'
            
        else:
            three_days_ago = pd.to_datetime(x).iloc[0] - timedelta(days=1)

            output_start_date = three_days_ago.strftime("%d/%m/%Y")
            output_end_date = datetime.now().strftime("%d/%m/%Y")

            return f'{output_start_date}, "to", {output_end_date}'
    
        


def isweekend(date):

    return date.isoweekday() in [6,7]