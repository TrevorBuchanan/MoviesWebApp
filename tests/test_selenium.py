import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep


#
# python3 -m pytest -v tests/test_selenium.py 
#

# Member fixure
@pytest.fixture
def member1():
    return  {'username':'arslanay', 'email':'arslanay@wsu.edu', 'password':'strongpassword'}

# Member fixure
@pytest.fixture
def member2():
    return  {'username':'john', 'email':'john@wsu.edu', 'password':'alsostrongpassword'}

# Member fixures
@pytest.fixture
def member2():
    return  {'username':'john', 'email':'john@wsu.edu', 'password':'alsostrongpassword'}

 # Review fixure
@pytest.fixture
def review1():
    return {'title': 'My cat Cookie', 
            'review': 'My cat Cookie and his girlfriend Chia watch the sunset together everyday. I need to go home before sunset to let her out. Sometimes when I get home, I find Chia outside of our front window staring at Cookie at the window.' , 
            'rating': 1}

 # Review fixure
@pytest.fixture
def review2():
    return {'title': 'Stolen book', 
            'review': 'Today, while I was browsing in a secondhand bookshop, I found a copy of a book that had been stolen from me when I was a kid. I opened it and saw, on the first page, in familiar hand writing, my own name. It had been a gift from my (now late) grandfather. Next to my name my grandfather wrote, “I hope you rediscover this book someday when you’re older, and it makes you think about the important things in life.' , 
            'rating': 2}

 # Review fixure
@pytest.fixture
def review3():
    return {'title': 'People chain', 
            'review': """While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.
                       While hiking in Muir woods a car suddenly drove off the road into a river. Immediately three separate groups of strangers stopped and began sprinting to the scene. The first three to arrive were from different groups and immediately made a human chain to allow the first person to repel down the hill. The group pulled all four people from the black sedan. After the ordeal, there was a moment when all the strangers made eye contact and realized how special it was that without saying a word everyone raced to the scene and worked together.""" , 
            'rating': 3}


"""
Download the chrome driver and make sure you have chromedriver executable in your PATH variable. 
To download the ChromeDriver to your system navigate to its download page. 
https://chromedriver.chromium.org/downloads  
"""
@pytest.fixture
def browser():
    CHROME_PATH = "c:\\Webdriver"
    print(CHROME_PATH)
    opts = Options()
    opts.headless = False
    driver = webdriver.Chrome(options=opts, executable_path = CHROME_PATH + '\chromedriver.exe')
    driver.implicitly_wait(10)
    
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_register_form(browser,user2):
    # test_user_1 = {'username':'ay1', 'email':'arslanay@wsu.edu', 'password':'strongpassword'}

    browser.get('http://localhost:5000/register')
    # Enable this to maximize the window
    # browser.maximize_window()
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(2)
    browser.find_element_by_name("email").send_keys(user2['email'])
    sleep(2)
    browser.find_element_by_name("password").send_keys(user2['password'])
    sleep(2)
    browser.find_element_by_name("password2").send_keys(user2['password'])    
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    # print(content)
    assert 'Congratulations, you are now a registered user!' in content

def test_register_error(browser,user2):
    browser.get('http://localhost:5000/register')
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(2)
    browser.find_element_by_name("email").send_keys(user2['email'])
    sleep(2)
    browser.find_element_by_name("password").send_keys(user2['password'])
    sleep(2)
    browser.find_element_by_name("password2").send_keys(user2['password'])    
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    assert 'Register' in content
    assert '[Please use a different username.]' in content

def test_login_form(browser,user2):
    browser.get('http://localhost:5000/login')
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(2)
    browser.find_element_by_name("password").send_keys(user2['password'])
    sleep(2)
    browser.find_element_by_name("remember_me").click()
    sleep(2)
    button = browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    assert 'Movie Ratings' in content
    assert user2['username'] in content

def test_invalidlogin(browser,user2):
    browser.get('http://localhost:5000/login')
    browser.find_element_by_name("username").send_keys(user2['username'])
    sleep(2)
    browser.find_element_by_name("password").send_keys('wrongpassword')
    sleep(2)
    browser.find_element_by_name("remember_me").click()
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    assert 'Invalid username or password' in content
    assert 'Sign In' in content

def test_post_review(browser,user2,post1):
    #first login
    browser.get('http://localhost:5000/login')
    browser.find_element_by_name("username").send_keys(user2['username'])
    browser.find_element_by_name("password").send_keys(user2['password'])
    browser.find_element_by_name("remember_me").click()
    browser.find_element_by_name("submit").click()

    browser.get('http://localhost:5000/postReview')
    browser.find_element_by_name("title").send_keys(post1['title'])
    sleep(2)
    browser.find_element_by_name("review").send_keys(post1['review'])
    sleep(2)
    Select(browser.find_element_by_name("rating")).select_by_visible_text(post1['rating'])
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    assert post1['title'] in content
    assert post1['review'] in content

def post_review2(browser,user2,post2):
    #first login
    browser.get('http://localhost:5000/login')
    browser.find_element_by_name("username").send_keys(user2['username'])
    browser.find_element_by_name("password").send_keys(user2['password'])
    browser.find_element_by_name("remember_me").click()
    browser.find_element_by_name("submit").click()

    browser.get('http://localhost:5000/postReview')
    browser.find_element_by_name("title").send_keys(post2['title'])
    sleep(2)
    browser.find_element_by_name("review").send_keys(post2['review'])
    sleep(2)
    Select(browser.find_element_by_name("rating")).select_by_visible_text(post2['rating'])
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(5)
    #verification
    content = browser.page_source
    assert post2['title'] in content
    assert post2['body'] in content

def test_post_review_error(browser,user2,post3):
    #first login
    browser.get('http://localhost:5000/login')
    browser.find_element_by_name("username").send_keys(user2['username'])
    browser.find_element_by_name("password").send_keys(user2['password'])
    browser.find_element_by_name("remember_me").click()
    browser.find_element_by_name("submit").click()

    browser.get('http://localhost:5000/postReview')
    browser.find_element_by_name("title").send_keys(post3['title'])
    sleep(2)
    browser.find_element_by_name("review").send_keys(post3['review'])
    sleep(2)
    Select(browser.find_element_by_name("rating")).select_by_visible_text(post3['rating'])
    sleep(2)
    browser.find_element_by_name("submit").click()
    sleep(10)
    #verification
    content = browser.page_source
    assert "[Field must be between 1 and 1500 characters long.]" in content


if __name__ == "__main__":
    retcode = pytest.main()