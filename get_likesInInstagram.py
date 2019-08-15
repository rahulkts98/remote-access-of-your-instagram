from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(2)
        username = driver.find_element_by_name('username')
        username.clear()
        username.send_keys(self.username)
        password = driver.find_element_by_name('password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(10)
        for i in range(1,1):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(5)
    #searshing for picture link
        hrefs = driver.find_elements_by_tag_name('a')
        images_links = []
        for item in hrefs:
            href = item.get_attribute('href')
            if "/p/" not in href:
                continue
            print(str(len(href)))
            print(str(len(images_links)))
            images_links.append(href)

        for images_link in images_links:
            driver.get(images_link)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9").click()
            time.sleep(10)
            


    


rahul=InstagramBot("your instagram useername","your instagram password")
rahul.login()
rahul.like_photo("srilanka")
 