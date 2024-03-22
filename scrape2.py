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
    faculties = browser.find_elements(By.XPATH, "//tr//td[1]//a | //tr//td[2]//a")
    for faculty in faculties:
        faculty_page = faculty.get_attribute("href")
        faculty_links.append(FacultyLink(link.name, faculty_page))
        
browser.quit()

seen_links = set()
unique_faculty_links = []
for link in faculty_links:
    if link.link not in seen_links:
        unique_faculty_links.append(link)
        seen_links.add(link.link)

write_json(unique_faculty_links)
