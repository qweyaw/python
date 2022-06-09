import xlrd

# 打开 excel
workbook = xlrd.open_workbook('test.xls')
print(workbook)  # <xlrd.book.Book object at 0x7fa04c368a30>

# 获取所有的 sheet 名称
sheet_names = workbook.sheet_names()
print(sheet_names) # ['test']

# 获取所有的 sheet 对象 或 某一个
sheet_objects = workbook.sheets()
print(sheet_objects) # [Sheet  0:<test>]

# 通过 index 获取
sheet_test = workbook.sheet_by_index(0)
print(sheet_test) # Sheet  0:<test>

# 通过 name 获取
sheet_test = workbook.sheet_by_name(sheet_name = 'test')
print(sheet_test) # Sheet  0:<test>

""" 判断某个sheet是否已导入"""
# 通过 index 判断 sheet 是否导入
sheet_test_is_load = workbook.sheet_loaded(sheet_name_or_index=0)
print(sheet_test_is_load)  # True
# 通过 sheet 名称判断 sheet 是否导入
sheet_test_is_load = workbook.sheet_loaded(sheet_name_or_index="test")
print(sheet_test_is_load)  # True

""" 对 sheet 对象中的行执行操作: 如有效行数、某行从n1到n2列的数据、某行的单元和类型、某行的长度...... """
# 获取 sheet 中的有效行数
nrows = sheet_test.nrows
print(nrows)   # 3
# 获取 sheet 中第 3 行的数据
all_row_values = sheet_test.row_values(rowx=2)
print(all_row_values)    # ['时尚', '我', 's']
# 获取 第2行 第 1-2 列 （不包含2）
row_values = sheet_test.row_values(rowx=2, start_colx=1, end_colx=2)
print(row_values)               #  ['我']
# # 获取 sheet 中第 3 行的单元对象
row_object = sheet_test.row(rowx=2)
print(row_object)   # [text:'时尚', text:'我', text:'s']
# # 获取 sheet 中第 3 行的单元
row_slice = sheet_test.row_slice(rowx=2)
print(row_slice)    # [text:'时尚', text:'我', text:'s']
# # 获取 sheet 中第3行的单元类型
row_types = sheet_test.row_types(rowx=2)
print(row_types)      # array('B', [1, 2, 1])
# # 获取 sheet 中第3行的长度
row_len = sheet_test.row_len(rowx=2)
print(row_len)     # 3
# # 获取 sheet 所有行的生成器
rows_generator = sheet_test.get_rows()
print(rows_generator)   # <generator object Sheet.get_rows.<locals>.<genexpr> at 0x7fd59e686120>
