# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("http://www.nexushd.org/signin.php")
On_Internet = 1
# this block is to log in
try:
	elem = driver.find_element_by_name("username")
	elem.clear()
	elem.send_keys("CodeSausage")
	elem = driver.find_element_by_name("password")
	elem.clear()
	elem.send_keys("123456grc")
	driver.find_element_by_class_name("btn").click()
except:
	driver.close()
	print "\n"
	print "Hey! You didn't connect the Internet!\n \
	   Try again when you connect the Internet later."
	On_Internet = 0

# this block is to comment.
if On_Internet:
	try:
		elem = driver.find_element_by_name("content")
		elem.clear()
		elem.send_keys("That's Awesome!")
		driver.find_element_by_xpath(u"//img[@style='max-width: 25px;']").click()
		driver.find_element_by_id("qr").click()
		driver.close()
		print "\n"
		print "OK, you have signed up successfully. 	\
		Think what you should do, make a plan, and make it real."
	except NoSuchElementException:
	#抛出异常，抓住异常并且保证仍然关闭浏览器
		driver.close()
		print "\n"
		raw_input("Hey, you have signed up today! \
		Go to do what you should do!")
# finally:
# 	driver.close()
