import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'

for page in range(1,5) :
    params = {'pg': page}
    data = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.check > input
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.page-nav.rank-page-nav
    trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# 아래 빈 칸('')을 채워보세요
    for tr in trs:
        rank = tr.select_one('td.number').contents[0].strip()
        title = tr.select_one('td > a.title.ellipsis').text.strip()
        artist = tr.select_one('td > a.artist.ellipsis').text
        print(rank, title, artist)
