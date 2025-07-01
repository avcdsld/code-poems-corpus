def QA_SU_save_stock_week(client=DATABASE, ui_log=None, ui_progress=None):
    """save stock_week

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    stock_list = QA_fetch_get_stock_list().code.unique().tolist()
    coll_stock_week = client.stock_week
    coll_stock_week.create_index(
        [("code",
          pymongo.ASCENDING),
         ("date_stamp",
          pymongo.ASCENDING)]
    )
    err = []

    def __saving_work(code, coll_stock_week):
        try:
            QA_util_log_info(
                '##JOB01 Now Saving STOCK_WEEK==== {}'.format(str(code)),
                ui_log=ui_log
            )

            ref = coll_stock_week.find({'code': str(code)[0:6]})
            end_date = str(now_time())[0:10]
            if ref.count() > 0:
                # 加入这个判断的原因是因为如果股票是刚上市的 数据库会没有数据 所以会有负索引问题出现

                start_date = ref[ref.count() - 1]['date']

                QA_util_log_info(
                    'UPDATE_STOCK_WEEK \n Trying updating {} from {} to {}'
                        .format(code,
                                start_date,
                                end_date),
                    ui_log=ui_log
                )
                if start_date != end_date:
                    coll_stock_week.insert_many(
                        QA_util_to_json_from_pandas(
                            QA_fetch_get_stock_day(
                                str(code),
                                QA_util_get_next_day(start_date),
                                end_date,
                                '00',
                                frequence='week'
                            )
                        )
                    )
            else:
                start_date = '1990-01-01'
                QA_util_log_info(
                    'UPDATE_STOCK_WEEK \n Trying updating {} from {} to {}'
                        .format(code,
                                start_date,
                                end_date),
                    ui_log=ui_log
                )
                if start_date != end_date:
                    coll_stock_week.insert_many(
                        QA_util_to_json_from_pandas(
                            QA_fetch_get_stock_day(
                                str(code),
                                start_date,
                                end_date,
                                '00',
                                frequence='week'
                            )
                        )
                    )
        except:
            err.append(str(code))

    for item in range(len(stock_list)):
        QA_util_log_info(
            'The {} of Total {}'.format(item,
                                        len(stock_list)),
            ui_log=ui_log
        )
        strProgress = 'DOWNLOAD PROGRESS {} '.format(
            str(float(item / len(stock_list) * 100))[0:4] + '%'
        )
        intProgress = int(float(item / len(stock_list) * 100))
        QA_util_log_info(
            strProgress,
            ui_log=ui_log,
            ui_progress=ui_progress,
            ui_progress_int_value=intProgress
        )

        __saving_work(stock_list[item], coll_stock_week)
    if len(err) < 1:
        QA_util_log_info('SUCCESS', ui_log=ui_log)
    else:
        QA_util_log_info(' ERROR CODE \n ', ui_log=ui_log)
        QA_util_log_info(err, ui_log=ui_log)