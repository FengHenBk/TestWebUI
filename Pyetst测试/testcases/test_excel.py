import openpyxl


class TestWithExcel:
    def test_get_data(self):
        # 读取工作簿
        book = openpyxl.load_workbook("../data/test_date.xlsx")
        # 获取活动工作表
        sheet = book.active
        # 获取数据
        # a_1 = sheet.cell(row=1, column=1).value
        a_1 = sheet["A1"]
        print(a_1)
        book.close()


