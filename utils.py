# 导入json模块
import json


# 封装通用断言函数
def assert_common_utils(self,response,st_code,success,code,message):
    self.assertEqual(st_code,response.status_code)
    self.assertEqual(success,response.json().get("success"))
    self.assertEqual(code,response.json().get("code"))
    self.assertEqual(message,response.json().get("message"))

# 封装读取登录数据的函数
def read_login_data(filename):
    # filename：是指登录数据的路径和名称
    with open(filename,'r',encoding="utf-8") as f:
        jsonData=json.load(f)
        # print(jsonData)
        result_list=[]
        for login_data in jsonData:
            # 将所有的登录数据以元组的形式存在空列表result_list中
            # print(tuple(login_data.values()))
            result_list.append(tuple(login_data.values()))
    return result_list

# interface_name:要加载的对应员工接口的数据(只有增删改查4个数字)
def read_emp_data(filename, interface_name):
    # filename:员工的数据文件路径
    # interface_name:要加载的对应员工接口的数据(只有增删改查4个数字)
    with open(filename, 'r', encoding='utf-8') as f:
        # 把数据文件加载成json格式
        jsonData = json.load(f)
        # 定义一个存放数据的空列表
        result_list = list()
        # 存放员工的某个接口的数据到空列表
        result_list.append(tuple(jsonData.get(interface_name).values()))

    return result_list


