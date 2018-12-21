
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

"""
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

#Use each color i.e red(0), green(1), blue(2). For each color traverse all it's 256 values.
#Then for each value between 0 to 256, randomly select value between 0 and 256 for other colors as well.
#But we do that only 120 times.
#For example when color = 0 ie red, traverse through all it's 256 values. For each value, then select 
#randomly the pixel value for green and blue also between 0 and 256. Do this only for 120 times for each value of red.
#Similarly repeat for blue ie color = 1. 
#So in total our train and test set will have 256 * 120 * 3 rows
for color in range(3):
    for pixel_1_val in range(257):
        pixels_used_train = {}
        for count in range(30):
            condition = True
            string_for_train = ""
            url_last_part = ""
            while(condition):  #This is to make sure to avoid same pixel values
                pixel_2_train = random.randint(0,256)
                pixel_3_train = random.randint(0,256)
                if(not(pixel_2_train in pixels_used_train) or not(pixel_3_train in pixels_used_train)): #This check if atleast one pixel value is different. If yes come out of while loop
                    condition = False
                    pixels_used_train[pixel_2_train] = True
                    pixels_used_train[pixel_3_train] = True
                    
            if(color == 0): # red color
                string_for_train = string_for_train + str(pixel_1_val) + "," + str(pixel_2_train) + "," + str(pixel_3_train) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_1_val) + "%2C" + str(pixel_2_train) + "%2C" + str(pixel_3_train) + "%29"
            elif(color == 1): # green color
                string_for_train = string_for_train + str(pixel_2_train) + "," + str(pixel_1_val) + "," + str(pixel_3_train) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_2_train) + "%2C" + str(pixel_1_val) + "%2C" + str(pixel_3_train) + "%29"
            else: # blue color
                string_for_train = string_for_train + str(pixel_2_train) + "," + str(pixel_3_train) + "," + str(pixel_1_val) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_2_train) + "%2C" + str(pixel_3_train) + "%2C" + str(pixel_1_val) + "%29"    

            if(text_white_train == True):
                url_last_part = "white-on-" + url_last_part
            else: # text color is black
                url_last_part = "black-on-" + url_last_part


            #Now go to the specific url with above background color ie pixel 1,2,3 values and the text color ie black or white
            browser.get(url + url_last_part)
            web_elem_threshold = browser.find_element_by_css_selector("output strong")
            curr_threshold_val = float(web_elem_threshold.text)
            
            if(curr_threshold_val > threshold_train): # all is good ie our current text color is visible for above background ie pixel 1,2,3 combinations
                if(text_white_train == True):
                    right_text_color = 1  # 1 is white
                    count_white_train = count_white_train + 1
                else: #text is black
                    right_text_color = 0  # 0 is black
                    count_black_train = count_black_train + 1
                    
                string_for_train = string_for_train + str(right_text_color) + "\n"
                
            else: # threshold <= curr_threshold ie our current text color is not visible for above background
                print("threshold break white")
                if(text_white_train == True):
                    right_text_color = 0  # ie select opposite, white text was not visible so make it black ie 0
                    count_black_train = count_black_train + 1
                    text_white_train = False #change our current text color to black
                    threshold_train = 1      # change the threshold according to black
                else: # black text
                    right_text_color = 1 # black text not visible so right choice is white ie 1
                    count_white_train = count_white_train + 1
                    text_white_train = True  # change our current text color to white
                    threshold_train = 1.03   # threshold for white is 1.03
                
                string_for_train = string_for_train + str(right_text_color) + "\n"
                
            #Now add the string_for_train to csv_file_train.
            #string_for_train will be like 120,20,50,0  ie red,green,blue,right_text_color can be 0 or 1
            csv_file_train.write(string_for_train)
            
#Repeat the same for loop but this time start with black text white background
text_white_train = False
threshold_train = 1
browser.get("https://contrast-ratio.com/#black-on-white")
            
for color in range(3):
    for pixel_1_val in range(257):
        pixels_used_train = {}
        for count in range(30):
            condition = True
            string_for_train = ""
            url_last_part = ""
            while(condition):  #This is to make sure to avoid same pixel values
                pixel_2_train = random.randint(0,256)
                pixel_3_train = random.randint(0,256)
                if(not(pixel_2_train in pixels_used_train) or not(pixel_3_train in pixels_used_train)): #This check if atleast one pixel value is different. If yes come out of while loop
                    condition = False
                    pixels_used_train[pixel_2_train] = True
                    pixels_used_train[pixel_3_train] = True
                    
            if(color == 0): # red color
                string_for_train = string_for_train + str(pixel_1_val) + "," + str(pixel_2_train) + "," + str(pixel_3_train) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_1_val) + "%2C" + str(pixel_2_train) + "%2C" + str(pixel_3_train) + "%29"
            elif(color == 1): # green color
                string_for_train = string_for_train + str(pixel_2_train) + "," + str(pixel_1_val) + "," + str(pixel_3_train) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_2_train) + "%2C" + str(pixel_1_val) + "%2C" + str(pixel_3_train) + "%29"
            else: # blue color
                string_for_train = string_for_train + str(pixel_2_train) + "," + str(pixel_3_train) + "," + str(pixel_1_val) + ","
                url_last_part = url_last_part + "rgb%28" + str(pixel_2_train) + "%2C" + str(pixel_3_train) + "%2C" + str(pixel_1_val) + "%29"    

            if(text_white_train == True):
                url_last_part = "white-on-" + url_last_part
            else: # text color is black
                url_last_part = "black-on-" + url_last_part


            #Now go to the specific url with above background color ie pixel 1,2,3 values and the text color ie black or white
            browser.get(url + url_last_part)
            web_elem_threshold = browser.find_element_by_css_selector("output strong")
            curr_threshold_val = float(web_elem_threshold.text)
            
            if(curr_threshold_val > threshold_train): # all is good ie our current text color is visible for above background ie pixel 1,2,3 combinations
                if(text_white_train == True):
                    right_text_color = 1  # 1 is white
                    count_white_train = count_white_train + 1
                else: #text is black
                    right_text_color = 0  # 0 is black
                    count_black_train = count_black_train + 1
                    
                string_for_train = string_for_train + str(right_text_color) + "\n"
                
            else: # threshold <= curr_threshold ie our current text color is not visible for above background
                print("threshold break black")
                if(text_white_train == True):
                    right_text_color = 0  # ie select opposite, white text was not visible so make it black ie 0
                    count_black_train = count_black_train + 1
                    text_white_train = False #change our current text color to black
                    threshold_train = 1      # change the threshold according to black
                else: # black text
                    right_text_color = 1 # black text not visible so right choice is white ie 1
                    count_white_train = count_white_train + 1
                    text_white_train = True  # change our current text color to white
                    threshold_train = 1.03   # threshold for white is 1.03
                
                string_for_train = string_for_train + str(right_text_color) + "\n"
                
            #Now add the string_for_train to csv_file_train.
            #string_for_train will be like 120,20,50,0  ie red,green,blue,right_text_color can be 0 or 1
            csv_file_train.write(string_for_train)
            
print("white_count train " + str(count_white_train))
print("black count train " + str(count_black_train))


"""

