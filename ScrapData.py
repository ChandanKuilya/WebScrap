# import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
#from selenium import ChromeDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
import json

# URL = "https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1"
# page = requests.get(URL)

# soup = BeautifulSoup(page.content,"html.parser")

# print(soup.prettify())


options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = r"C:\Users\CHANDAN KUILYA\Downloads\chromedriver_win32.exe"
driver = webdriver.Chrome(chrome_driver_binary, options=options)
driver.get('https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1')

#driver = Chrome(executable_path=r'C:\Users\CHANDAN KUILYA\Downloads\chromedriver_win32.exe')
#driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chrome') 
#driver.get('https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1')

soup = BeautifulSoup(driver.page_source,'lxml')


#from selenium import webdriver
#import selenium.webdriver.chrome.service as service
#service = service.Service('C:\Users\CHANDAN KUILYA\Downloads\chromedriver_win32.exe')
#service.start()
#capabilities = {'chrome.binary': "C:\Program Files\Google\Chrome\Application\chrome.exe"}
#driver = webdriver.Remote(service.service_url, capabilities)
#driver.get('https://www.naukri.com/job-listings-data-scientist-business-analyst-science-data-analyst-megara-infotech-bhubaneswar-mumbai-hyderabad-secunderabad-gurgaon-gurugram-bangalore-bengaluru-delhi-ncr-0-to-1-years-310323003909?src=discovery_trendingWdgt_homepage_srch&sid=16802765936445865&xp=1&px=1')


job_title = soup.find('h1', attrs={'class': 'jd-header-title'}).text.strip()
company_name = soup.find('div', attrs={'class': 'jd-header-comp-name'}).text.strip()
location = soup.find('span', attrs={'class': 'location'}).text.strip()
experience = soup.find('div', attrs={'class': 'exp'}).text.strip()
skills = [tag.text.strip() for tag in soup.select('div.key-skill span')]
job_description = soup.find('div', attrs={'class': 'dang-inner-html'}).text.strip()
salary_range = soup.find('div', attrs={'class': 'salary'}).text.strip()
date_of_posting = soup.find('span', attrs={'class': 'stat'}).text.strip()
#job_type = soup.find('div', attrs={'class': 'details[3]'}).text.strip()
#job_type = [tag.text.strip() for tag in soup.select('div.details span.Employment Type')]
#job_type=soup.find('label', attrs={'tag': 'Employment Type'}).text.strip()
job_type = [tag.text.strip() for tag in soup.select('div.details span')]


#job_type = [tag.text.strip() for tag in soup.select('div.details Employment Type')]

job_data = {
    "job_title": job_title,
    "company_name": company_name,
    "location": location,
    "experience": experience,
    "skills": skills,
    "job_description": job_description,
    "salary_range": salary_range,
    "date_of_posting": date_of_posting,
    "job_type": job_type
}

json_data = json.dumps(job_data)

driver.quit()
print(json_data)


