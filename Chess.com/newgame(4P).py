import time
from selenium import webdriver
from sensitiveInfo import *
from selenium.webdriver.chrome.options import Options

#login page
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.chess.com/login_and_go?returnUrl=https%3A%2F%2Fwww.chess.com%2Fregister')

username_input = driver.find_element_by_id('username')
username_input.send_keys(USERNAME)

psd_input = driver.find_element_by_id('password')
psd_input.send_keys(PASSWORD)

login_btn = driver.find_element_by_id('login')
login_btn.click()
driver.implicitly_wait(5)

#play online
play_btn = driver.find_element_by_xpath('//*[@id="sb"]/div[2]/a[3]') 
play_btn.click()
driver.implicitly_wait(10)

#variant
chessvrnt_btn = driver.find_element_by_xpath('//*[@id="board-layout-sidebar"]/div/div[2]/div/a[5]/div[2]/h2') 
chessvrnt_btn.click()
driver.implicitly_wait(10)

#4player
chess4player = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div[4]/div/div[2]/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/span')
chess4player.click()
driver.implicitly_wait(10)

#new game
newgame = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[1]/div/a')
newgame.click()
driver.implicitly_wait(10)

#solo mode
solomode = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]')
solomode.click()
driver.implicitly_wait(10)

#invite friends
invite = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[4]/div[1]/a/div/font')
invite.click()
driver.implicitly_wait(10)

#friend 1
frnd1_input = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/input')
frnd1_input.send_keys(FRIEND1)
driver.implicitly_wait(10)

#frnd1_click = driver.find_element_by_xpath(
#    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]')
#frnd1_click.click()

invite1 = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/a/span')
invite1.click()

#friend 2
frnd2_input = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/input')
frnd2_input.send_keys(FRIEND2)
driver.implicitly_wait(10)

#frnd2_click = driver.find_element_by_xpath(
#    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]')
#frnd2_click.click()

invite2 = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/a/span')
invite2.click()
time.sleep(10)

#adds random bot
randombot = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[5]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div[2]/a[2]')
randombot.click()
    
#random setting
randomsetting = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[3]/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/a')
randomsetting.click()

#starts the game
start = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div/div[6]/div[1]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div[4]/a')
start.click()
