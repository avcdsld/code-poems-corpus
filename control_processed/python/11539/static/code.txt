def QA_fetch_get_option_contract_time_to_market():
    '''
    #🛠todo 获取期权合约的上市日期 ？ 暂时没有。
    :return: list Series
    '''
    result = QA_fetch_get_option_list('tdx')
    # pprint.pprint(result)
    #  category  market code name desc  code
    '''
    fix here : 
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
    result['meaningful_name'] = None
    C:\work_new\QUANTAXIS\QUANTAXIS\QAFetch\QATdx.py:1468: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    '''
    # df = pd.DataFrame()
    rows = []

    result['meaningful_name'] = None
    for idx in result.index:
        # pprint.pprint((idx))
        strCategory = result.loc[idx, "category"]
        strMarket = result.loc[idx, "market"]
        strCode = result.loc[idx, "code"]  # 10001215
        strName = result.loc[idx, 'name']  # 510050C9M03200
        strDesc = result.loc[idx, 'desc']  # 10001215

        if strName.startswith("510050"):
            # print(strCategory,' ', strMarket, ' ', strCode, ' ', strName, ' ', strDesc, )

            if strName.startswith("510050C"):
                putcall = '50ETF,认购期权'
            elif strName.startswith("510050P"):
                putcall = '50ETF,认沽期权'
            else:
                putcall = "Unkown code name ： " + strName

            expireMonth = strName[7:8]
            if expireMonth == 'A':
                expireMonth = "10月"
            elif expireMonth == 'B':
                expireMonth = "11月"
            elif expireMonth == 'C':
                expireMonth = "12月"
            else:
                expireMonth = expireMonth + '月'

            # 第12位期初设为“M”，并根据合约调整次数按照“A”至“Z”依序变更，如变更为“A”表示期权合约发生首次调整，变更为“B”表示期权合约发生第二次调整，依此类推；
            # fix here : M ??
            if strName[8:9] == "M":
                adjust = "未调整"
            elif strName[8:9] == 'A':
                adjust = " 第1次调整"
            elif strName[8:9] == 'B':
                adjust = " 第2调整"
            elif strName[8:9] == 'C':
                adjust = " 第3次调整"
            elif strName[8:9] == 'D':
                adjust = " 第4次调整"
            elif strName[8:9] == 'E':
                adjust = " 第5次调整"
            elif strName[8:9] == 'F':
                adjust = " 第6次调整"
            elif strName[8:9] == 'G':
                adjust = " 第7次调整"
            elif strName[8:9] == 'H':
                adjust = " 第8次调整"
            elif strName[8:9] == 'I':
                adjust = " 第9次调整"
            elif strName[8:9] == 'J':
                adjust = " 第10次调整"
            else:
                adjust = " 第10次以上的调整，调整代码 %s" + strName[8:9]

            executePrice = strName[9:]
            result.loc[idx, 'meaningful_name'] = '%s,到期月份:%s,%s,行权价:%s' % (
                putcall, expireMonth, adjust, executePrice)

            row = result.loc[idx]
            rows.append(row)

        elif strName.startswith("SR"):
            # print("SR")
            # SR1903-P-6500
            expireYear = strName[2:4]
            expireMonth = strName[4:6]

            put_or_call = strName[7:8]
            if put_or_call == "P":
                putcall = "白糖,认沽期权"
            elif put_or_call == "C":
                putcall = "白糖,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[9:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass
        elif strName.startswith("CU"):
            # print("CU")

            # print("SR")
            # SR1903-P-6500
            expireYear = strName[2:4]
            expireMonth = strName[4:6]

            put_or_call = strName[7:8]
            if put_or_call == "P":
                putcall = "铜,认沽期权"
            elif put_or_call == "C":
                putcall = "铜,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[9:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass
        # todo 新增期权品种 棉花，玉米， 天然橡胶
        elif strName.startswith("RU"):
            # print("M")
            # print(strName)
            ##
            expireYear = strName[2:4]
            expireMonth = strName[4:6]

            put_or_call = strName[7:8]
            if put_or_call == "P":
                putcall = "天然橡胶,认沽期权"
            elif put_or_call == "C":
                putcall = "天然橡胶,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[9:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass

        elif strName.startswith("CF"):
            # print("M")
            # print(strName)
            ##
            expireYear = strName[2:4]
            expireMonth = strName[4:6]

            put_or_call = strName[7:8]
            if put_or_call == "P":
                putcall = "棉花,认沽期权"
            elif put_or_call == "C":
                putcall = "棉花,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[9:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass

        elif strName.startswith("M"):
            # print("M")
            # print(strName)
            ##
            expireYear = strName[1:3]
            expireMonth = strName[3:5]

            put_or_call = strName[6:7]
            if put_or_call == "P":
                putcall = "豆粕,认沽期权"
            elif put_or_call == "C":
                putcall = "豆粕,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[8:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass
        elif strName.startswith("C") and strName[1] != 'F' and strName[1] != 'U':
            # print("M")
            # print(strName)
            ##
            expireYear = strName[1:3]
            expireMonth = strName[3:5]

            put_or_call = strName[6:7]
            if put_or_call == "P":
                putcall = "玉米,认沽期权"
            elif put_or_call == "C":
                putcall = "玉米,认购期权"
            else:
                putcall = "Unkown code name ： " + strName

            executePrice = strName[8:]
            result.loc[idx, 'meaningful_name'] = '%s,到期年月份:%s%s,行权价:%s' % (
                putcall, expireYear, expireMonth, executePrice)

            row = result.loc[idx]
            rows.append(row)

            pass
        else:
            print("未知类型合约")
            print(strName)

    return rows