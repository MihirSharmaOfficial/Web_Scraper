import requests
from bs4 import BeautifulSoup
import pandas as pd
def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    url = f'https://in.indeed.com/jobs?q=data+analyst&l=india&jt=internship&start={page}'
    r= requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job_seen_beacon')
    for item in divs:
        title = item.find('h2').text.strip()
        companyName = item.find('span' , class_='companyName').text.strip()
        try:
            salary = item.find('div', class_='salary-snippet').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class':'job-snippet'}).text.strip().replace('\n', '')

        job = {
            'title' : title,
            'companyName' : companyName,
            'salary' : salary,
            'summary' : summary
            }
        joblist.append(job)
    return
     
     
joblist = []

for i in  range(0,20,5):
    print(f'Getting page, {i}')
    c= extract(0)
    transform (c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')






