import requests
from selenium.webdriver.common.by import By

from utils.driver_setup import get_driver


def test_broken_links():

    driver = get_driver()

    broken_links = []

    try:

        # Open website
        driver.get("https://www.saucedemo.com/")

        # Get all links
        links = driver.find_elements(By.TAG_NAME, "a")

        print(f"\nTotal Links Found: {len(links)}\n")

        for link in links:

            url = link.get_attribute("href")

            if url is not None:

                try:

                    response = requests.get(url, timeout=5)

                    print(f"{url} ---> {response.status_code}")

                    if response.status_code >= 400:
                        broken_links.append(url)

                except Exception as e:

                    print(f"ERROR checking {url}: {e}")

                    broken_links.append(url)

        print("\nBroken Links:")

        for broken in broken_links:
            print(broken)

        assert len(broken_links) == 0

    finally:

        driver.quit()