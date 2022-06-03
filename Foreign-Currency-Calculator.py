import lxml #для парсинга с сайта
import csv #для изменения формата файла (в дальнейшем для удобства работы)
import pandas as pandi #модуль для парсинга с сайта
class NATO:
    """Класс для конвертации валют с сайта ЦБ РФ"""
    value1 = 0 #значение 1 валюты
    value2 = 0 #значение 2 валюты
    many_f1 = '' #строчная запоминалка валюты (для удобства работы)
    zak = 0     #защёлка для предотвращения бесконечной рекурсии вызова поиска по валютам
    kurs = pandi.read_html('https://cbr.ru/currency_base/daily/') #модуль читает данные с сайта центробанка
    print(kurs[0]) #вывод всей информации (для удобства работы)
    lenka = len(kurs[0]) #длина информации (для модификаций)
    many_finder = [] #список для занесения данных по валютам
    kurs[0].to_csv('1.csv') #превращаем информацию с сайта в формат csv
    def __init__(self,name):
        self.name = name #имя валюты
    def __str__(self):
        return str(NATO.value1/NATO.value2) #итоговый перевод из 1-ой валюты во 2-ую валюту
    def searching(self):
        with open("1.csv", encoding='utf-8') as f: #открываем файл (способ чтения на усмотрение)
            file_reader = csv.reader(f) #читаем файл
            count = 0 #счётчик
            for row in file_reader: #для каждой строки данных в исходном файле информации формата csv
                if count == 0: #выводим первую строку с заголовками столбцов по умолчанию
                    str_ = ' '.join(row) #преобразуем в строку
                    NATO.many_finder.append(str_[1:]) #сами заголовки
                else:
                    if self.name in row[4].lower(): #все валюты в которых было совпадение по запросу пользователя
                        NATO.many_finder.append(f'{row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
                        continue
                    else: #для перебора всех возможных
                        pass
                if count < NATO.lenka:  # не превышая длинны
                    count += 1


            if len(NATO.many_finder) > 2: #если несколько совпадений
                print('Найдено несколько совпадений:\n')
                for i in NATO.many_finder:
                    print(str(i) + '\n')
                choice = int(input('Введите номер строки для выбора:\n')) #выбираем конкретнее(если нашли несколько)
                NATO.many_f1 = NATO.many_finder[choice]
                print(NATO.many_f1)
            else: #если совпадений = 1,то сразу выводим
                NATO.many_f1 = NATO.many_finder[1]
                print(NATO.many_f1)

    def calculator(self): #калькулятор конвертации
        if NATO.zak == 0: #значение задаётся для первой валюты всего 1 раз, а второй эта функция не требуется
            value1 = int(input('Введите значение для: '+ NATO.many_f1 + '\n'))
            v_1 = NATO.many_f1.split() #разделяем информацию в строке для вывода только курса валюты
            NATO.value1 = (int(v_1[-1])/10000)*value1 #преобразуем его в корректное числовое значение
            print(value1) #показываем пользователю
            NATO.many_finder.clear() #очистка ячеек для перехода к новой валюте
            v_1.clear() #очистка ячеек для перехода к новой валюте
            NATO.zak += 1 #защёлка сработала - рекурсия предотвращена
            self.name = input('Введите полное название ВТОРОЙ валюты:\n')
            self.name = self.name.lower() #предотвращаем сбой по литералу
            ss = NATO.searching(self) #запускаем функцию поиска для 2-ой валюты
            NATO.calculator(self) #рекурсия
        else: #настало время второй валюты
            v_1 = NATO.many_f1.split() #разделяем информацию в строке для вывода только курса валюты
            NATO.value2 = int(v_1[-1])/10000 #преобразуем его в корректное числовое значение







name_wallet = input('Введите полное название ПЕРВОЙ валюты:\n')
try:
    cl = NATO(name_wallet.lower())
    cl.searching()
    cl.calculator()
    print(cl)
except IndexError:
    print('Некорректное значение!')
except ValueError:
    print('Некорректное значение!')