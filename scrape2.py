from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from faculty_list import DepartmentFacultyLink, read_json
from faculty_link import FacultyLink, write_json

faculty_links: list[FacultyLink] = []

links: list[DepartmentFacultyLink] = read_json()

browser = webdriver.Firefox()

for link in links:
    browser.get(link.faculty_link)
    faculties = browser.find_elements(By.XPATH, "//tr//td[1]//a")
    for faculty in faculties:
        faculty_page = faculty.get_attribute("href")
        faculty_links.append(FacultyLink(link.name, faculty_page))

browser.quit()

write_json(faculty_links)
