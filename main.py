from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


with open("database.txt", "w") as file:
    arquivo = file

arquivo = "OI"

with open("database.txt", "a") as file:
    file.write("oi\n") #read()

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@asmrmunuronkan/shorts")

links = ""

input_element = driver.find_elements(By.PARTIAL_LINK_TEXT, " ")
for video in input_element:
    time.sleep(1)
    link_atual = video.get_attribute("href")
    if "short" in link_atual:
        links += f"{video.get_attribute("href")}\n"

with open("database.txt", "a") as file:
    file.write(links)

time.sleep(3)

driver.quit()