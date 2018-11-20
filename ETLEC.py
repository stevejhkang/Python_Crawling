#ETLEC : EveryTime Lecture Evaluation Crawling
import requests
from bs4 import BeautifulSoup

class ETLEC:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.auth = False
        self.professorList = []
        self.LEList = []
    
    def set_auth(self):
        login_info = {'userid': self.userid, 'password': self.password, 'redirect': '/'}
        base_url = 'https://everytime.kr'

        with requests.Session() as session:
            user_res = session.post(base_url+'/user/login', data=login_info)
            soup = BeautifulSoup(user_res.text, 'html.parser').select('body div')

            # 첫 번째 예외 처리 // 로그인 실패
            if len(soup) == 0:
                self.auth = False
                return False
            

            self.auth = True
            return True
    
    def set_professor_list(self):
        self.professorList = []

        if self.auth == False:
            return self.professorList
        


        
    