import numpy as np
import pandas as pd
# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# a = pd.Series([1,2,3,4,5])
# print(a)
# a = pd.Series(np.array([1,2,3,4,5]))
# print(a)
# # - скалярные значение
# b = pd.Series(2)
# print(b)
# d = pd.Series(2, index=[0, 1, 2, 3, 4])
# print(d)
# # - словари
# dict = pd.Series({'1':2 , '2' : 3, '3' : 4})
# print(dict)


# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
# a = pd.Series([1,2,3,4,5])
# d = pd.Series(2, index=[0, 1, 2, 3, 4])
# Ser = pd.DataFrame({
#     'a' : a,
#     'b' : d
# })
# print(Ser)
# - списки словарей
# d = [{
#     'city':'SPB',
#     'country':'Rus'},
#     {'planet':'Earth',
#     'Galaxy':'Milky Way'}
#     ]
# dic = pd.DataFrame(d)
# print(dic)
# - словари объектов Series
# Ser = pd.DataFrame({'A': s1, 'B': s2})
# print(df3)
# - двумерный массив NumPy
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arrdata = pd.DataFrame(arr, columns=['a', 'b', 'c'])
# print(arrdata)
# - структурированный массив Numpy
# dtype = [('A', 'int32'), ('B', 'float32')]
# structured_array = np.array([(1, 2.0), (3, 4.0)], dtype=dtype)
# df = pd.DataFrame(structured_array)
# print(df)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
# s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# s2 = pd.Series([4, 5], index=['b', 'd'])
# result = s1.combine_first(s2).fillna(1)
# print(result)
# print(s1+s2)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
# df = pd.DataFrame({
#     'A': [1, 2, 3],
#     'B': [4, 5, 6],
# })

# result = df - 1
# print(result)

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
df = pd.DataFrame({
    'A': [1, np.nan, 3, None],
    'B': [4, 5, np.nan, 7],
    'C': [np.nan, 8, 9, pd.NA]
})

print(df)
print(df.ffill())
print(df.bfill())

