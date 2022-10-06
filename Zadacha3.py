# ф-ция map - https://pythonist.ru/python-map-znakomstvo/
lst = list(map(float, input("Введите числа через пробел:\n").split()))
# split дл разделения строки https://pythonim.ru/string/str-split-python
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# round - округление до кол-ва знаков после запятой
print(max(new_lst) - min(new_lst))