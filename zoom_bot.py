from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import keyboard

class zoom_bot:
	def join(self,meeting_link):
		self.bot = webdriver.Chrome("chromedriver.exe")
		self.bot.get(meeting_link)
		time.sleep(1000)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("tab", do_press=True, do_release=True)
		keyboard.send("enter", do_press=True, do_release=True)
		time.sleep(1000)

		self.bot.quit()

link = open("meeting_link","r").read()		


obj = zoom_bot()
obj.join(link)