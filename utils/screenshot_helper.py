import os
from datetime import datetime


def capture_screenshot(driver, test_name):

    # Create screenshots folder if not exists
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # File path
    file_path = f"screenshots/{test_name}_{timestamp}.png"

    # Save screenshot
    driver.save_screenshot(file_path)

    return file_path