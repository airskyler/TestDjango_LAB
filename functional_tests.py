

from selenium import webdriver # using webdriver to use a browser

browser = webdriver.Firefox() # use Firefox as a brower
browser.get('http://localhost:8000')

assert 'Django' in browser.title

