#coding : utf-8
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent import DependentData
from util.send_email import SendEmail
from base.mock_demo import mock_test
import HTMLTestRunner

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
    # 程序执行的主入口
    def go_on_run(self):
        #rows_count = self.data.get_case_lines()
        rows_count = 2
        pass_count = []
        fail_count = []
        res = None
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            request_data = self.data.get_data_for_json(i)
            header = self.data.get_is_header(i)
            expect = self.data.get_expect_data_for_sql(i)
            print(expect)
            print(type(expect))
            depend_case = self.data.is_depend(i)
            '''if depend_case != '':
                self.depend_data = DependentData(depend_case)
                #获取依赖的响应数据
                depend_response_data = self.depend_data.get_data_for_key(i)
                #获取依赖的key
                depend_key = self.data.get_depend_field(i)
                request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method,url,request_data,header)'''
            #res = self.run_method.run_main(method, url, request_data, header)
            request_data1 = {"id": 1, "username": "tanyang", "password": "tanyang", "email": "tanyang@test.com", "age": 18}
            ress = mock_test(self.run_method.run_main(method, url, request_data, header),request_data,url,method,request_data1)
            print(ress)
            print(type(ress))
            if is_run:
                if self.com_util.is_equal_dict(expect,ress):
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i,ress)
                    fail_count.append(i)
        self.send_email.send_main(pass_count,fail_count)

if __name__=='__main__':
    run = RunTest()
    print(run.go_on_run())





