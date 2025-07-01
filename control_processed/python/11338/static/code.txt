def QA_SU_save_stock_day(client=DATABASE, ui_log=None, ui_progress=None):
    '''
     save stock_day
    保存日线数据
    :param client:
    :param ui_log:  给GUI qt 界面使用
    :param ui_progress: 给GUI qt 界面使用
    :param ui_progress_int_value: 给GUI qt 界面使用
    '''
    stock_list = QA_fetch_get_stock_list().code.unique().tolist()
    coll_stock_day = client.stock_day
    coll_stock_day.create_index(
        [("code",
          pymongo.ASCENDING),
         ("date_stamp",
          pymongo.ASCENDING)]
    )
    err = []

    # saveing result

    def __gen_param(stock_list, coll_stock_day, ip_list=[]):
        results = []
        count = len(ip_list)
        total = len(stock_list)
        for item in range(len(stock_list)):
            try:
                code = stock_list[item]
                QA_util_log_info(
                    '##JOB01 Now Saving STOCK_DAY==== {}'.format(str(code)),
                    ui_log
                )

                # 首选查找数据库 是否 有 这个代码的数据
                search_cond = {'code': str(code)[0:6]}
                ref = coll_stock_day.find(search_cond)
                end_date = str(now_time())[0:10]
                ref_count = coll_stock_day.count_documents(search_cond)

                # 当前数据库已经包含了这个代码的数据， 继续增量更新
                # 加入这个判断的原因是因为如果股票是刚上市的 数据库会没有数据 所以会有负索引问题出现
                if ref_count > 0:
                    # 接着上次获取的日期继续更新
                    start_date = ref[ref_count - 1]['date']
                    # print("ref[ref.count() - 1]['date'] {} {}".format(ref.count(), coll_stock_day.count_documents({'code': str(code)[0:6]})))
                else:
                    # 当前数据库中没有这个代码的股票数据， 从1990-01-01 开始下载所有的数据
                    start_date = '1990-01-01'
                QA_util_log_info(
                    'UPDATE_STOCK_DAY \n Trying updating {} from {} to {}'
                        .format(code,
                                start_date,
                                end_date),
                    ui_log
                )
                if start_date != end_date:
                    # 更新过的，不更新
                    results.extend([(code, start_date, end_date, '00', 'day', ip_list[item % count]['ip'],
                                     ip_list[item % count]['port'], item, total, ui_log, ui_progress)])
            except Exception as error0:
                print('Exception:{}'.format(error0))
                err.append(code)
        return results

    ips = get_ip_list_by_multi_process_ping(stock_ip_list, _type='stock')[:cpu_count() * 2 + 1]
    param = __gen_param(stock_list, coll_stock_day, ips)
    ps = QA_SU_save_stock_day_parallelism(processes=cpu_count() if len(ips) >= cpu_count() else len(ips),
                                          client=client, ui_log=ui_log)
    ps.add(do_saving_work, param)
    ps.run()

    if len(err) < 1:
        QA_util_log_info('SUCCESS save stock day ^_^', ui_log)
    else:
        QA_util_log_info('ERROR CODE \n ', ui_log)
        QA_util_log_info(err, ui_log)