import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

google = 'https://www.google.com/images'


def run():
    driver = init()
    search_box = driver.find_element_by_name('q')
    search_box.clear()
    search_box.send_keys('python language')
    search_box.send_keys(Keys.RETURN)

    # submit = driver.find_element()
    #
    # new_driver = driver.window_handles[1]

    print(driver.text)

    image_page = driver.find_elements_by_class_name('rg_i Q4LuWd')
    print(image_page)
    # for element in image_page:
    #     print('in for loop')
    #     element.click()
    #     time.sleep(1)
    #     e = driver.find_elements_by_class_name('v4dQwb')


    # time.sleep(10)
    # driver.close()


def init():
    print('Initializing...')

    driver = webdriver.Firefox(executable_path='web_drivers/geckodriver.exe')
    driver.get(google)
    assert 'google' in driver.title.lower()
    print('Connecting to Google Images...')
    return driver


if __name__ == '__main__':
    run()
