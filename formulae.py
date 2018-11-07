def maket(a, b): # (a/b) * 100%
    result = []
    i = 0
    for x in a:
        try:
            result.append(str(round((x/b[i]) * 100)) + '%')
        except TypeError:
            result.append('')
        except IndexError:
            result.append('')
        i = i + 1
    return result

def gross_margin(gross_profit, sales): #Валовая маржа
    return maket(gross_profit, sales)

def k_sg_and_a(sga, gross_profit): #Коэффициент SG&A от величины валовой прибыли
    return maket(sga, gross_profit)

def k_depreciation(depreciation, gross_profit): #Коэффициент амортизации от величины валовой прибыли
    return maket(depreciation, gross_profit)

def k_net_income(net_income, gross_profit): #Отношение чистой прибыли к валовой
    return maket(net_income, gross_profit)

def k_interest_expense(interest_expense, operating_income): #Отношение процентных расходов к операционной прибыли
    return maket(interest_expense,operating_income)

def k_capex(capex, net_income): #Отношение CAPEX к чистой прибыли
    return maket(capex, net_income)

def roa(net_income, sum_asset): #Рентабельность активов (ROA)
    return maket(net_income, sum_asset)

def roe(net_icome, equity): #Рентабельность акционерного капитала (ROE)
    return maket(net_icome, equity)

def k_dept_and_equity(dept, equity): #Соотношение заёмных и собсвенных средств
    return maket(dept, equity)