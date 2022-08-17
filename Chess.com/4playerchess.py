import time
from selenium import webdriver
from sensitiveInfo import *
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2Fregister')

username_input = driver.find_element_by_id('username')
username_input.send_keys(USERNAME)

psd_input = driver.find_element_by_id('password')
psd_input.send_keys(PASSWORD)

login_btn = driver.find_element_by_id('login')
login_btn.click()
driver.implicitly_wait(10)

play_btn = driver.find_element_by_xpath('//*[@id="sb"]/div[2]/a[3]/span')
play_btn.click()
driver.implicitly_wait(10)

chessvrnt_btn = driver.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[2]/div/a[5]/div[2]/h2')
chessvrnt_btn.click()
driver.implicitly_wait(10)

chess4player = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[3]/div[3]/div/div[2]/div[3]/div/div[1]/div/div[1]/div/div[2]/div[2]/span')
chess4player.click()
