from selenium import webdriver
#pip install selenium

import time

#insert ur login details

rollno="18K0159"#no dash

Password="nhk12040"
browser=webdriver.Chrome()
browser.get(("http://flexstudent.nu.edu.pk/"))
username = browser.find_element_by_id('m_inputmask_4')
username.send_keys(rollno)
password= browser.find_element_by_id('pass')
password.send_keys(Password)
