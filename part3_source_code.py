#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Firefox()
url = "ここに表示させたいHPのURLを書く"
browser.get(url)

###################
###
###　これ以降はHPによりチューニングが必要です。
###　動画で解説します。
###
###################
"""
names_xpath = "//*[@id=\"mw-content-text\"]/div/table[5]/tbody/tr[*]/td[1]/a"
abstract_xpath ="/html/body/div[3]/div[3]/div[4]/div/p[1]"

idol_elements = browser.find_elements(By.XPATH, names_xpath)

for idol_element in idol_elements:
    name = idol_element.text
    print(name)
sleep(3)
idol_element.click()
abstract_element = browser.find_element(By.XPATH, abstract_xpath)
abstract = abstract_element.text
print(abstract)
"""
