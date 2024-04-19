import csv


class TestWithCsv:
    def get_data(self):
        with open('../data/test_data.csv', 'r', encoding="utf-8") as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                print(row)

    def test_with_csv(self):
        csv_obj = TestWithCsv()
        csv_obj.get_data()
