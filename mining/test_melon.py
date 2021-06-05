from bs4 import BeautifulSoup
import requests
import codecs

class Melon(object):

    url = 'https://www.melon.com/chart/index.htm?'
    headers = {'User-Agent':'Mozilla/5.0'} # 벅스와 달리 멜론에서 설정해야하는 헤더값
    music_list = []

    def set_url(self, detail):
        # detail 은 dayTime=2021060515 부분으로 바뀌는 값
        # headers는 멜론에서 스크래핑을 할 때 필요한 속성값
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        titleList = soup.find_all(name='div', attrs={"class": "ellipsis rank01"})
        for idx, title in enumerate(titleList):
            # print(f'{idx + 1}위 {title.find("a").text}')  # idx 는 0에서부터 시작함.
            self.music_list.append(f'{idx + 1},{title.find("a").text}')

        artistList = soup.find_all(name='div', attrs={"class": "ellipsis rank02"})
        for idx, artist in enumerate(artistList):
            self.music_list[idx] += ',' + artist.find("a").text

    def save_file(self):
        filePath = "./data/melon.csv"
        f = codecs.open(filePath, 'w', 'euc-kr')
        for music in self.music_list:
            data = f"{music}\n"
            try:
                f.write(data)
            except:
                print(f'encoding에 문제가 있는 곡은 => {music}')
                pass

        f.close()

    @staticmethod
    def main():
        melon = Melon()
        melon.set_url('dayTime=2021060515')
        melon.get_ranking()
        melon.save_file()


Melon.main()