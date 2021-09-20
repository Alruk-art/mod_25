#запуск из файла как обычно
# или терминал cd C:\pythonProject\SF_mod_25
# python -m pytest -v --driver Chrome --driver-path c://brodriver/chromedriver 25_3.py
# разница не будет выведено количество питомцев


import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('c://brodriver/chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield pytest.driver

   pytest.driver.quit ()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys("al66@pf.com")
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys("1qasw2")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   # pytest.driver.get ('https://petfriends1.herokuapp.com/my_pets')
   # второй способ перейти на свою страницу через click
   pytest.driver.find_element_by_css_selector('#navbarNav [href="/my_pets"]').click()
   text = pytest.driver.find_element_by_tag_name('h2').text
   print ('text=',text )
   assert pytest.driver.find_element_by_tag_name('h2').text == 'al66'
   time.sleep(2)

   am_names = pytest.driver.find_elements_by_css_selector ('.table-hover td.smart_cell')
   images = pytest.driver.find_elements_by_css_selector ('.table-hover img')
   descriptions = pytest.driver.find_elements_by_css_selector ('.table-hover td')
   #count_of_my_pets = pytest.driver.find_elements_by_xpath('//*[h2][1]').text.split()[2]
   #print (count_of_my_pets)
   pet_images = []
   amount=pytest.driver.find_element_by_xpath('//body/div[1]/div/div[1]').text.split()[2]
   # assert len(am_names) == am_names
   print ('количество=', amount)

