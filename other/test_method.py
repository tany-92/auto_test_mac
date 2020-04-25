
#coding: utf-8

import unittest
from get_post_test import RunMain
import json

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


        res = json.loads(self.run.run_main(url,'POST',data))


        self.assertEqual(res["ver"],"2.0","测试失败")

    def test_02(self):
        url = 'https://camorope-client-a.meiqia.com/pusher/info?browser_id=97178b0a01a392638cecb36ad65e681e&ent_id=165418&track_id=1ZhdtWoOWQ3GUuREKYirS746cUl&visit_id=1ZhdtVtGBKc4gbJiTF7BkTxRiav&t=1585295474335'


        res = json.loads(self.run.run_main(url,'GET'))

        print(res)
        self.assertEqual(res['cookie_needed'],False,"测试失败")


if __name__ == '__main__':
    unittest.main()