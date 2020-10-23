import logging


def log_debug(filename, class_name, method_name, parameters, return_value):
    logging.debug((str(filename), '.', str(class_name) + '.' + str(method_name) + ':CALL (' + str(parameters) + ')'))
    logging.debug((str(filename), '.', str(class_name) + '.' + str(method_name) + ':RETURN ' + str(return_value)))
