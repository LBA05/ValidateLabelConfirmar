import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe",options=options)
driver.get("https://lavandanatural.com/account/register/")
driver.maximize_window()
time.sleep(3)

requirement =()
labelObtained =()

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")

campoConfirmar= driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[5]/label")

labelCampoConfirmar = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[5]/label").text

labelObtained=labelCampoConfirmar

print(labelObtained)

requirement= 'CONFIRMAR CONTRASEÑA'

compareLabels()