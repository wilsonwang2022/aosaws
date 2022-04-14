import sys
import datetime
from time import sleep
import aos_locators as locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

global shippingname1
global ordernumber
global my_ordernumber
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def setUp():
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.aos_url)

    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'---------------------------------------------------------------------------')
        print(f'We are at the correct web page, {driver.current_url}')
        print(f'We are see the correct title page:{driver.title}')
    else:
        print(f'We are not at the correct home page. try again/check your code')
        driver.close()  # close the current tab
        driver.quit()  # close the browser completely


def create_new_user():
    if driver.current_url == locators.aos_url and driver.title == locators.aos_title:
        print(f'---------------------------------------------------------------------------')
        print(f'We are at the correct web page, {driver.current_url}')
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(1)
        if driver.current_url == locators.aos_registerUrl:
            driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
            driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
            driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
            driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
            driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
            sleep(1)
            driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
            driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
            Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
            driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
            driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.street_city_region)
            driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
            driver.find_element(By.NAME, 'i_agree').click()
            driver.find_element(By.ID, 'register_btnundefined').click()
            sleep(1)
            if driver.find_element(By.XPATH, f'//*[contains(., "{locators.new_username}")]').is_displayed():
                print('you have created new user: ' + locators.new_username)
                print('your password is: ' + locators.new_password)


def check_user_created():
    # Check that we are on the User's Main Page
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        sleep(2)
        driver.find_element(By.ID, 'menuUserLink').click()
        print(f'---------------------------------------------------------------------------')
        print(f'this is: {driver.title}')
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id = "loginMiniTitle"]/label[1]').click()
        print('Verified the new user: ' + locators.new_username)
        print('Verified the password is: ' + locators.new_password)
        sleep(1)


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id = "loginMiniTitle"]/label[3]').click()
    # driver.find_element(By.XPATH, '//*[contains(., "Sign out")]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'---------------------------------------------------------------------------')
        print(f'the log out successfuly done at : {datetime.datetime.now()}')
        sleep(1)


def tearDown():
    if driver is not None:
        print(f'---------------------------------------------------------------------------')
        print(f'Wishing you have a good day')
        print(f'test was completed at :{datetime.datetime.now()}')
        driver.close()
        driver.quit()
        old_instance = sys.stdout
        log_file = open('message.log', 'w')
        sys.stdout = log_file
        print(f'Email: {locators.email}\nUsername: {locators.new_username}\nPassword: {locators.new_password}\n'
              f'Full Name: {locators.full_name}')
        sys.stdout = old_instance
        log_file.close()


def log_in():
    # if driver.current_url == locators.aos_loginurl:
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    if driver.current_url == locators.aos_url:
        driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        print(f'---------------------------------------------------------------------------')
        print(f'We are at the correct web page, {driver.current_url}')


def delete_a_user():
    if driver.current_url == locators.aos_loginurl:
        driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[6]/button').click()
        sleep(2)
        driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
        sleep(1)
        print(f'---------------------------------------------------------------------------')
        print(f'--- Account with username {locators.new_username} has been deleted successfully. Test passed ---')
        print(f'Account deleted successfully at: {datetime.datetime.now()}')
        sleep(5)
    else:
        print(f'Unable to delete New Account. Something went wrong.')


def verified_delete_user():
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(1)
        driver.find_element(By.XPATH, "//input[@name= 'username']").send_keys(locators.new_username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]').is_displayed()
        print(f'---------------------------------------------------------------------------')
        print(f'Verified {locators.new_username} has been deleted')
    else:
        print(f'This is not currect webpage')


# Validate Homepage Text, Links and Top Navigation Menu
def validate_homepage_text():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.ID, "speakersTxt").click()
        if driver.current_url == locators.aos_speakers:
            print(f'=================================================================')
            print(f'Validate SPEAKERS is displayed')
            sleep(2)
            driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
            sleep(1)
            driver.find_element(By.ID, "tabletsTxt").click()
            if driver.current_url == locators.aos_tablets:
                print(f'------------------------------------------------------------------------')
                print(f'Validate TABLETS is displayed')
                sleep(2)
                driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                sleep(1)
                driver.find_element(By.ID, "laptopsTxt").click()
                if driver.current_url == locators.aos_laptops:
                    print(f'------------------------------------------------------------------------')
                    print(f'Validate LAPTOPS is displayed')
                    sleep(2)
                    driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                    sleep(1)
                    driver.find_element(By.ID, "headphonesTxt").click()
                    if driver.current_url == locators.aos_headphones:
                        print(f'------------------------------------------------------------------------')
                        print(f'Validate HEADPHONES is displayed')
                        sleep(2)
                        driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                        sleep(1)
                        driver.find_element(By.ID, "miceTxt").click()
                        if driver.current_url == locators.aos_mice:
                            print(f'------------------------------------------------------------------------')
                            print(f'Validate MICE is displayed')
                            sleep(2)
                            driver.find_element(By.XPATH, '//a[contains(., "HOME")]').click()
                            sleep(1)
    else:
        print('It is correct homepage, try again')


def validate_links():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
        if driver.find_element(By.ID, 'special_offer_items').is_displayed():
            print(f'---------------------------------------------------------')
            print('SPECIAL OFFER Link is displayed')
            driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
            if driver.find_element(By.ID, 'popular_items').is_displayed():
                print(f'---------------------------------------------------------')
                print('POPULAR ITEMS Link is displayed')
                driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
                if driver.find_element(By.ID, 'supportCover').is_displayed():
                    print(f'---------------------------------------------------------')
                    print('CONTACT US Link is displayed')
    else:
        print('the links are not displayed, try again')


def validate_main_logo():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.XPATH, '//a[@href="#/"]').click()
        if driver.find_element(By.LINK_TEXT, 'OUR PRODUCTS').is_displayed():
            print(f'==========================================================')
            print('Main logo is displayed')
    else:
        print('It is not correct main logo link, try again')


def validate_contact_us_form():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
            Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Speakers')
            sleep(1)
            Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text(
                'Bose Soundlink Bluetooth Speaker III')
            sleep(1)
            driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
            sleep(1)
            driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description1)
            sleep(1)
            driver.find_element(By.ID, 'send_btnundefined').click()
            sleep(1)
            print(f'========================================================')
            print('It is already diaplayed Contact Us links')
            if driver.find_element(By.XPATH,
                                   '//*[contains(.,"Thank you for contacting Advantage support.")]').is_displayed():
                driver.find_element(By.XPATH, '//a[contains(., "CONTINUE SHOPPING ")]').click()
                print('Thank You and Continue to Shopping!')
    else:
        print('It is not correct to contact us form, try again')


def validate_facebook():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
            driver.find_element(By.NAME, 'follow_facebook').click()
            sleep(1)
            print('swtich to facebook homepage')
            p = driver.window_handles[0]
            c = driver.window_handles[1]
            driver.switch_to.window(c)
            if driver.current_url == 'https://www.facebook.com/MicroFocus/':
                sleep(2)
                print(f'===============================================')
                print('It is Facebook homepage')
                driver.close()
                sleep(1)
                driver.switch_to.window(p)


def validate_twitter():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
            driver.find_element(By.NAME, 'follow_twitter').click()
            sleep(1)
            p = driver.window_handles[0]
            c = driver.window_handles[1]
            driver.switch_to.window(c)
            if driver.current_url == 'https://twitter.com/MicroFocus':
                sleep(2)
                print(f'------------------------------------------------')
                print('It is twitter homepage')
                driver.close()
                sleep(1)
                driver.switch_to.window(p)


def validate_linkdin():
    if driver.current_url == locators.aos_url:
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(1)
        if driver.find_element(By.ID, 'supportCover').is_displayed():
            driver.find_element(By.NAME, 'follow_linkedin').click()
            sleep(1)
            p = driver.window_handles[0]
            c = driver.window_handles[1]
            driver.switch_to.window(c)
            if "LinkedIn" in driver.title:
                sleep(2)
                print(f'------------------------------------------------')
                print('It is LinkedIn homepage')
                driver.close()
                driver.switch_to.window(p)
                print('We already checked social media links, well done!')
    else:
        print('It is not correct to social media links, try again')


def checkout_shopping_cart():
    global shippingname1
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, "speakersTxt").click()
        if driver.current_url == locators.aos_speakers:
            driver.find_element(By.ID, "20").click()
            sleep(1)
            driver.find_element(By.NAME, "save_to_cart").click()
            sleep(1)
            driver.find_element(By.ID, "menuCart").click()
            driver.find_element(By.ID, "checkOutButton").click()
            sleep(1)
            driver.find_element(By.ID, "next_btn").click()
            sleep(1)
            driver.find_element(By.NAME, 'safepay_username').send_keys(locators.phonetic_name)
            driver.find_element(By.NAME, 'safepay_password').send_keys(locators.new_password)
            driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()
            sleep(1)
            if driver.find_element(By.XPATH, '//*[contains(., "Thank you for buying with Advantage")]').is_displayed():
                sleep(1)
                print('it is order payment page, and Thank you for buying with Advantage is displayed')
                labels = driver.find_elements(By.XPATH, '//label[@ID="trackingNumberLabel"]')
                for label1 in labels:
                    print(f'The tracking number is: {label1.text}')
                ordernumbers = driver.find_elements(By.XPATH, '//label[@ID="orderNumberLabel"]')
                for order_number in ordernumbers:
                    locators.order_number = order_number.text
                    print(f'The Order is created, the order number is: {order_number.text}')
                shipnames = driver.find_elements(By.XPATH, '//div[@class="innerSeccion"]/label[@class="ng-binding"]')
                for shippingname1 in shipnames:
                    # print(f'shippingname is: {shippingname1.text}')
                    if locators.full_name in shippingname1.text:
                        print(f'Validate the order Full Name: {locators.full_name} is correct')
                    if locators.phone in shippingname1.text:
                        print(f'Validate The Order Phone number: {locators.phone} is correct')
                        sleep(1)


def validate_orderpage():
    # if driver.current_url == locators.aos_url:
    global my_ordernumber
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(2)
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id = "loginMiniTitle"]/label[2]').click()
    sleep(1)
    if driver.current_url == locators.aos_orderpage:
        my_ordernumber = driver.find_element(By.XPATH, f'//label[contains(text(), "{locators.order_number}")]')
        sleep(1)
        assert my_ordernumber.is_displayed()
        sleep(1)
        print('===========================================================================')
        print(f'validate order is displayed -order number is: {locators.order_number}-- confirmed!')
        sleep(1)
    else:
        print('it is not correct order number')


def delete_order():
    driver.find_element(By.XPATH, f"//*[contains(.,'{locators.order_number}')]/../td/span/a[text()='REMOVE']").click()
    sleep(1)
    driver.find_element(By.ID, 'confBtn_1').click()
    sleep(1)
    try:
        assert my_ordernumber.is_displayed()
    except (AssertionError, StaleElementReferenceException):
        print('-------------------------------------------------------------------------')
        print(f'My_ordernumber is not found:')
        print(f'my order already deleted successfully')

    else:
        print('Order not validated. Please try to check your order number again.')


# setUp()
# validate_homepage_text()
# validate_links()
# validate_main_logo()
# validate_contact_us_form()
# validate_facebook()
# validate_twitter()
# validate_linkdin()
# create_new_user()
# check_user_created()
# log_out()
# log_in()
# checkout_shopping_cart()
# log_out()
# log_in()
# validate_orderpage()
# delete_order()
# log_out()
# log_in()
# check_user_created()
# delete_a_user()
# verified_delete_user()
# tearDown()
