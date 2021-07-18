import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.title)
# print(soup.title.get_text())
print(soup.a)
print(soup.a.attrs)
url2=soup.a.attrs['href']
res=requests.get(url2)
soup.a['href']

print(soup.find('a',{'class':'Nbtn_upload'}))
soup.find('a',{'class':'Nbtn_upload'}).text # class = "Nbtn_upload"인 a element를 찾아줘

soup.find(attrs={'class':'Nbtn_upload'})  # class = "Nbtn_upload"인 어떤 element를 찾아줘

rank1 = soup.find('li',{'class':'rank01'})

rank1.a['title'] # a : 꺽쇠, title : 딕셔너리

print(rank1.a.get_text())
# 싸움독학-88화 : 형은 이제 ㅈ됐어~
rank1.a['title'] # '싸움독학-88화 : 형은 이제 ㅈ됐어~'
rank2 = rank1.next_sibling.next_sibling
rank2.a.get_text()

for i in range(10):
    print(rank1.a.get_text())
    rank1 = rank1.next_sibling.next_sibling