from selenium import webdriver
import time
import requests
from hashlib import md5
import re
import base64
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):

        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):

        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


class Login:
    def __init__(self, url, username, passwd):
        self.url = url
        self.username = username
        self.passwd = passwd

    def login(self):

        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        time.sleep(2)
        login_select = self.browser.find_element_by_class_name('login-hd-account')
        login_select.click()
        user = self.browser.find_element_by_id('J-userName')
        word = self.browser.find_element_by_id('J-password')
        user.send_keys(self.username)

        word.send_keys(self.passwd)

    def get_pic(self):
        tag = self.browser.find_element_by_class_name('imgCode')
        temp = tag.get_attribute('src')
        b64_pic = re.sub(r'data:image/jpg;base64,', '', temp)
        pic = base64.b64decode(b64_pic)
        return pic

    def click(self, j):
        temp = j.get('pic_str')
        locations = [list(map(int, i.split(','))) for i in temp.split('|')]    # [[11, 22], [33, 44]]
        for location in locations:
            ActionChains(self.browser).move_to_element_with_offset(self.browser.find_element_by_class_name('imgCode'),
                                                                   location[0], location[1]).click().perform()
            time.sleep(2)
        time.sleep(2)
        self.browser.find_element_by_id('J-login').click()

    def get_cookies(self):
        return self.browser.get_cookies()


if __name__ == '__main__':
    a = Login('https://kyfw.12306.cn/otn/resources/login.html', '15382518632', 'motianya1996')
    a.login()
    time.sleep(2)
    chaojiying = Chaojiying_Client('motian', '19961201', '软件id')
    im = a.get_pic()
    z = chaojiying.PostPic(im, 9004)
    print(z)
    a.click(z)
    print('登录成功')

