from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from faculty_link import FacultyLink, read_json
from faculty_profile import FacultyProfile, write_json, write_org_mode, write_csv

links: list[FacultyLink] = read_json()
browser = webdriver.Firefox()

profiles: list[FacultyProfile] = []

for link in links:
    actual_link = link.link
    print(actual_link)
    browser.get(actual_link)

    department = link.department
    name = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/h1").text
    designation = ""
    teaching_exp = 0
    research_exp = 0
    industry_exp = 0
    date_of_joining = ""
    email = ""

    profile = FacultyProfile(department, name, designation, teaching_exp, research_exp, industry_exp, date_of_joining, email, actual_link)
    profiles.append(profile)    

browser.quit()
write_org_mode(profiles)
write_csv(profiles)
