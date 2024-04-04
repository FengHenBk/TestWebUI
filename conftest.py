# # from _pytest.config import Parser, Config
# #
# # global_env = {}
# #
# #
# # def pytest_addoption(parser: Parser):
# #     # parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")
# #     mygroup = parser.getgroup("mygroup")
# #     mygroup.addoption(
# #         "--browser", default="Chrome", help="指定的浏览器"
# #     )
# #
# #
# # def pytest_configure(config: Config):
# #     browser = config.getoption("--browser", default='Chrome')
# #     global_env['browser'] = browser
#
#
# # def pytest_collection_modifyitems(items):
# #     """
# #     测试用例收集完成时，将收集到的用例名称和用例标识nodeid的中文信息显示在控制台
# #     :param items:
# #     :return:
# #     """
# #     for item in items:
# #         item.name = item.name.encode("utf-8").decode("unicode_escape")
# #         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
#
# # 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
#     """
#     for i in items:
#         i.name = i.name.encode("utf-8").decode("unicode_escape")
#         i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")
