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

pheight = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:

	time.sleep(2)

	nheight = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	if pheight == nheight:
		break

	pheight = nheight

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