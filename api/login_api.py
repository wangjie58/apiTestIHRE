import requests
# class LoginApi:
#     def __init__(self):
#         self.login_url="http://182.92.81.159/api/sys/login"
#     def login(self,jsonData,headers):
#         response=requests.post(url=self.login_url,json=jsonData,headers=headers)
#         return response
class LoginApi:
    def __init__(self):
        self.login_url="http://182.92.81.159/api/sys/login"
    def login(self,jsonDate,headers):
        return requests.post(url=self.login_url,json=jsonDate,headers=headers)
