import numpy as np
import pandas as pd

#pandas - расширение NumPy (структурированные массивы). Строки и столбцы индексируются метками, а не только числовыми значениями

#Series,DataFrame,Index

##Series

# data = pd.Series([0.25, 0.5, 0.75, 1])
# print(data)
# print(type(data))

# print(type(data.values))
# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1])
# print(data[0])
# print(data[1:3])

# data = pd.Series([0.25, 0.5, 0.75, 1],index=['a','b','c','d'])
# print(data)
# print(data['a'])
# print(data['b':'d'])

# print(type(data.index))

# data = pd.Series([0.25, 0.5, 0.75, 1],index=[1,10,7,'d'])

# print(data)
# print(data[1])
# print(data[10:'d'])

# population_dict = {
#     'city1':1001,
#     'city2':1002,
#     'city3':1003,
#     'city4':1004,
#     'city5':1005,
# }
# population = pd.Series(population_dict)
# print(population)

# print(population['city4'])
# print(population['city4':'city5'])

#для создания сериас можно исппльзовать 
#Списки питона или массивы нампи
#Скалярные значения
#Словари

##dataFrame -двумерный массив с явно определенными индексами.Последовательность "Согласованных " обьектов Series

# population_dict = {
#     'city1':1001,
#     'city2':1002,
#     'city3':1003,
#     'city4':1004,
#     'city5':1005,
# }
# area_dict ={
#     'city1':9991,
#     'city2':9992,
#     'city3':9993,
#     'city4':9994,
#     'city5':9995,
# }

# population =pd.Series(population_dict)
# area  =pd.Series(area_dict)

# states = pd.DataFrame({
#     'population1':population,
#     'area1':area
# })
# print(states)

# print(states.values)
# print(states.index)
# print(states.columns)
# print(type(states.values))
# print(type(states.index))
# print(type(states.columns))

# print(states['area1'])

# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив Numpy

#Index -способ организации ссылки на данные обьектов series и DataFrame.Index -неизменякем, упорядочен,является мультимножеством(Могут быть повторяющиеся значения)

# ind = pd.Index([2,3,4,5,11])
# print(ind[1])
# print(ind[::2])

#ind[1] = 5- запрещено

#Index - следует соглашениям обьекта set
# indA = pd.Index([1,2,3,4,5])
# indB = pd.Index([2,3,4,5,6])

# print(indA.intersection(indB))

#Выбиорка данных из Series
#как словарть

# data = pd.Series([0.25, 0.5, 0.75, 1],index=['a','b','c','d'])
# print('a' in data )
# print('z' in data )
# print(data.keys())

# print(list(data.items()))

# data['a'] = 100
# data['z'] = 1000
# print(data)


## как одномерный массив
# data = pd.Series([0.25, 0.5, 0.75, 1],index=['a','b','c','d'])
# print(data['a':'c'])
# print(data[0:2])

#атрибуты - индексаторы
# data = pd.Series([0.25, 0.5, 0.75, 1],index=[1,3,10,15])
# print(data[1])
# print(data.loc[1])
# print(data.iloc[1])

#Выборка данных из DataFrame
#как словарь
# pop = pd.Series({
#     'city1':1001,
#     'city2':1002,
#     'city3':1003,
#     'city4':1004,
#     'city5':1005,})

# area = pd.Series({
#     'city1':9991,
#     'city2':9992,
#     'city3':9993,
#     'city4':9994,
#     'city5':9995,
# }
# )
# data = pd.DataFrame({
#     'area1':area,
#     'pop1':pop,
#     'pop':pop
# })
# print(data)
# print(data['area1'])
# print(data.area1)
# print(data.pop1 is data['pop'])

# data['new'] = data['area1']

# data['new1'] = data['area1']/data['pop']

# print(data)
#как нампи двукмерный массив 
# data = pd.DataFrame({
#     'area1':area,
#     'pop1':pop,
#     'pop':pop
# })
# print(data)
# print(data.values)
# print(data.T)
# print(data['area1'])
# print(data.values[0])

#фтрибуты-индексаторы

# print(data)
# print(data.iloc[:3,1:2])
# print(data.loc[data['pop'] >1002, ['pop1','pop']])

# data.iloc[0,2] = 99999

# print(data)


# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0,10,4))

# print(s)
# print(np.exp(s))

# pop = pd.Series({
#     'city1':1001,
#     'city2':1002,
#     'city3':1003,
#     'city41':1004,
#     'city51':1005,})

# area = pd.Series({
#     'city1':9991,
#     'city2':9992,
#     'city3':9993,
#     'city42':9994,
#     'city52':9995,
# }
# )
# data = pd.DataFrame({
#     'area1':area,
#     'pop1':pop,
#     'pop':pop
# })

# print(data)

# dfA =pd.DataFrame(rng.integers(0,10,(2,2)),columns =['a','b'])
# dfB =pd.DataFrame(rng.integers(0,10,(3,3)),columns =['a','b','c'])
# print(dfA)
# print(dfB)
# print(dfA+dfB)

# rng = np.random.default_rng(1)

# A = rng.integers(0, 10, (3,4))
# print(A)

# print (A[0])

# print(A - A[0])

# df = pd.DataFrame(A, columns=['a','b','c','d'])
# print(df)

# print(df.iloc[0])
# print(df['a'])

# print(df - df['a'])

# rng = np.random.default_rng(1)
# A = rng.integers(0, 10, (3,4))
# print(A)
# df = pd.DataFrame(A, columns=['a','b','c','d'])
# print(df - )

#NaN - not a number
#NA - значения : NaN, null

#pandas.Два способа хранения отсутствующих значений
#NaN,null
#null

#None - объект
