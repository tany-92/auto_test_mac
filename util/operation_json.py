import json

'''fp = open('/Users/tany/Downloads/study/autotest/p22naf/dataconfig/user.json')
data = json.load(fp)
print(data['user1'])'''

#定义类
class OperationJson:
    def __init__(self):
        self.data = self.read_data()

     #获取json文件
    def read_data(self):
        with open('/Users/tany/Downloads/study/autotest/p22naf/dataconfig/user.json') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]


if __name__=='__main__':
    opjson = OperationJson()
    print(opjson.get_data("user"))