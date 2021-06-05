from bs4 import BeautifulSoup
import requests

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = [] # 파이썬에서 복수의 값을 담는 리스트


    def set_url(self, detail):
        # detail 은 chartdate=20210605&charthour=11 부분으로 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}').text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='p', attrs={"class":"title"})
        for idx, title in enumerate(ls1):
            print(f'{idx+1}위 {title.find("a").text}' ) # idx 는 0에서부터 시작함.

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.set_url('chartdate=20210605&charthour=11')
        bugs.get_ranking()

Bugsmusic.main()