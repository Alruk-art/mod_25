#python -m pytest -v --driver Chrome --driver-path c://brodriver/chromedriver  25_4.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(autouse=True)
def login():
   pytest.driver = webdriver.Chrome('c://brodriver/chromedriver')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')
   pytest.driver.find_element_by_id ('email').send_keys ("al66@pf.com")
   pytest.driver.find_element_by_id ('pass').send_keys ("1qasw2")
   pytest.driver.find_element_by_css_selector ('button[type="submit"]').click ()


   yield
   pytest.driver.quit()

def test_main_page():
    pytest.driver.get ('http://petfriends1.herokuapp.com/all_pets')
    assert pytest.driver.find_element_by_tag_name ('h1').text == 'PetFriends'


def test_explicitly_wait_pet_grid():
    pytest.driver.get ('http://petfriends1.herokuapp.com/all_pets')
    #element = WebDriverWait(pytest.driver, 8).until(
    #   ec.presence_of_element_located((By.CSS_SELECTOR, '.text-center')))
    #element = WebDriverWait (pytest.driver, 9).until (
    #    ec.presence_of_element_located ((By.CSS_SELECTOR, '.card-deck')))
    element = WebDriverWait (pytest.driver, 7).until (
        ec.presence_of_element_located ((By.CSS_SELECTOR, '.task2.fill')))
    assert element

def test_implicitly_wait_pet_properties():
    pytest.driver.implicitly_wait(7)
    pytest.driver.get('http://petfriends1.herokuapp.com/all_pets')
    assert pytest.driver.find_element_by_class_name('card-img-top')
    assert pytest.driver.find_element_by_class_name('card-title')
    assert pytest.driver.find_element_by_class_name('card-text')