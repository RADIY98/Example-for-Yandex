import json


def parsing_request_from(data):
    ''' Функция разбора с byte-ой строки'''
    my_json = data.decode('utf8').replace("'", "'")
    result = json.loads(my_json)
    return result
