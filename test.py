from timeit import timeit

setup = 'test_list = [10 ** 3] * 10 ** 8'
number = 10 **3

stmt = '''
while test_list:
    test_list.pop()
'''
print(timeit(stmt=stmt, setup=setup, number=number))
# 4.991474372000084

stmt = '''
test_list_pop = test_list.pop
while test_list:
    test_list_pop()
'''
print(timeit(stmt=stmt, setup=setup, number=number))
# 3.1912732280002274
