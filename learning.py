# import time
#
import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as exc
from selenium.webdriver import ActionChains

driver = wd.Chrome(
    executable_path="C:\\Users\\KalkiAvatharam\\PycharmProjects\\Selenium_Learning\\chromedriver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # ************* Use of CSS Selector for the Program
# # driver.find_element(By.CSS_SELECTOR, "input[value = 'radio1']").click()
# # assert "Radio1" in driver.page_source
# # *************** Use of the xpath for Attribute and Value
# # driver.find_element(By.XPATH, "//input[@value ='radio1']").click()
# # *************** Use of Xpath to get the text available
# # print(driver.find_element(By.XPATH, "//legend[text() ='Checkbox Example']").text)
# # *************** Use of Xpath for Parent to Child Relationship events
# # driver.find_element(By.XPATH, "//label[@for='bmw']/input").click()
# # *************** Use of Xpath for the parent to last child
# # driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']/option[last()]").send_keys()
# # ************* Use of the Xpath for the Grand Parent to Child
# # print(driver.find_element(By.XPATH, "//table [@name ='courses']/tbody/tr/th").text)
# # ************ Use of the Xpath for Child to any ancestor
# # driver.find_elements(By.XPATH, '// table [@id = "product"] /ancestor :: div [@class ="left-align"]')
# # ************ Use of Xpath for the Starts With options
# # driver.find_element(By.XPATH, "//input [starts-with(@placeholder,'Type to')]")
# # ************ Use of Xpath for the contains options
# # print(driver.find_element(By.XPATH, "//*[contains(@placeholder,'Type to')]").text)
# # ************ Use of Xpath to find out the Start with and Contains Option
# # driver.find_element(By.XPATH, "//input [starts-with(@placeholder,'Type to') and contains(@type,'tex')]")
# # ************ Use of multiselect option by creating unique path and then reviewing it
# # checkboxes = driver.find_elements(By.XPATH, '//Input[@type = "checkbox"]')
# # for checkbox in checkboxes:
# #     checkbox.click()
# # ********** Use of the Select Option to select value on a dropdown
# # static_dropdown = Select(driver.find_element(By.XPATH, '//select[(@id="dropdown-class-example")]'))
# # static_dropdown.select_by_visible_text("Option1")
# # time.sleep(2)
# # static_dropdown.select_by_index(3) ## Python starts counting from zero
# # time.sleep(2)
# # static_dropdown.select_by_value("option2")
# # time.sleep(5)
# # *********** Use of the dynamic drop down option
# # driver.find_element(By.XPATH, '//input[(@id="autocomplete")]').send_keys("ja")
# # time.sleep(2)
# # elements = driver.find_elements(By.XPATH, '//li[(@class="ui-menu-item")]/div[@id="ui-id-9"]')
# # for element in elements:
# #     if element.text == "Japan":
# #         element.click()
# #         time.sleep(5)
# #     else:
# #         pass
# # ************* Use of the Alert pop up  message box for the application using the driver.switch to function
# # driver.find_element(By.XPATH, '//input[@id="name"]').send_keys("Sujoy Chand")
# # time.sleep(2)
# # driver.find_element(By.XPATH, '//input[@id="alertbtn"]').click()
# # time.sleep(2)
# # popup_text = driver.switch_to.alert.text
# # driver.switch_to.alert.accept()
# # ## Find some random text in the popover message
# # find_text = "Sujoy Chand"
# # if find_text in popup_text:
# #     print('Searched text is available')
# # else:
# #     print('searched text not available')
# # *********** Use uplaod file feature and then uplaod a file
# # driver.get('https://the-internet.herokuapp.com/')  # change URL to go to example of uplaod
# # driver.find_element(By.LINK_TEXT, "File Upload").click()
# # driver.find_element(By.TAG_NAME, 'input').send_keys('C:\\Users\\KalkiAvatharam\\Downloads\\Assignment 02 - Ch 1_441.pdf')
# # time.sleep(2)
# # driver.find_element(By.CLASS_NAME, "button").click()
# # time.sleep(2)
# # file_upload = driver.find_element(By.TAG_NAME, "h3").text
# # if file_upload == 'File Uploaded!':
# #     print("File Uploaded is a Success !! ")
# # else:
# #     print("File Upload is a Fail.. attempt again")
# # ******** Use of the implicit wait function in selenimum
# # driver.get("https://chercher.tech/practice/implicit-wait-example")
# # driver.implicitly_wait(30)  # needs to be called only once per session for the selenium run done
# # driver.find_element(By.XPATH, '//input[@type="checkbox"][2]').click()
# # driver.find_element(By.XPATH, '//input[@type="checkbox"][4]').click()
# # ************ Use of Explicit Wait Example in Selenimum
# Example =1
# driver.get("https://chercher.tech/practice/implicit-wait-example")
# wdw(driver, 1000).until(exc.element_to_be_clickable((By.XPATH, "//div[@id=\"q\"]/input[2]")))
# **********************************************
# Example =2
# driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
# driver.find_element(By.XPATH, '//button[@id="populate-text"]').click()
# wdw(driver, 100).until(
#     exc.text_to_be_present_in_element((By.XPATH, '//h2 [starts-with(@id,"h2") and contains(@class,"target-text")]'),
#                                       "Selenium Webdriver"),
#     )
# ****************How to Handle the Mouse Over Feature for the application
# action_operation = ActionChains(driver)
# action_operation.move_to_element(driver.find_element(By.XPATH, '//button[(@class="btn btn-primary") and ('
#                                                                '@id="mousehover")]')).perform()
# action_operation.move_to_element(driver.find_element(By.LINK_TEXT, 'Top')).click().perform()
# time.sleep(2)
#
# ************* How to handle double click and single click options for the Actions Class
# driver.get("https://the-internet.herokuapp.com/")
# driver.find_element(By.LINK_TEXT, "Context Menu").click()
# wdw(driver, 100).until(exc.text_to_be_present_in_element((By.LINK_TEXT, "Elemental Selenium"), 'Elemental Selenium'))
# action = ActionChains(driver)
# action.context_click(driver.find_element(By.XPATH, '//div[@id="hot-spot"]')).perform()
# time.sleep(2)
# driver.switch_to.alert.accept()
# ************ How to shift between the windows in selenimum
# driver.find_element(By.XPATH, '//button[@id ="openwindow"]').click()
# driver.switch_to.window(driver.window_handles[1])
# print(driver.window_handles[1])
# time.sleep(2)
# print(driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav navbar-right"]/li[5]/a').text)
# ************** How to switch between tabs and windows with the best practice available.
# driver.implicitly_wait(5)  # Wait needs to be added
# driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
# open_window = driver.window_handles[1]  # Update the window
# driver.find_element(By.XPATH, "//a[@class='btn-style class1 class2']").click()
# open_tab = driver.window_handles[2]  # Update the tab name
# driver.switch_to.window(open_tab)  # switch between the tab and windows
# print(driver.find_element(By.XPATH, '//ul[@class ="navigation clearfix" ]/li[2]/a').text)
driver.close()
