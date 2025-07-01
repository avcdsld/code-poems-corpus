def show_metrics(metrics, all_branches=False, all_tags=False):
    """
    Args:
        metrics (list): Where each element is either a `list`
            if an xpath was specified, otherwise a `str`
    """
    for branch, val in metrics.items():
        if all_branches or all_tags:
            logger.info("{branch}:".format(branch=branch))

        for fname, metric in val.items():
            lines = metric if type(metric) is list else metric.splitlines()

            if len(lines) > 1:
                logger.info("\t{fname}:".format(fname=fname))

                for line in lines:
                    logger.info("\t\t{content}".format(content=line))

            else:
                logger.info("\t{}: {}".format(fname, metric))