def QA_fetch_lhb(date, db=DATABASE):
    '获取某一天龙虎榜数据'
    try:
        collections = db.lhb
        return pd.DataFrame([item for item in collections.find(
            {'date': date}, {"_id": 0})]).set_index('code', drop=False).sort_index()
    except Exception as e:
        raise e