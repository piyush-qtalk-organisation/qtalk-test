# import time
# from selenium.webdriver.common.by import By
#
# from QuickTalk_Automation import funtion
#
# funtion.open_browser()
#
# def test_click_on_new_created_card():
#     card_elements = funtion.driver.find_elements(By.CLASS_NAME, "card-main ")
#     print(card_elements)
#     for card_elem in card_elements:
#         title_elem = card_elem.find_element(By.CLASS_NAME, "talk--title")
#         if title_elem.text == "Automate quickTalk Created":
#             print(title_elem.text)
#             funtion.driver.execute_script("arguments[0].scrollIntoView()",card_elem)
#             print(card_elem)
#             time.sleep(3)
#             card_elem.click()
#             time.sleep(10)