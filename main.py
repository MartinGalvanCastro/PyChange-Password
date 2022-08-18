from json import load
from json import dump
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyfiglet



def update_account(account: dict):
    """
    Function that updates the current index
    :param account: account to be updated
    :return: account with index updated
    """
    pass_length = len(account['passwords'])
    current = account['current']
    if current == pass_length - 1:
        current = 0
        account['current'] = current
    else:
        current += 1
        account['current'] = current
    return [account, account['passwords'][current], account['passwords'][current - 1]]


def update_json_file(file, data: dict):
    file.seek(0)
    dump(data, file, indent=4)
    file.truncate()


def select_driver(nav_options: list):
    """
    Function that select the desired browser
    :param nav_options:
    :return:
    """
    flag = True  # Flag for non valid options
    while flag:
        print("Please select a browser installed in your PC: ")
        for idx, nav in enumerate(nav_options):
            print(f"{idx + 1}. {nav}")
        default = int(input()) - 1

        # If not valid option retry
        if default > len(nav_options) or default < 0:
            print("Please select a valid option")

        # Using Chrome
        elif default == 0:
            from selenium.webdriver.chrome.service import Service as ChromeService
            from webdriver_manager.chrome import ChromeDriverManager
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Using Firefox
        elif default == 1:
            from selenium.webdriver.firefox.service import Service as FirefoxService
            from webdriver_manager.firefox import GeckoDriverManager
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        # Using Edge
        elif default == 2:
            from selenium.webdriver.edge.service import Service as EdgeService
            from webdriver_manager.microsoft import EdgeChromiumDriverManager
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


if __name__ == '__main__':
    result = pyfiglet.figlet_format("PyChange Password", font="digital", width=200)
    print(result)
    browsers = ['Chrome', 'Firefox', 'Edge']

    # Load config file
    with open('./config.json', "r+") as file:
        account = load(file)

        # Update Password
        account, new_pass, old_pass = update_account(account)

        driver = select_driver(browsers)
        driver.maximize_window()
        
        driver.get(account['website'])
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            driver.find_element(By.ID, 'username').send_keys(account['user'])
            driver.find_element(By.ID, 'password').send_keys(old_pass)
            driver.find_element(By.ID, 'password1').send_keys(new_pass)
            driver.find_element(By.ID, 'password2').send_keys(new_pass)
            driver.find_element(By.ID,"submit").click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Ir al correo"))
            )

        finally:
            update_json_file(file, account)
            driver.close()

        print(f"Old Password is: {old_pass}")
        print(f"New Password is: {new_pass}")
        print("Thanks for using PyChange My Password")