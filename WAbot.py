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
from fileHandling import FileHandlingClass as fileHandling


#Firefox_browser = webdriver.Firefox()  # Change the path as per your local dir.
#Firefox_browser.get('https://web.whatsapp.com/')
class WAbotClass:
    def __init__(self, Firefox_browser):
        self.Firefox_browser = Firefox_browser

    #This is a function that will send a message
    def clickSendButton(self):
        # Click on send button
        btn_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button'
        message_box =self.Firefox_browser.find_element_by_xpath(btn_xpath)
        message_box.click()

    def sendMessage(self, targetName, msgToSend):
        # Typing message into message box
        wait = WebDriverWait(self.Firefox_browser, 10)
        wait5 = WebDriverWait(self.Firefox_browser, 5)
        inp_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
        time.sleep(1)
                    
        input_box.send_keys(msgToSend)
        self.clickSendButton()
    # Function for getting user from
    def new_chat(self, targetName):
        # Selecting the new chat search textbox
        new_chat = self.Firefox_browser.find_element_by_xpath('//div[@class="ZP8RM"]')
        new_chat.click()

        # Enter the name of chat
        new_user =self.Firefox_browser.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
        new_user.send_keys(user_name)

        time.sleep(1)

        try:
            # Select for the title having user name
            user = self.Firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user.click()
        except NoSuchElementException:
            print('Given user "{}" not found in the contact list'.format(user_name))
        except Exception as e:
            # Close the browser
            self.Firefox_browser.close()
            print(e)
            sys.exit()

    def findContact(self, targetName):
        # Select for the title having user name
        user = self.Firefox_browser.find_element_by_xpath('//span[@title="{}"]'.format(targetName))
        user.click()

    def openWA(self):
        self.Firefox_browser.get('https://web.whatsapp.com')
