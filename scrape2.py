from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from faculty_list import DepartmentFacultyLink, read_json

links: list[DepartmentFacultyLink] = read_json()

browser = webdriver.Firefox()

for link in links:
    browser.get(link.faculty_link)
    faculties = browser.find_elements(By.XPATH, "//tr//td[1]//a")
    for faculty in faculties:
        print(faculty.get_attribute("href"))

    browser.quit()
    break
