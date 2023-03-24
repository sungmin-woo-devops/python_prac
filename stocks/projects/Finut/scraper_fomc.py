import os
import requests
from bs4 import BeautifulSoup

months = {"01": 'January', "02": 'February', "03": 'March', "04": 'April', 
          "05": 'May', "06": 'June', "07": 'July', "08": 'August', "09": 'September', 
          "10": 'October', "11": 'November', "12": 'December'}

# 웹 페이지 URL
url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'

# requests를 사용하여 HTML 소스코드 가져오기
html = requests.get(url).content

# BeautifulSoup을 사용하여 HTML 소스코드 파싱
soup = BeautifulSoup(html, 'html.parser')

# <div class="panel panel-default"> 태그 추출
panel_tags = soup.find_all('div', {'class': 'panel panel-default'})
fomc_meeting = soup.find_all('div', {'class': 'fomc-meeting'})
# <div class="panel panel-default"> 태그 내부 자식 태그 추출

current_path = os.getcwd() 
# print(current_path) # F:\Python

panel_headings = []
panel_rows = []

# print(panel_tags)

# 항상 최신 일정이 맨 앞에 오도록 정렬(reverse)
data = []
temp_year = []
temp_month = []
temp_date = []

# print(panel_tags[0])
print(panel_tags[0].find('a').text.split(" ")[0])
print(len(panel_tags))

# year 추출
for i in range(len(panel_tags)):
    temp_year.append(panel_tags[i].find('a').text.split(" ")[0])
print(temp_year)

# month 추출
month_date = []
for tag in fomc_meeting:
    # FOMC month 처리 부분
    month_child = tag.find("div", class_="fomc-meeting__month")
    month_temp = month_child.text.split()[0]

    for key, value in months.items():
        if month_temp == value or month_temp[0:3] == value[0:3]:
            month_temp = key
            break

    # FOMC day 처리 부분
    day_child = tag.find("div", class_="fomc-meeting__date")
    day_temp = day_child.text.split()[0]
    
    temp = day_temp.split("-")[0]
    if len(temp) == 1:
        temp = "0" + temp
    else:
        temp = temp[0:2]
    
    day_temp = temp

    month_date.append([month_temp, day_temp])
print(month_date)

def count_meetings(month_date):
    yearly_meetings = []
    cnt = 0
    for i in range(0,len(month_date)):
        if int(month_date[i][0]) < 12:
            cnt += 1
        elif int(month_date[i][0]) == 12:
            cnt += 1
            yearly_meetings.append(cnt)
            cnt = 0
    return yearly_meetings

meeting_counts = count_meetings(month_date)

for i in range(len(meeting_counts)):
    for j in range(0, meeting_counts[i]):
        temp_date.append((temp_year[i], month_date[j][0], month_date[j][1]))

for i in range(len(temp_date)):
    print(temp_date[i])
