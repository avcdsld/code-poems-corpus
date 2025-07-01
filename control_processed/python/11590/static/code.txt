def QA_SU_save_future_day_all(engine, client=DATABASE):
    """save future_day_all

    Arguments:
        engine {[type]} -- [description]

    Keyword Arguments:
        client {[type]} -- [description] (default: {DATABASE})
    """

    engine = select_save_engine(engine)
    engine.QA_SU_save_future_day_all(client=client)