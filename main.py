from scraper.bot import Stocks
from scraper.utilfunc import isweekend
import os

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


BASE_URL = os.environ.get('BASE_URL')
LOGIN = os.environ.get('Login')
PASSWORD = os.environ.get('PASSWORD')
FILE_PATH = os.environ.get('FILE_PATH')


try:
    
    if not isweekend(datetime.today()):

        # # File to store last run date
        last_run_file = 'last_run_date.txt'

        # # Check if last run date file exists
        if os.path.exists(last_run_file):
           with open(last_run_file, 'r') as file:
                 last_run_date = datetime.strptime(file.read(), '%Y-%m-%d')
        else:
        #  If file doesn't exist, assume the script has never been run before
             last_run_date = datetime.min


        # # Get current date
        current_date = datetime.now().date()

        # # Check if the current date is the same as the last run date
        if current_date == last_run_date.date():
        #     If the script has already been run today, raise an error
             raise Exception("Script already ran today!")
        else:
        #  Update last run date to today's date
            with open(last_run_file, 'w') as file:
                 file.write(current_date.strftime('%Y-%m-%d'))

            bot=Stocks(BASE_URL,LOGIN,PASSWORD) 
            bot.apply_parsing()
            bot.file()
            bot.daily_file(FILE_PATH)
    
    else:
        print('Stock Exchange is closed Today')

    
except Exception as e:
    print(e)







