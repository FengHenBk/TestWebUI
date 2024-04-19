import openpyxl
import pytest
import yaml
import csv
from Pyetst测试.func.operation import my_add


# 用到yaml文件时，需要先读取出来
# def get_data():
#     with open('../data/test.yaml', encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#
#     return data
#
#
# def write_data():
#     with open('../data/test.yaml', 'w', encoding="utf-8") as f:
#         data = [1, 2, 3]
#         yaml.safe_dump(data, f)


# class TestWithYAML:
#     # 参数化实现
#     @pytest.mark.parametrize('x,y,expected', [[1, 1, 2]])
#     def test_add(self, x, y, expected):
#         assert my_add(int(x), int(y)) == int(expected)
#
#     @pytest.mark.parametrize('x,y,expected', get_data())
#     def test_add2(self, x, y, expected):
#         assert my_add(int(x), int(y)) == int(expected)




