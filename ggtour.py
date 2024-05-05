import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import csv
import time

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)  # 기본값 True: 웹 안 뜸
page = browser.new_page()

jobs_db = []

page.goto("http://www.ggac.or.kr/?p=14")
time.sleep(2)
page.click("div.month>ul>li")
time.sleep(2)
page.click("div.photo_list>ul>li")
time.sleep(2)