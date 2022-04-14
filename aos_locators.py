import datetime
from faker import Faker
fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_loginurl = 'https://advantageonlineshopping.com/#/myAccount'
aos_title = f'\xa0''Advantage Shopping'
aos_registerUrl = 'https://advantageonlineshopping.com/#/register'
aos_speakers = 'https://advantageonlineshopping.com/#/category/Speakers/4'
aos_tablets = 'https://advantageonlineshopping.com/#/category/Tablets/3'
aos_headphones = 'https://advantageonlineshopping.com/#/category/Headphones/2'
aos_laptops = 'https://advantageonlineshopping.com/#/category/Laptops/1'
aos_mice = 'https://advantageonlineshopping.com/#/category/Mice/5'
aos_orderpage = 'https://advantageonlineshopping.com/#/MyOrders'
new_username = f'{fake.user_name()}{fake.pyint(11,99)}'[:15]
new_password = fake.password()[:12]
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
description1 = fake.sentence(nb_words=30)
description = f'User added by {new_username} via Python Selenium Automated script on {datetime.datetime.now()}'
pic_desc = fake.user_name()
phonetic_name = fake.user_name()[:15]
list_of_interests = [new_username, new_password, full_name, email, city]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text='????????????????????')
department = fake.lexify(text='???????')
phone = fake.phone_number()
mobile_phone = fake.phone_number()
# address = fake.address()
# address = fake.address().replace("\n", "")
address = fake.street_address()
postal_code = fake.postalcode()
province_code = fake.province_abbr()
country_code = fake.current_country_code()
street_city_region = f'{country_code}/{province_code}'
order_number = ""
