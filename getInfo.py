def maket_float (table, x):
    rows = table.find_all('tr')
    money = rows[x].find_all('td')
    i = 2018 - len(money[1:-2])
    sale = []
    for a in money[1:-2]:
        i = i + 1
        try:
            sale.append(float(a.text.replace(' ', '').replace('\t', '')))
        except ValueError:
            sale.append('')
            continue
    return sale

def maket (table, x):
    rows = table.find_all('tr')
    money = rows[x].find_all('td')
    i = 2018 - len(money[1:-2])
    sale = []
    for a in money[1:-2]:
        i = i + 1
        try:
            sale.append(a.text.replace(' ', '').replace('\t', ''))
        except ValueError:
            sale.append('')
            continue
    return sale

def getNumber(table, name): #поиск номера
    name2 = ''
    i = 0
    x = 0
    while name2 != name:
        if i > 60:
            break
        try:
            rows = table.find_all('tr')[i]
            name2 = str(rows.find('a').text)
        except AttributeError:
            pass
        except IndexError:
            pass
        i += 1
    if name2 == name:
        x = i -1
    return x

#Свой параметр
def my_setting(table, name):
    x = getNumber(table, name)
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Свой параметр (%)
def my_setting_prof(table, name):
    x = getNumber(table, 'Выручка')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket(table, x)

#Выручка
def sales (table):
    x = getNumber(table, 'Выручка')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Себестоимость
def cogs (table):
    x = getNumber(table, 'Себестоимость')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Чистая прибыль
def net_income(table):
    x = getNumber(table, 'Чистая прибыль')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#CAPEX
def capex (table):
    x = getNumber(table, 'CAPEX')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Операционные расходы
def operating_expenses(table):
    x = getNumber(table, 'Опер. расходы')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Ниокр
def R_and_D(table):
    x = getNumber(table, 'НИОКР')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Процентные расходы
def interest_expense(table):
    x = getNumber(table, 'Процентные расходы')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Цена акции
def price_action(table):
    x = getNumber(table, 'Цена акции ао')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Балансовая стоимость
def book_value(table):
    x = getNumber(table, 'Баланс стоимость')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#Чистая рентабельность - (чист.прибыль/выручка)
def net_margin(table):
    x = getNumber(table, 'чистая рентаб')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket(table, x)

#P/E
def pe(table):
    x = getNumber(table, 'P/E')
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)

#P/BV
def pbv(table):
    x = getNumber(table, 'P/BV') #P/B или P/BV
    if x == 0:
        return ['', '', '', '', '', '']
    return maket_float(table, x)