from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time



if __name__ == '__main__':

    start =time.clock()

    path_to_chrome = '/Users/Owner/Desktop/chromedriver'
    browser = webdriver.Chrome(executable_path = path_to_chrome);

    url = 'http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=The+Ohio+State+University&schoolID=724&queryoption=TEACHER'
    browser.get(url)
    browser.maximize_window()

    browser.find_element_by_xpath('//*[@id="cookie_notice"]/a[1]').click()

    # click dropdown button
    browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/span').click()

    #1-152 department
    i = 2;
    browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[3]/div/div/ul/li[%s]' % i).click()

    # left side scroll down
    target = browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[5]/div/div[1]')
    browser.execute_script("arguments[0].scrollIntoView();", target)

    browser.find_element_by_xpath('//*[@id="spout-header-close"]').click()
    browser.find_element_by_xpath('//*[@id="mainContent"]/div[1]/div/div[5]/div/div[1]').click()

    text = browser.page_source
    soup = BeautifulSoup(text, 'html.parser')
    names = browser.find_elements_by_class_name("result-list")

    for name in names:
        print(name.text)


    end = time.clock()

    print('\n')
    print('Running time: %s Seconds'%(end-start))
