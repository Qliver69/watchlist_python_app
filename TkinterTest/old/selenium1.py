from time import sleep
import subprocess
import sys
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
except ModuleNotFoundError:
    print('Error: Selenium is not install on this machine')
    quit()

# I would like to introduce a new feature where user can search an anime directly from the website and download it
# without passed by a browser to copy the first link

print("\nHi ! I'm a script which permits you to download easily from voiranime.com\n"
      "Sorry for those who aren't french but it's the first version of me ...\n"
      "Oh ! And I warn you : the Captcha check are very long .....\n"
      "(One last things, it works only on Chrome)\n Good using ! ;)\n\n")

number_episode = int(input("How many episode's link do you want to get ? "))
first_url = input("Copy the URL corresponding to the first episode : ")

url_list = []

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe', options=options)
driver.get(first_url)

try:
    for nbr_episode in range(number_episode):
        reader = driver.find_element_by_xpath(
            "//select[@class='selectpicker host-select']/option[@value='LECTEUR Stape']")
        reader.click()

        validate_btn = driver.find_element_by_xpath("//button[@class='btn']")
        WebDriverWait(driver, 180).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='btn']")))
        validate_btn.click()

        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((
            By.XPATH, "//div[@class='chapter-video-frame']/p[1]/iframe[1]")))

        iframe_url = driver.find_element_by_xpath("//div[@class='chapter-video-frame']/p[1]/iframe[1]")
        video_url = iframe_url.get_attribute('src')
        url_list.append(video_url)
        print(video_url)

        btn_next = driver.find_elements_by_xpath("//*[@id='manga-reading-nav-head']/div/div[3]/div/div[2]/a")

        if len(btn_next) > 0 and btn_next[0].is_displayed():
            btn_next.click()
    for element in range(len(url_list)):
        download_url = 'https://9xbud.com/'+url_list[element]
        print(download_url)

        driver.get(download_url)
        driver.implicitly_wait(20)
        download_btn = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/section[4]/div/div/section[2]/div[2]/div[3]/div[2]/a')
        download_btn.click()
        sleep(10)
except selenium.common.exceptions.WebDriverException:
    print('\nError: the chrome tab has been closed\n')

while True:
    try:
        retry = input('Do you want to retry ? (y/n)  ').upper()

        for i in range(10):
            if retry == str(i):
                raise TypeError

        if len(retry) != 1:
            raise ValueError

        assert retry == 'Y' or retry == 'N'

        break
    except ValueError:
        print('Error: more than one character')
    except TypeError:
        print('Error: number instead of letter')
    except AssertionError:
        print('Error: the character is not y or n')

if retry == 'Y':
    subprocess.Popen(args=['python', 'selenium1.py'], stdout=sys.stdout)