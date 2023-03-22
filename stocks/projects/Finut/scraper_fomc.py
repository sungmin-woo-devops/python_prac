import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'

# requests를 사용하여 HTML 소스코드 가져오기
html = requests.get(url).content

# BeautifulSoup을 사용하여 HTML 소스코드 파싱
soup = BeautifulSoup(html, 'html.parser')

# <div class="panel panel-default"> 태그 추출
panel_tags = soup.find_all('div', {'class': 'panel panel-default'})

# <div class="panel panel-default"> 태그 내부 자식 태그 추출

with open('./projects/Finut/fomc_raw.html', "w") as file:
    file.write(str(panel_tags))

year_temp = []
month_temp = []
date_temp = []

for panel_tag in panel_tags:
    panel_headings = panel_tag.find_all('div', {'class': 'panel-heading'})
    panel_rows = panel_tag.find_all('div', {'class': 'row fomc-meeting'})

for panel_heading in panel_headings:
    panel_title = panel_heading.find('h4', {'class': 'panel-title'})
    year_temp.append(panel_title.text)

for panel_row in panel_rows:
    month_child_tags = panel_row.find_all('div', {'class': 'fomc-meeting__month'})
    date_child_tags = panel_row.find_all('div', {'class': 'fomc-meeting__date'})

    
print()