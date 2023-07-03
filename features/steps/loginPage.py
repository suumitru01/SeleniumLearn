import time

from selenium import webdriver
from behave import given, when, then, step
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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


@then('I enter username as {user_name} and password as {pass_word}')
def enter_username(context, user_name, pass_word):
    time.sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]').send_keys(user_name)
    context.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(pass_word)


@step('I click on Login button')
def click_on_login_button(context):
    context.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


@step('I validate error message as {expected_message} on home screen')
def validate_invalid_error_msg(context, expected_message):
    time.sleep(3)
    actual_message = context.driver.find_element(By.CSS_SELECTOR, 'p[class="oxd-text oxd-text--p oxd-alert-content-text"]')
    assert expected_message == actual_message.text

@step('I close the browser')
def close_browser(context):
    context.driver.quit()