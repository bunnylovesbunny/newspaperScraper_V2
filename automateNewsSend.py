from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform
import json

options = Options()



# f = open("scraped_english_articles.json", "r")
# message = f.read()
# f.close()

######################### code for sending new########################
with open ('scraped_english_articles.json') as access_json:
	read_content = json.load (access_json)

newspapers = [ 'bbc' , 'thedailystar' , 'banglatribune' ]
for newspaper in newspapers:
	article_list = read_content.get ('newspapers').get (newspaper).get ('articles')
	for i in article_list:
		values = i.values ()
		values_list = list (values)
		listToStr = '~~'.join (map (str , values_list))
		# print(listToStr,'\n')
		l = listToStr.split ('~~')

		message = "Link: " + l [ 0 ] + \
				 "\nPublished: " + l [ 1 ] \
				 + "\nTitle: " + l [ 2 ] \
				 + "\nSummary: " + l [ 3 ] + "\n"

		print ('This is your message..')
		print (message)
		message = quote (message)

		numbers = [ ]
		f = open ("numbers.txt" , "r")
		for line in f.read ().splitlines ():
			if line != "":
				numbers.append (line)
		f.close ()
		total_number = len (numbers)

		print ('\nWe found ' + str (total_number) + ' numbers in the file')

		print ()
		delay = 30

		if platform == "win32":
			driver = webdriver.Chrome ("drivers\\chromedriver.exe" , options=options)
		else:
			driver = webdriver.Chrome ("./drivers/chromedriver" , options=options)
		print ('Once your browser opens up sign in to web whatsapp')
		driver.get ('https://web.whatsapp.com')
		input ("Press ENTER after login into Whatsapp Web and your chats are visiable	.")
		for idx , number in enumerate (numbers):
			if number == "":
				continue
			print ('{}/{} => Sending message to {}.'.format ((idx + 1) , total_number , number))
			try:

				url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
				driver.get (url)
				try:
					click_btn = WebDriverWait (driver , delay).until (
						EC.element_to_be_clickable ((By.CLASS_NAME , '_2Ujuu')))
				except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
					print ("alert present")
					Alert (driver).accept ()
				sleep (1)
				click_btn.click ()
				sleep (3)
				print ('Message sent to: ' + number)
			except Exception as e:
				print ('Failed to send message to ' + number + str (e))




# numbers = []
# f = open("numbers.txt", "r")
# for line in f.read().splitlines():
# 	if line != "":
# 		numbers.append(line)
# f.close()
# total_number=len(numbers)
#
# print('\nWe found ' + str(total_number) + ' numbers in the file')
#
# print()
# delay = 30
#
# if platform == "win32":
# 	driver = webdriver.Chrome("drivers\\chromedriver.exe", options=options)
# else:
# 	driver = webdriver.Chrome("./drivers/chromedriver", options=options)
# print('Once your browser opens up sign in to web whatsapp')
# driver.get('https://web.whatsapp.com')
# input("Press ENTER after login into Whatsapp Web and your chats are visiable	.")
# for idx, number in enumerate(numbers):
# 	if number == "":
# 		continue
# 	print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number))
# 	try:
# 		######################### code for sending new########################
# 		with open ('scraped_english_articles.json') as access_json:
# 			read_content = json.load (access_json)
#
# 		newspapers = [ 'bbc' , 'thedailystar' , 'banglatribune' ]
# 		for newspaper in newspapers:
# 			article_list = read_content.get ('newspapers').get (newspaper).get ('articles')
# 			for i in article_list:
# 				values = i.values ()
# 				values_list = list (values)
# 				listToStr = '~~'.join (map (str , values_list))
# 				# print(listToStr,'\n')
# 				l = listToStr.split ('~~')
#
# 				message = "Link: " + l [ 0 ] + \
# 						  "\nPublished: " + l [ 1 ] \
# 						  + "\nTitle: " + l [ 2 ] \
# 						  + "\nSummary: " + l [ 3 ] + "\n"
#
# 				print ('This is your message..')
# 				print (message)
# 				message = quote (message)
#
# 				url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
# 				driver.get (url)
# 				try:
# 					click_btn = WebDriverWait (driver , delay).until (
# 						EC.element_to_be_clickable ((By.CLASS_NAME , '_2Ujuu')))
# 				except (UnexpectedAlertPresentException , NoAlertPresentException) as e:
# 					print ("alert present")
# 					Alert (driver).accept ()
# 				sleep (1)
# 				click_btn.click ()
# 				sleep (3)
# 				print ('Message sent to: ' + number)
# 			except Exception as e:
# 			print ('Failed to send message to ' + number + str (e))

	# 	url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
	# 	driver.get(url)
	# 	try:
	# 		click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME , '_2Ujuu')))
	# 	except (UnexpectedAlertPresentException, NoAlertPresentException) as e:
	# 		print("alert present")
	# 		Alert(driver).accept()
	# 	sleep(1)
	# 	click_btn.click()
	# 	sleep(3)
	# 	print('Message sent to: ' + number)
	# except Exception as e:
	# 	print('Failed to send message to ' + number + str(e))
