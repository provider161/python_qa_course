import logging


def create_log():

    # create a logger
    logger = logging.getLogger('browser')
    logger.setLevel(logging.INFO)

    # create log-handlers
    handler_critical = logging.FileHandler(filename='logs/critical.log', mode='a')
    handler_critical.setLevel(logging.WARNING)
    handler_error = logging.FileHandler(filename='logs/error.log', mode='a')
    handler_error.setLevel(logging.ERROR)
    handler_info = logging.StreamHandler()
    handler_info.setLevel(logging.INFO)

    # formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler_critical.setFormatter(formatter)
    handler_info.setFormatter(formatter)
    handler_error.setFormatter(formatter)

    # add the handlers
    logger.addHandler(handler_info)
    logger.addHandler(handler_critical)
    logger.addHandler(handler_error)

    return logger
