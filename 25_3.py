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

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys("al66@pf.com")
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys("1qasw2")
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
   #pytest.driver.get ('http://petfriends1.herokuapp.com/my_pets')
   #title = pytest.driver.find_element_by_css_selector ('head title')
   #assert title.get_attribute ("innerText") == "PetFriends: My Pets"

   pytest.driver.get ('https://petfriends1.herokuapp.com/my_pets')
   assert pytest.driver.title == "PetFriends: My Pets"
   time.sleep(2)
   images = pytest.driver.find_elements_by_css_selector ('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector ('.card-deck .card-img-top')
   descriptions = pytest.driver.find_elements_by_css_selector ('.card-deck .card-img-top')

   for i in range (len (names)):
      assert images[i].get_attribute ('src') != ''
      assert names[i].text != ''
      print (i, names)
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split (", ")
      assert len (parts[0]) > 0
      assert len (parts[1]) > 0