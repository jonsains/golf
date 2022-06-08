from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import numpy
import pandas as pd
import time
from datetime import timedelta
from datetime import datetime

tourneyscores = pd.read_csv("Jan262022farmers-insurance-open.csv")
#print(tourneyscores.columns)
newcols = ['index','name']
holes = range(1,73,1)
newcols += holes
#print(newcols)
tourneyscores.columns = newcols

tourneyscores.set_index('name', inplace=True)
tourneyscores.drop('index', axis=1, inplace=True)
print(tourneyscores.head())

