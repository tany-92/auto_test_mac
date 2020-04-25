
#coding: utf-8

import unittest
from get_post_test import RunMain
import json
from other import HTMLTestRunner

from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()

    #执行的case
    def test_01(self):
        url = 'https://t-auth3.fvt.tujia.com/ios/api/condition/list.api'
        data = {
            "hotelId": 189,
            "date": "2020-03-25",
            "pageSize": 30,
            "pageNum": 1
        }

        #self.run.run_main=mock.Mock(return_value=data)
        #print(mock_data)
        res = mock_test(self.run.run_main,data,url,'POST',data)

        #res = self.run.run_main(url,'POST',data)
        print(res)

        #globals()['userid']= 10000
        self.assertEqual(res["hotelId"],189,"测试失败")
        print('这是第一个case')
    @unittest.skip('test_03')

    def test_02(self):
        url = 'https://camorope-client-a.meiqia.com/pusher/info?browser_id=97178b0a01a392638cecb36ad65e681e&ent_id=165418&track_id=1ZhdtWoOWQ3GUuREKYirS746cUl&visit_id=1ZhdtVtGBKc4gbJiTF7BkTxRiav&t=1585295474335'

        res = json.loads(self.run.run_main(url,'GET'))

        #print(userid)
        self.assertEqual(res['cookie_needed'],True,"测试失败")
        print('这是第二个case')



if __name__ == '__main__':
    file = open("/report/report.html", mode="wb")

    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='this is first report')
    runner.run(suite)
