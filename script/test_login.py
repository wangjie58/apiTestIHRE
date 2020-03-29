import unittest
import logging
from api.login_api import LoginApi
import app
# class LoginConfig:
#     # 在登录的配置类中增加HEADERS变量
#     HEADERS = {"Content-Type": "application/json"}
from utils import assert_common_utils


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass
    def test01_login_success(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456"}
        # 定义请求头
        # HEADERS = {"Content-Type": "application/json"}
        response=self.login_api.login(jsonData,app.HEADERS)
        # 利用日志模块打印登录的结果
        logging.info("登录成功的结果为：",response.json())
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self,response,200,True,10000,"操作成功！")

    def test02_password_is_error(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "1234567"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test03_mobile_is_not_exist(self):
        jsonDate={"mobile":"13900000009","password":"123456"}
        response=self.login_api.login(jsonDate,app.HEADERS)
        logging.info("账号不存在：",response.json())
        assert_common_utils(self,response,200,True,10000, "操作成功！")
    def test04_mobile_has_eng(self):
        jsonDate={"mobile": "138000A0X2", "password": "123456"}
        response=self.login_api.login(jsonDate,app.HEADERS)
        logging.info("输入的手机号码有英文字符:",response.json())
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    def test05_mobile_has_special(self):
        jsonData={"mobile": "1380(*000002", "password": "123456"}
        response=self.login_api.login(jsonData,app.HEADERS)
        logging.info("手机号码有特殊字符:",response.json())
        assert_common_utils(self,response,200, False, 20001, "用户名或密码错误")
    def test06_mobile_is_None(self):
        jsonData={"mobile":"","password": "123456"}
        response=self.login_api.login(jsonData,app.HEADERS)
        logging.info("手机号码为空:",response.json())
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
    def test07_password_is_None(self):
        pass
    def test08_more_params(self):
        jsonData={"mobile": "13800000002", "password": "123456","sign":"123"}
        response=self.login_api.login(jsonData,app.HEADERS)
        logging.info("多出1个参数:",response.json())
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
    def test09_less_mobile(self):
        pass

    # 少参-缺少password
    def test10_less_password(self):
        pass

    # 无参
    def test11_none_params(self):
        # 定义登录成功所需要的请求体
        jsonData = None
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 错误参数--输入错误的参数
    def test12_params_is_error(self):
        # 定义登录成功所需要的请求体
        jsonData = {"mboile": "13800000002", "password": "123456"}
        # 利用封装的登录接口，发送登录请求，测试ihrm系统
        response = self.login_api.login(jsonData, app.HEADERS)
        # 利用日志模块打印登录的结果（首先要导入日志模块）
        logging.info("登录成功的结果为：{}".format(response.json()))
        # 断言登录的结果：响应状态码、success、code、message
        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
