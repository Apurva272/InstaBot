from selenium import webdriver
from time import sleep
class InstaBot:
    def __init__(self,username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get('https://instagram.com')
        sleep(2)
        
        
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        

        sleep(4)

        
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')] ").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')] ").click()
        
    def get_unfollowers (self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a'.format(self.username)).click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers ]
        print(not_following_back)
        sleep(2)
    def _get_names(self): 
        sleep(2)   
    
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0,1
        while last_ht!= ht:
            last_ht = ht
        
            sleep(1)
            ht = self.driver.execute_script(""" 
                 arguments[0].scrollTo(0,arguments[0].scrollHeight);
                 return arguments[0].scrollHeight;
                 """,scroll_box)
            links = scroll_box.find_element_by_tag_name('a')

            names = [name.text for name in links if name.text!='']
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
            return names 
my_bot = InstaBot('yourusername','yourpassword') 
my_bot.get_unfollowers()

     






