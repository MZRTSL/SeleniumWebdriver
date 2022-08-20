# Example 0:
# open a new Firefox browser
# load the page at the given URL

"""we have already installed selenium package
webdriver is a component of selenium which we already know that
webdriver the editor i want to write my webdriver program for which i need to use this command
in order to use those commands we need to specify to out editor that use this webdriver from the selenium package
whatever we have install for this reason we are using FROM
"""

# from selenium import webdriver
"""we specifying that in this class we can create a program for webdriver
as we have successfully imported it """

from selenium import webdriver
browser=webdriver.Firefox(executable_path='drivers/geckodriver')
browser.get("http://bing.com/")

"""for chromedriver nee chromedriver
for firefox need geckodriver.exe"""