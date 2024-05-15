
from bs4 import BeautifulSoup
import re 



class MyBeautifulSoup:

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        

    def parse_columns(self):

        columns = []
        tr = self.soup.find('tr')
        for i in tr.find_all('a'):
            column_name = re.sub(r'\s+', ' ', i.text.strip().replace('\n', ''))
            columns.append(column_name)

      
        return columns
    

    def filter_rows(self, tag):
        return tag.name == 'tr' and tag.find('th') is None

    def parse_data(self):
        data = []
        for row in self.soup.find_all(self.filter_rows):
            row_data = []
            for element in row.find_all('td'):
                if element.text.strip() != '':
                    row_data.append(element.text.strip())
            data.append(row_data)
        data.pop() # Remove the last empty row
        return data

    


