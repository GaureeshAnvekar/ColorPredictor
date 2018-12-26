
"""
Created on Mon Dec  3 23:32:59 2018

@author: root

"""
import random
from selenium import webdriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('/root/firefox/firefox')
#browser = webdriver.Firefox(firefox_binary=binary)
browser = webdriver.Firefox()
#csv_file_train = open("color-data-train.csv", "w+")
url = "https://contrast-ratio.com/#"
url_last_part = ""
string_for_train = ""
cant_see_count_black = 0
cant_see_count_white = 0
can_see_count_black = 0
can_see_count_white = 0


"""
#"Can't see" set when black text on black. "0" indicates "Can't see" for both black or white text
browser.get("https://contrast-ratio.com/#black-on-black")
url_last_part = ""
for red_pixel in range(257):
    for green_pixel in range(257):
        for blue_pixel in range(257):
            url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

            browser.get(url + "black-on-" + url_last_part)
            web_elem_threshold = browser.find_element_by_css_selector("output strong")
            curr_threshold_val = float(web_elem_threshold.text)

            if(curr_threshold_val <= 1.03):
                string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(0) + "," + str(0)
                csv_file_train.write(string_for_train + "\n")
                cant_see_count_black = cant_see_count_black + 1
                url_last_part = ""
                string_for_train = ""
            else:
                url_last_part = ""
                string_for_train = ""
                break

print(cant_see_count_black)


#"Can't see" set when white text on white. "0" indicates "Can't see" for both white or black text
#csv_file_train = open("color_data_train.csv", "a+")
browser.get("https://contrast-ratio.com/#white-on-white")
url_last_part = ""
for red_pixel in range(256, -1, -1):
    for green_pixel in range(256,-1, -1):
        for blue_pixel in range(256, -1, -1):
            url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

            browser.get(url + "white-on-" + url_last_part)
            web_elem_threshold = browser.find_element_by_css_selector("output strong")
            curr_threshold_val = float(web_elem_threshold.text)

            if(curr_threshold_val <= 1.06): #1.06 threshold when text is white
                string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(1) + "," + str(0)
                csv_file_train.write(string_for_train + "\n")
                cant_see_count_white = cant_see_count_white + 1
                url_last_part = ""
                string_for_train = ""
            else:
                url_last_part = ""
                string_for_train = ""
                break

print(cant_see_count_white)

csv_file_train.close()


total_cant_see = 3495 + 15298 # black + white count
total_half = total_cant_see / 2

#"Can see" set when text is black. "1" in last column indicates "Can see"
#csv_file_train = open("color-data-train.csv", "a+")
csv_file_test = open("color-test-data.csv", "a+")
while(True):
    red_pixel = random.randint(0,256)
    green_pixel = random.randint(0,256)
    blue_pixel = random.randint(0,256)
    
    url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

    browser.get(url + "black-on-" + url_last_part)
    web_elem_threshold = browser.find_element_by_css_selector("output strong")
    curr_threshold_val = float(web_elem_threshold.text)

    if(curr_threshold_val > 1.03):
        string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(0) + "," + str(1)
        csv_file_test.write(string_for_train + "\n")
        can_see_count_black = can_see_count_black + 1
        
    url_last_part = ""
    string_for_train = ""
    
    if(can_see_count_black >= total_half):
        break
    
#"Can see" set when text is white. "1" in last column indicates "Can See"
while(True):
    red_pixel = random.randint(0,256)
    green_pixel = random.randint(0,256)
    blue_pixel = random.randint(0,256)
    
    url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

    browser.get(url + "white-on-" + url_last_part)
    web_elem_threshold = browser.find_element_by_css_selector("output strong")
    curr_threshold_val = float(web_elem_threshold.text)

    if(curr_threshold_val > 1.06):
        string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(1) + "," + str(1)
        csv_file_test.write(string_for_train + "\n")
        can_see_count_white = can_see_count_white + 1

    url_last_part = ""
    string_for_train = ""
    
    if(can_see_count_white >= total_half):
        break
    
csv_file_test.close()
"""


#DEV-SET
#"Can see" set when text is black. "1" in last column indicates "Can see"
#csv_file_train = open("color-data-train.csv", "a+")
csv_file_dev = open("color-dev-data.csv", "a+")
while(True):
    red_pixel = random.randint(0,256)
    green_pixel = random.randint(0,256)
    blue_pixel = random.randint(0,256)
    
    url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

    browser.get(url + "black-on-" + url_last_part)
    web_elem_threshold = browser.find_element_by_css_selector("output strong")
    curr_threshold_val = float(web_elem_threshold.text)

    if(curr_threshold_val > 1.03):
        string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(0) + "," + str(1)
        csv_file_dev.write(string_for_train + "\n")
        can_see_count_black = can_see_count_black + 1
        
    url_last_part = ""
    string_for_train = ""
    
    if(can_see_count_black >= 20000):
        break
    
#"Can see" set when text is white. "1" in last column indicates "Can See"
while(True):
    red_pixel = random.randint(0,256)
    green_pixel = random.randint(0,256)
    blue_pixel = random.randint(0,256)
    
    url_last_part = url_last_part + "rgb%28" + str(red_pixel) + "%2C" + str(green_pixel) + "%2C" + str(blue_pixel) + "%29"

    browser.get(url + "white-on-" + url_last_part)
    web_elem_threshold = browser.find_element_by_css_selector("output strong")
    curr_threshold_val = float(web_elem_threshold.text)

    if(curr_threshold_val > 1.06):
        string_for_train = string_for_train + str(red_pixel) + "," + str(green_pixel) + "," + str(blue_pixel) + "," + str(1) + "," + str(1)
        csv_file_dev.write(string_for_train + "\n")
        can_see_count_white = can_see_count_white + 1

    url_last_part = ""
    string_for_train = ""
    
    if(can_see_count_white >= 20000):
        break
    
csv_file_dev.close()

