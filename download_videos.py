from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with open("database.txt", "r") as file:
    links = file.read()

lista = []
link = ""

for letra in links:
    link += letra
    if letra == "\n":
        lista.append(link)
        link = ""

print(lista)

