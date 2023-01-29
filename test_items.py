from selenium.webdriver.common.by import By
import time  # for manual testing

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)

    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        present_btn = True
    except NoSuchElementException:
        present_btn = False
    assert present_btn, "'Add-to-basket' button is not found"

