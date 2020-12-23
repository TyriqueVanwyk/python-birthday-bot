#!/usr/bin/env python3
import sys
import time

#import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime

Firefox_browser = webdriver.Firefox()  # Change the path as per your local dir.
Firefox_browser.get('https://web.whatsapp.com/')
#This is a function that will send a message
def clickSendButton():
    # Click on send button
    btn_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button'
    message_box = Firefox_browser.find_element_by_xpath(btn_xpath)
    message_box.click()

def sendMessage(targetName, msgToSend):
    # Typing message into message box
    wait = WebDriverWait(Firefox_browser, 10)
    wait5 = WebDriverWait(Firefox_browser, 5)
    inp_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
    time.sleep(1)
                
    input_box.send_keys(msgToSend)
    clickSendButton()

# Function for getting user from
def new_chat(targetName):
    # Selecting the new chat search textbox
    new_chat = Firefox_browser.find_element_by_xpath('//div[@class="ZP8RM"]')
    new_chat.click()

    # Enter the name of chat
    new_user =Firefox_browser.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(1)

    try:
        # Select for the title having user name
        user = Firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        Firefox_browser.close()
        print(e)
        sys.exit()

def findContact(targetName):
    try:
        # Select for the title having user name
        user = Firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(targetName))
        user.click()
    except NoSuchElementException as se:
        new_chat(targetName)

        
if __name__ == '__main__':

    options = webdriver.FirefoxOptions()
    options.add_argument('--user-data-dir=<User Data Path>')
    options.add_argument('--profile-directory=Default')

    # Register the drive
    #Firefox_browser = webdriver.Firefox()  # Change the path as per your local dir.
    #Firefox_browser.get('https://web.whatsapp.com/')

    # Sleep to scan the QR Code
    time.sleep(15)

    user_name_list = ['Jade']

    for user_name in user_name_list:

        findContact(user_name)
        msgToSend = 'The whatsapp bot worked!'
        sendMessage(user_name, msgToSend)
    Firefox_browser.close()


