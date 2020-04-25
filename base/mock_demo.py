#coding:utf-8

from unittest import mock

#模拟mock封装
def mock_test(mockmethod,request_data,url,method,response_data):
    mockmethod=mock.Mock(return_value=response_data)
    res = mockmethod(url, method, request_data)
    return res

