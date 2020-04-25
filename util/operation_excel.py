#coding: utf-8

import xlrd
from xlutils.copy import copy

'''data = xlrd.open_workbook('/Users/tany/Downloads/study/autotest/p22naf/dataconfig/case1.xls')

tables = data.sheets()[0]

print(tables.nrows)

print(tables.cell_value(2,9))'''

class OperationExcel:
    def __init__(self,filename=None,sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
        else:
            self.filename = '/Users/tany/Downloads/study/autotest/p22naf/dataconfig/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    #获取表格内容
    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    #获取某个单元格内容
    def get_cell_value(self,row,col):
        tables = self.data
        return tables.cell_value(row,col)
    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.filename)

    #根据case_id找到行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_value(row_num)
        return rows_data

    #根据对应的case_id找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_col_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num +1

    #根据行号找到该行的内容
    def get_row_value(self,row):
        tables = self.data
        tables_value = tables.row_values(row)
        return tables_value

    #获取某列内容
    def get_col_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols



if __name__== '__main__':
    opers = OperationExcel()
    #print(opers.get_cell_value(2,9))
    print(opers.get_row_num('Imooc-11'))
