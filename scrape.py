from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from dataclasses import dataclass
from faculty import DepartmentFacultyLink

browser = webdriver.Firefox()
browser.get('https://rvce.edu.in/rvce-departments')

links_div: WebElement = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[1]/article/div/div/div/div")
links: list[WebElement] = links_div.find_elements(by=By.XPATH, value=".//a")
faculty_links: list[DepartmentFacultyLink] = []
for link in links[:-1]:
    faculty_links.append(DepartmentFacultyLink(link.text, link.get_attribute('href')))

link_hrefs: list[str] = [link.get_attribute('href') for link in links]

browser.get(links[-1].get_attribute('href'))
links_article: list[WebElement] = browser.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[1]/article")
other_links: list[WebElement] = links_article.find_elements(by=By.XPATH, value=".//a")

for link in other_links:
    faculty_links.append(DepartmentFacultyLink(link.text, link.get_attribute('href')))

link_hrefs.pop()
link_hrefs.extend([link.get_attribute('href') for link in other_links])

for link_href in link_hrefs:
    print(link_href)

    browser.execute_script("window.open('" + link_href + "', '_blank');")
    
    browser.switch_to.window(browser.window_handles[-1])

    browser.implicitly_wait(2)
    
    faculty_link: WebElement = browser.find_element(by=By.XPATH, value="//a[text()='Faculty'] | //a//*[text()='Faculty']/parent::a | //a[text()='Faculty Members']")
    print(faculty_link.get_attribute('href'))

    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    print()

    
browser.quit()
