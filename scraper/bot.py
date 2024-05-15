
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import re 
import datetime
import os
from scraper.parsing import MyBeautifulSoup
from scraper.file import FileCreation





class Stocks():

    def __init__(self,base_url,login,password):

        self.playwright = sync_playwright().start()
        self.BASE_URL = base_url
        self.LOGIN = login
        self.PASSWORD = password

    def scrape_website(self):

        # Launch a browser
        playwright = self.playwright
        # Launch a browser
        browser = playwright.chromium.launch(headless=True, slow_mo=0)
       
        # Create a new page
        page = browser.new_page()

        # Visit the playwright website
        page.goto(self.BASE_URL)

        # Click on the 'Login' link
        page.get_by_role('link', name='Login').click()

        # Fill in the username and password fields
        page.fill('input#id_username', self.LOGIN)
        page.fill('input#id_password', self.PASSWORD)

        # Click the submit button
        page.click('button[type=submit]')

        # Click on the 'Watchlist View' link
        page.get_by_role('link', name='Watchlist View').click()

        # Wait for the table to be visible
        page.wait_for_selector('table.data-table.text-nowrap.striped.mark-visited')

        # Get the inner HTML of the desired element
        html = page.inner_html('.responsive-holder.fill-card-width')

        # Close the browser
        browser.close()

        # Parse the HTML using BeautifulSoup
        # soup = BeautifulSoup(html, 'html.parser')
        # Perform further processing with BeautifulSoup if needed
        return html
    
    def apply_parsing(self):

        parsing = MyBeautifulSoup(self.scrape_website())
        self.column = parsing.parse_columns()
        self.data = parsing.parse_data()
       

    def file(self):

        file = FileCreation()
        file.stock_file_creation(self.data,self.column)
        file.save_to_csv(file.df,file.name)

    def daily_file(self,file_path):

        file = FileCreation()
        dataframe = file.daily_file_creation(file_path=file_path)
        print('first time data saved') if dataframe.size == 0 else file.save_to_csv(dataframe,file.file_name)
            
      
            
            

    


   







