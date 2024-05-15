
import os
import pandas as pd
from datetime import datetime,timedelta
from scraper.utilfunc import dates
from dotenv import load_dotenv
from scraper.file import FileCreation
load_dotenv()


File_path = os.environ.get('FILE_PATH')


class changes():

    def __init__(self) -> None:

        self.df = pd.read_csv(File_path)
        self.file_path = 'daily_change.csv'

    def weekly_change(self):

        self.df.drop(columns=['S.No.'],inplace=True,axis=1)
        self.df.set_index(['Name','Date'],inplace=True)
        self.df.sort_index(inplace=True)
        self.df = self.df.groupby(level=0).diff(periods=1)
        self.df.reset_index(inplace=True)
        self.df = self.df.groupby(['Name']).last()
        self.df['Date'] = dates(self.df['Date'])
        FileCreation()


