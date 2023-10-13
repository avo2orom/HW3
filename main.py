
import re
import sys
import datetime
from datetime import datetime


def dubles(reg, userline, data):
    count = 0
    count = len(re.findall(reg, userline))
    #	print("debuguserline=",userline)
    if count >> 1:
        print(f'{data} введено {count} раз')
        #                sys.exit()
        line = ''
        return


def main():
    userline = input("Введите ФИО, разделенные проблемами, дату рождения в формате dd.mm.yyyy, номер телефона без разделителя, пол f/m: ")
    #userline = '89266439196 Nagaev Alex Petrovich m 14.10.2013'  # на время отладки. для прода раскомментировать предыдущую строку
    #userline = 'M Malkova Aleksandra Leonidovna 30.10.1996 11111111111'
    print("\n------------------\nUserline= ", userline)
    reg = r'\d{2}\.\d{2}\.\d{4}'
    data = "Дата"
    dubles(reg, userline, data)
    parsdate = re.search(reg, userline)

    try:
        userline = userline.replace(parsdate.group(0), '')
    except:
        print("Неверно указана или отсутствует дата рождения. Дата рождения должна быть указана в формате dd.mm.yyyy")
        #		sys.exit()
        line = ''
        return

    dpars = datetime.strptime(parsdate.group(0), "%d.%m.%Y").date()
    now = datetime.now()
    dcur = now.date()
    ddif = dcur - dpars
    zero = dcur - dcur

    if ddif < zero:
        print("Введенная дата еще не наступила")
        #		sys.exit()
        line = ''
        return

    reg = r'\d{11}'
    data = "Телефон"
    dubles(reg, userline, data)
    parsphone = re.search(reg, userline)
    # print(parsphone)
    try:
        userline = userline.replace(parsphone.group(0), '')
    except:
        print("Неверно указана или отсутствует телефон. Телефон должен быть указан в формате 11 цифр без разделителей")
        #		sys.exit()
        line = ''
        return

    reg = r'\s[m,M]|\s[f,F]|[m,M]/s|[f,F]/s'  # непонятно можно ли кпростить
    data = "Пол"
    dubles(reg, userline, data)
    parssex = re.search(reg, userline)
    # print(parssex)
    try:
        userline = userline.replace(parssex.group(0), '')
    except:
        print("Неверно указана или отсутствует пол. Укажите f или m")
        #		sys.exit()
        line = ''
        return

    userline = userline.strip()

    reg = r'[A-Z][a-z]*\s[A-Z][a-z]*\s[A-Z][a-z]*'
    data = "ФИО"
    dubles(reg, userline, data)
    parsfio = re.search(reg, userline)
    # print(parsfio)
    try:
        userline = userline.replace(parsfio.group(0), '')
    except:
        print("Неверно указана или отсутствует ФИО. Укажите в формате Фамилия Имя Отчество")
        #		sys.exit()
        line = ''
        return

    ##выделяем фамилию
    fname = re.search(r'[A-Z][a-z]*\s', parsfio.group(0))

    if userline != '':
        print("Введены лишние данные: ", userline)
        #		sys.exit()
        line = ''
        return

    print("Date: ", parsdate.group(0))
    print("Phone: ", parsphone.group(0))
    print("Sex: ", parssex.group(0))
    print("FIO: ", parsfio.group(0))
    print("First Name: ", fname.group(0))

    filename = fname.group(0).strip() + ".txt"

    try:
        f = open(filename, 'a')
        f.write(f'{parsfio.group(0)} {parsdate.group(0)} {parsphone.group(0)} {parssex.group(0).strip()}\n')
        f.close()
    except:
        print("Ошибка записи в файл ", filename)
        return


main()
