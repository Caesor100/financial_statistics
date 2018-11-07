def gross_profit(sales, cogs):
    result = []
    i = 0
    for a in sales:
        try:
            if (a - cogs[i]) > 0:
                result.append(float("%.2f" % (a - cogs[i])))
            if (a - cogs[i]) > 100:
                result.append(round((a - cogs[i])))
            if (a - cogs[i]) <= 0:
                result.append(float("%.4f" % (a - cogs[i])))
        except TypeError:
            result.append('')
        i = i + 1
    return result