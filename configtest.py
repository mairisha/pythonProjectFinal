import pytest
import yaml
import requests


with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = my_dict['url']
url1 = my_dict['url1']

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser1 = testdata["browser"]

@pytest.fixture()
def login():
    obj_data = requests.post(url=url, data={'username':'KiraZ2', 'password': 'gi89mjb90f'})
    token = obj_data.json()['token']
    return token

@pytest.fixture()
def postP():
    obj_data = requests.post(url=url1, headers={"X-Auth-Token": my_dict['token']},data={
        'username':'KiraZ2',
        'password': 'gi89mjb90f',
        'title': 'newTitle',
        'description': 'Anything',
        'content':'we will see'})
    return obj_data.json()['description']
@pytest.fixture(scope="session")
def browser():
    if browser1 == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()