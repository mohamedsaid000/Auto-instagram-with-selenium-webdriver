from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.instagram.com/")
time.sleep(3)

username = driver.find_element_by_name("username")
username.send_keys("username")
password = driver.find_element_by_name("password")
password.send_keys("password")

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()

time.sleep(5)


turn_on = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]')
turn_on.click()

time.sleep(3)




#create an array that will generate numbers
Number = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

def follow():
    
    driver.get("https://www.instagram.com/explore/people/suggested/")
    time.sleep(2)
    #follow people

    for id in Number:
        #time.sleep(1)
        follow = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[2]/div/div/div["+id+"]/div[3]/button")
        follow.click()
        
    time.sleep(3)

follow()    

def unfollow():
  driver.get("https://www.instagram.com/chatbot0989/")
  time.sleep(2)
  see = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
  see.click()
  
  for id in Number:
        follow = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+id+"]/div/div[3]/button")
        follow.click()
        
        follow = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
        follow.click()
#unfollow()

