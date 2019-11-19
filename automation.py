import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

user = input("username")
uid = input("uid")


driver = webdriver.Chrome()
driver.get('http://dellomo.ece.umd.edu/make_apt.php')



username_box = driver.find_element_by_name('studname')
username_box.send_keys(user)

uid_box = driver.find_element_by_name('uid')
uid_box.send_keys(uid)


rows = len(driver.find_elements_by_xpath("/html/body/form/p[8]/table/tbody/tr[1]/td"))
print(rows)

dict1 ={}
for row in driver.find_elements_by_xpath("/html/body/form/p[8]/table/tbody/tr"):
  i = 0
  while (i <rows):
    cell = row.find_elements_by_tag_name("td")[i]
    col = row.find_elements_by_tag_name("td")[i+1]
    dict1[cell.text]= col.text
    i +=4

print("The available slots are")
for key,value in dict1.items():
  if(value == 'Available'):
    print(key)
    
slot = input('enter the slot')
slot1 =  '//input[@value='+"'" + slot[:3]+' '+slot[3:]+' 0'+"'"+']' 
if(dict1[slot] == 'Available'):
    driver.find_element_by_xpath(slot1).click()
    print("your appointment is booked")
    print("Have a nice day")
else:
    print('the slot is not available')

submit = "//input[@value='Submit']"
driver.find_element_by_xpath(submit).click()




