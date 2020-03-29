import unittest
import logging
import app
from api.emp_api import EmpApi
from api.login_api import LoginApi
import requests
from utils import assert_common_utils

'''
class TestEmp(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
        self.emp_api=EmpApi()
    def tearDown(self):
        pass
    def test01_add_emp(self):
        # 1 实现登录接口
        response=self.login_api.login({"mobile": "13800000002", "password": "123456"},headers=app.HEADERS)
        result=response.json()
        logging.info("员工模块登录接口的结果为：{}".format(result))
        token=result.get("data")
        headers={"Content-Type": "application/json", "Authorization":"Bearer "+token}
        logging.info("登录成功后设置的请求头为：{}".format(headers))
        # 2 实现添加员工接口
        response=self.emp_api.add_emp("尼古拉us8", "14587379909",headers)
        logging.info("添加员工的结果为：{}".format(response.json()))
        add_result=response.json()
        emp_id=add_result.get("data").get("id")
        logging.info("获取员工ID为：{}".format(emp_id))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 3 实现查询员工接口
        response=self.emp_api.search_emp(emp_id,headers)
        logging.info("查询员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 4 实现修改员工接口
        response=self.emp_api.modify_emp(emp_id, "fd67r5", headers)
        logging.info("修改员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 5 实现删除员工接口
        response=self.emp_api.delete_emp(emp_id,headers)
        logging.info("删除员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
'''
class TestEmp(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
        self.emp_api=EmpApi()
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
    def tearDown(self):
        pass
    def test01_add_emp(self):
        # 1 实现登录接口
        response=self.login_api.login({"mobile": "13800000002", "password": "123456"},headers=app.HEADERS)
        logging.info("员工模块登录接口的结果为：{}".format(response.json()))
        token=response.json().get("data")
        headers={"Content-Type":"application/json","Authorization":"Bearer "+token}
        # 2 实现添加员工接口
        response=self.emp_api.add_emp("尼古拉5s8", "14587379709", headers)
        logging.info("添加员工:",response.json())
        emp_id=response.json().get("data").get("id")
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 3 实现查询员工接口
        response=self.emp_api.search_emp(emp_id,headers)
        logging.info("查询员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 4 实现修改员工接口
        response=self.emp_api.modify_emp(emp_id,"dffs3",headers)
        logging.info("修改员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")
        # 5 实现删除员工接口
        response=self.emp_api.delete_emp(emp_id,headers)
        logging.info("删除员工的结果为：{}".format(response.json()))
        assert_common_utils(self, response, 200, True, 10000, "操作成功！")