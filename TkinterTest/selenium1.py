from time import sleep
import subprocess
import sys
try:
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
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

try:
    number_episode = int(input("How many episode's link do you want to get ? "))
    first_url = input("Copy the URL corresponding to the first episode : ")

    assert first_url.find('https://voiranime.com/') != -1
except ValueError:
    print('Error: a number need to be enter')
    quit()
except AssertionError:
    print('Error: the url does not match with the site')
    quit()

url_list = []

# set the driver's options
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe', options=options)
driver.get(first_url)

try:
    # repeting for the number of episode desired
    for nbr_episode in range(number_episode):
        # set the host to Stream Stape
        reader = driver.find_element_by_xpath(
            "//select[@class='selectpicker host-select']/option[@value='LECTEUR Stape']")
        reader.click()

        # find the validate button and wait for the user to finish the recaptcha
        validate_btn = driver.find_element_by_xpath("//button[@class='btn']")
        WebDriverWait(driver, 180).until(ec.element_to_be_clickable((By.XPATH, "//button[@class='btn']")))
        validate_btn.click()

        # wait for the video frame to appear
        WebDriverWait(driver, 30).until(ec.visibility_of_element_located((
            By.XPATH, "//div[@class='chapter-video-frame']/p[1]/iframe[1]")))

        # get the url source of the video
        iframe_url = driver.find_element_by_xpath("//div[@class='chapter-video-frame']/p[1]/iframe[1]")
        video_url = iframe_url.get_attribute('src')
        url_list.append(video_url)
        print(f'{video_url}\n')

        # get the next button on a list
        btn_next = driver.find_elements_by_xpath("//*[@id='manga-reading-nav-head']/div/div[3]/div/div[2]/a")
        # click the button if it exists
        if len(btn_next) > 0 and btn_next[0].is_displayed():
            btn_next[0].click()
    
    # repetting for each url got in previous loop
    for element in range(len(url_list)):
        while True:
            try:
                path = input(r'Path and name of the file to download (ex: C:\user\Download\video.mp4) : ')
                break
            except FileNotFoundError:
                print('Error: given path does not exist, please try again\n')

        # adding a url piece to go to the download page
        download_url = 'https://9xbud.com/'+url_list[element]
        # go to the previouly got url
        driver.get(download_url)
        driver.implicitly_wait(5)
        # go to the file we need to download
        download_btn = driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/section[4]/div/div/section[2]/div[2]/div[3]/div[2]/a')
        download_btn.click()
        WebDriverWait(driver, 5)

        print(f'[Video number {element+1}] Download starting ...')
        driver.find_element_by_name('body').send_keys(Keys.SPACE)

    try:
            # get the content of the file on the current page
            r = requests.get(URL)
            # write the content got just before and write it in a file
            with open(path, 'wb') as f:
                f.write(r.content)
            print(r.headers['content-typre']+'\t'+r.encoding)
    except:
        print('Error: problem occurs during download, wait for the download to finish and check if it is readable or try again')
        
        print(f'[Video number {element+1}] Download finished')


except selenium.common.exceptions.WebDriverException:
    print('\nError: the URL is not correct or the tab has been closed\n')
# except:
#     print('Error: the tab has been closed or a problem occurs')

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
    subprocess.Popen(args=['python', 'selenium12.py'], stdout=sys.stdout)
