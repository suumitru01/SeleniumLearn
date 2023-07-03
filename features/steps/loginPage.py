from selenium import webdriver
from behave import given, when
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@given('I launch the browser')
def launch_browser(context):
    context.webdriver_service = Service("C:\\SeleniumLearn\\chromedriver_win32\\chromedriver.exe")
    context.webdriver_options = Options()
    context.webdriver_options.add_experimental_option("detach", True)
    context.driver = webdriver.Chrome(options=context.webdriver_options, service=context.webdriver_service)
    context.driver.maximize_window()
    context.driver.delete_all_cookies()


@when('I navigate to the url')
def navigate_to_url(context):
    expected_titleName = "OrangeHRM"
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    actual_titleName = context.driver.title
    assert expected_titleName == actual_titleName
