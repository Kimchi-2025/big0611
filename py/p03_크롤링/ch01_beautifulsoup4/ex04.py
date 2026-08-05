from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = 'https://ai-dev.tistory.com/1'
# html = urlopen(url)
# print(html)
# print(html.read())

# 제목과 본문 정보 웹 크롤링
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# title = soup.find_all('h1')
# print(title)
# print(len(title))



url = 'https://ai-dev.tistory.com/2'
html = urlopen(url)

# 제목과 본문 정보 웹 크롤링
soup = BeautifulSoup(html, 'html.parser')

# 방법1: <table> 태그 이용
table_tag = soup.find_all('table')
print(table_tag)
print(len(table_tag))
print(table_tag[0].text)
print('-----------------------------------------')

table_tag01 = table_tag[0].find_all('td')
print(table_tag01)


