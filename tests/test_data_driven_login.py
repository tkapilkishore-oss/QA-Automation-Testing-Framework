import pytest
import time

from utils.driver_setup import get_driver
from utils.excel_reader import get_login_test_data
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected",
    get_login_test_data()
)

def test_data_driven_login(username, password, expected):

    driver = get_driver()

    login_page = LoginPage(driver)

    try:

        login_page.open()

        if str(username) != "nan":
            login_page.enter_username(str(username))

        if str(password) != "nan":
            login_page.enter_password(str(password))

        login_page.click_login()

        time.sleep(2)

        current_url = driver.current_url

        if expected == "success":

            assert "inventory" in current_url

        else:

            assert "inventory" not in current_url

        print(f"TEST PASSED -> {username}")

    except Exception as e:

        print(f"TEST FAILED -> {username}", e)

        raise

    finally:

        time.sleep(2)

        driver.quit()