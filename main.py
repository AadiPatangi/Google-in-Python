import os
os.system("pip install selenium==3.141.0")
from webbot import Browser
import time

driver = Browser()

driver.go_to('https://google.com')

input("Service is running")
