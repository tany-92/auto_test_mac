#coding:utf-8

import json
from filecmp import cmp


class CommonUtil:
    #判断一个字符串是否在另外一个字符串中,str_one：查找的字符串，str_two:被查找的字符串
    def is_contain(self,str_one,str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return dict_one==dict_two


if __name__ == '__main__':
    dict_one = {"id": 1, "username": "tanyang", "password": "tanyang", "email": "tanyang@test.com", "age": 18}
    dict_two = {'id': 1, 'username': 'tanyang', 'password': 'tanyang', 'email': 'tanyang@test.com', 'age': 18}
    res = CommonUtil().is_equal_dict(dict_one,dict_two)
    print(res)

