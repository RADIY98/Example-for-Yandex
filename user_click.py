import datetime

from app import app
from flask import request
from app import Parsing


@app.route('/user_click', methods=['POST', 'GET'])
def user_click():
    conn = None
    try:
        conn = app.pool.getconn()
        query = '''INSERT INTO "user_click"("user_name", "page", "res_time", "device", "type_elem", "class_elem",
        "x", "y", "x_size", "y_size","browser")
        values (%s::text, %s::text, %s::timestamptz, %s::text, %s::text, %s::text, %s::integer, %s::integer,
        %s::integer, %s::integer, %s::text) '''
        data = Parsing.parsing_request_from(request.data)
        with conn.cursor() as curs:
            curs.execute(query,
                         (data.get('user'),
                          data.get('location'),
                          data.get('time'),
                          data.get('device'),
                          data.get('data').get('class_list'),
                          data.get('data').get('element_type'),
                          data.get('data').get('x'),
                          data.get('data').get('y'),
                          data.get('data').get('screen_x'),
                          data.get('data').get('screen_y'),
                          data.get('browser')
                          ))
        conn.commit()
    finally:
        if conn:
            app.pool.putconn(conn)
    return 'true'
