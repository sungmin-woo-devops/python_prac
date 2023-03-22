import requests
from bs4 import BeautifulSoup

months = {"01": 'January', "02": 'February', "03": 'March', "04": 'April', 
          "05": 'May', "06": 'June', "07": 'July', "08": 'August', "09": 'September', 
          "10": 'October', "11": 'November', "12": 'December'}

# HTML 페이지의 URL
url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'

# requests를 사용하여 HTML 소스코드 가져오기
html = requests.get(url).content

# BeautifulSoup을 사용하여 HTML 소스코드 파싱
soup = BeautifulSoup(html, 'html.parser')

# 특정 태그, 속성 또는 id가 일치하는 모든 태그 가져오기
data_for_keys = soup.find_all('a')
fomc_meeting = soup.find_all('div', {'class': 'fomc-meeting'})
# data = soup.find_all(['x', {'y': 'value'}, {'id': 'z'}])
# <a id="36495">2023 FOMC Meetings</a>

# with open("./projects/Finut/fomc_meeting.txt", "w") as file:
#     for value in data_for_values:
#         file.write(value.text + "\n")

# [month, day] 리스트를 저장하는 방법 - 나중에 튜플로 변경
date = []
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

    date.append([month_temp, day_temp])
print(date)

keys = []
dates = []

# 각 태그에서 데이터 추출하기
# for tag in data_for_keys:
#     if tag.text[5:9] == "FOMC":
#         keys.append(tag.text)

# for tag in data_for_values:
#     if tag.text[0:2] == "20":
#         dates.append(tag.text)

# print(keys)
# print(dates)

# 연도별 a 태그에서 "2023 FOMC Meetings" 추출
# 이후 해당 연도의 모든 회의 일정을 딕셔러니 형태로 추출
# 연도별 이름과 일정 딕셔러니를 매핑시켜 JSON 형태로 저장

# 어짜피 월별로 나눠져 있으니까 12개씩 나눠서 연도별로 저장하면 될 듯