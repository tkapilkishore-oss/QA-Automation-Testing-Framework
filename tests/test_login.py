from utils.driver_setup import get_driver
from utils.test_data import *
from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.screenshot_helper import capture_screenshot
import time
import os

logger=get_logger()

# Create screenshots folder
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")


# ---------------- VALID LOGIN TEST ----------------

def test_valid_login():

    driver = get_driver()

    login_page = LoginPage(driver)

    logger.info("Starting VALID LOGIN TEST")

    try:

        login_page.open()

        logger.info("Opened SauceDemo website")

        login_page.enter_username(VALID_USERNAME)

        logger.info("Entered username")

        login_page.enter_password(VALID_PASSWORD)

        logger.info("Entered password")

        login_page.click_login()

        logger.info("Clicked login button")

        time.sleep(2)

        assert "wrong_text" in driver.current_url

        logger.info("VALID LOGIN TEST PASSED")

    except Exception as e:

        logger.error(f"VALID LOGIN TEST FAILED: {e}")

        capture_screenshot(driver, "valid_login_failure")

        raise

    finally:

        logger.info("Closing browser")

        time.sleep(2)

        driver.quit()


# ---------------- INVALID LOGIN TEST ----------------

def test_invalid_login():

    driver = get_driver()

    login_page = LoginPage(driver)

    try:
        login_page.open()

        login_page.enter_username(INVALID_USERNAME)
        login_page.enter_password(INVALID_PASSWORD)

        login_page.click_login()

        time.sleep(2)

        error_message = login_page.get_error_message()

        assert "Epic sadface" in error_message

        logger.info("INVALID LOGIN TEST PASSED")

    except Exception as e:

        logger.error("INVALID LOGIN TEST FAILED: %s", e)

        capture_screenshot(driver, "invalid_login_failure")

        raise

    finally:

        time.sleep(2)

        driver.quit()


# ---------------- EMPTY USERNAME TEST ----------------

def test_empty_username():

    driver = get_driver()

    login_page = LoginPage(driver)

    try:
        login_page.open()

        login_page.enter_password(VALID_PASSWORD)

        login_page.click_login()

        time.sleep(2)

        error_message = login_page.get_error_message()

        assert "Username is required" in error_message

        logger.info("EMPTY USERNAME TEST PASSED")

    except Exception as e:

        logger.error("EMPTY USERNAME TEST FAILED: %s", e)

        capture_screenshot(driver, "empty_username_failure")

        raise

    finally:

        time.sleep(2)

        driver.quit()


# ---------------- EMPTY PASSWORD TEST ----------------

def test_empty_password():

    driver = get_driver()

    login_page = LoginPage(driver)

    try:
        login_page.open()

        login_page.enter_username(VALID_USERNAME)

        login_page.click_login()

        time.sleep(2)

        error_message = login_page.get_error_message()

        assert "Password is required" in error_message

        logger.info("EMPTY PASSWORD TEST PASSED")

    except Exception as e:

        logger.error("EMPTY PASSWORD TEST FAILED: %s", e)

        capture_screenshot(driver, "empty_password_failure")

        raise

    finally:

        time.sleep(2)

        driver.quit()