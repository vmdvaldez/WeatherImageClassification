import os
# import urlibb.request
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup 
import subprocess
import time

URL = input("Enter Website (i.e. https://test.com): \n")
driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")

driver.get(URL)

pheight = driver.execute_script("return document.body.scrollHeight")
html = driver.find_element_by_tag_name('html')

t0 = time.time()
t1 = t0

timeout = 180
scroll_sleep = 2

while (t1 - t0 < timeout):
	print(t1 - t0)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	time.sleep(scroll_sleep)

	nheight = driver.execute_script("return document.body.scrollHeight")

	if pheight == nheight:
		print("BREAKING")
		break

	pheight = nheight
	t1 = time.time()


bs4 = BeautifulSoup(driver.page_source, "html5lib")

LOGDIR="http_logs/"

os.makedirs(os.path.dirname(LOGDIR), exist_ok=True)

images = bs4.findAll('img',{"src":True})


f = os.path.join(LOGDIR, "Test.txt")

file = open(f, "w+")
for img in images:
	file.write(img['src'] + '\n')

file.close()

subprocess.call("./get_images.sh")