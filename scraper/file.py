import pandas as pd
import datetime
import os 
from scraper.utilfunc import dates



class FileCreation:


    def stock_file_creation(self,data,columns):  

        self.df = pd.DataFrame(data=data, columns=columns)
        #self.df['Date'] = datetime.datetime.today().strftime("%d/%m/%Y")
        self.df['Date'] = datetime.date.today()
        self.df.set_index('S.No.', inplace=True)
        self.name = 'stocks_data.csv'


    def daily_file_creation(self,file_path):
       
        self.df = pd.read_csv(file_path)
     
        self.file_name = 'daily_change.csv'
        # self.df.drop(columns=['S.No.'],inplace=True,axis=1)
      
        self.df.set_index(['Name','Date'],inplace=True)
       
        self.df.sort_index(inplace=True)
        self.df = self.df.groupby(level=0).diff(periods=1)
        self.df.dropna(inplace=True)
       
        self.df.reset_index(inplace=True)
      
        self.df = self.df.groupby(['Name'],as_index=False).last()
       
        self.df['Date'] = dates(self.df['Date'])

        return self.df 
        

    def save_to_csv(self,df,file_name):

        if os.path.isfile(file_name):
            df.to_csv(file_name, index=False, header=False, mode='a')
        else:
            df.to_csv(file_name, index=False, header=True, mode='a')






