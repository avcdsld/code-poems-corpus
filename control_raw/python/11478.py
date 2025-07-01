def QA_util_is_trade(date, code, client):
    """
    判断是否是交易日
    从数据库中查询
    :param date: str类型 -- 1999-12-11 这种格式    10位字符串
    :param code: str类型 -- 股票代码 例如 603658 ， 6位字符串
    :param client: pymongo.MongoClient类型    -- mongodb 数据库 从 QA_util_sql_mongo_setting 中 QA_util_sql_mongo_setting 获取
    :return:  Boolean -- 是否是交易时间
    """
    coll = client.quantaxis.stock_day
    date = str(date)[0:10]
    is_trade = coll.find_one({'code': code, 'date': date})
    try:
        len(is_trade)
        return True
    except:
        return False