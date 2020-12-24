import sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime

from WAbot import  WAbotClass 
from fileHandling import FileHandlingClass

if __name__ == '__main__':
    print("Press 1 for file handling and 2 to continue to the whatsappbot")
    print("")
    print("1. file handling")
    print("2. Whatsapp Bot")
    print("0. Quit")
    print("------------------------------------------------------------------")
    choice = input()
    print("------------------------------------------------------------------")
    try:
        if choice == '1':
            fh.useMenu();
        if choice == '2':    
            options = webdriver.FirefoxOptions()
            options.add_argument('--user-data-dir=<User Data Path>')
            options.add_argument('--profile-directory=Default')
            # Register the drive
            Firefox_browser = webdriver.Firefox()  # Change the path as per your local dir.
            #create Whatsapp bot class
            WAbot= WAbotClass(Firefox_browser)
            # create file handling class
            fh = FileHandlingClass('Birthdays.txt')
            #open whatsapp using driver
            #Firefox_browser.get('https://web.whatsapp.com/')
            WAbot.openWA()
            # Sleep to scan the QR Code
            input("Scan the QR code and press Enter")
            # Wait for the site to load
            time.sleep(10)
            contacts = fh.readContacts()

            for contact in contacts['people']:
                #find contact
                contactName = contact['name']
                WAbot.findContact(contactName)
                msgToSend = 'The whatsapp bot worked!'
                #send message
                WAbot.sendMessage(contactName, msgToSend)
            Firefox_browser.close()
    except Exception as e:
        print(e)
