import urllib.request
import getInfo
import cov
import formulae
import show
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def main():
    Calculation(get_html('https://smart-lab.ru/q/RSTI/f/y/MSFO/')) #Ссылка сайта

def Calculation(html):
    soup = BeautifulSoup(html)
    table = soup.find('table', class_='simple-little-table financials')

    #Получаем информацию

    sales = getInfo.sales(table)  # выручка
    cogs = getInfo.cogs(table) #Себестоимость
    net_income = getInfo.net_income(table) #Чистая прибыль
    operating_expenses = getInfo.operating_expenses(table)  # Операционные расходы
    R_and_D = getInfo.R_and_D(table)  # НИОКР
    interest_expense = getInfo.interest_expense(table)  # Процентные расходы
    book_value = getInfo.book_value(table)  # Балансовая стоимость
    net_margin = getInfo.net_margin(table)  # Чистая рентабельность - (чист.прибыль/выручка)
    capex = getInfo.capex(table)  # CAPEX - капитальные расходы
    pe = getInfo.pe(table)  # P/E
    pbv = getInfo.pbv(table)  # P/BV
    price_action = getInfo.price_action(table) #Цена акции

    #Расчитываем остальную информацию на основе полученного

    gross_profit = cov.gross_profit(sales, cogs)

    #Вручную заносим информацию

    depreciation = ['', 125, 100, 113, 109]  # Армотизация
    sga = ['', 228, 256, 252, 245]  # sg&a
    operating_income = ['', 141, 136, 143, 191]  # Операционная прибыль
    sum_asset = ['', 198, 2145, 2266, 2409]  # итого активов
    dept = ['', 1231, 1292, 1302, 1351]  # Обязательства
    equity = ['', 752, 852, 964, 1057]  # Акционерный капитал

    # Место для корректировки

    gross_profit = sales

    #Расчитываем коэффициенты

    gross_margin = formulae.gross_margin(gross_profit, sales) #Валовая маржа
    k_sg_and_a = formulae.k_sg_and_a(sga, gross_profit) #Коэффициент SG&A от величины валовой прибыли
    k_depreciation = formulae.k_depreciation(depreciation, gross_profit) #Коэффициент амортизации от величины валовой прибыли
    k_net_income = formulae.k_net_income(net_income, gross_profit) #Отношение чистой прибыли к валовой
    k_interest_expense = formulae.k_interest_expense(interest_expense, operating_income) #Отношение процентных расходов к операционной прибыли
    k_capex = formulae.k_capex(capex, net_income) #Отношение CAPEX к чистой прибыли
    roa = formulae.roa(net_income, sum_asset) #Рентабельность активов (ROA)
    roe = formulae.roe(net_income, equity) #Рентабельность акционерного капитала (ROE)
    k_dept_and_equity = formulae.k_dept_and_equity(dept, equity) #Соотношение заёмных и собсвенных средств

    #Выводим информацию

    show.getShow(gross_margin, 'Валовая маржа')
    show.getShow(k_sg_and_a, 'Коэффициент SG&A от величины валовой прибыли')
    show.getShow(k_depreciation, 'Коэффициент амортизации от величины валовой')
    show.getShow(k_net_income, 'Отношение чистой прибыли к валовой')
    show.getShow(k_interest_expense, 'Отношение процентных расходов к операционной прибыли')
    show.getShow(k_capex, 'Отношение CAPEX к чистой прибыли')
    show.getShow(roa, 'Рентабельность активов (ROA)')
    show.getShow(roe, 'Рентабельность акционерного капитала (ROE)')
    show.getShow(k_dept_and_equity, 'Соотношение заёмных и собсвенных средств')
    show.getShow(pe,'Цена/прибыль (P/E)')
    show.getShow(pbv,'цена/Балансовая стоимость (P/BV)')

    #подводим оценку

if __name__ == '__main__':
    main()