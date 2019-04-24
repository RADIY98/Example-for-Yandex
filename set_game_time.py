import datetime

from app import app
from flask import request
from app import Parsing


@app.route('/set_game_time', methods=['POST','GET'])
def set_game_time():
    conn = None
    try:
        conn = app.pool.getconn()
        query = '''INSERT INTO "game_time"("user_player", "lvl", "global_time", "game_time")
        values (%s::text, %s::text, %s::timestamptz, %s::text) '''
        data = Parsing.parsing_request_from(request.data)
        with conn.cursor() as curs:
            curs.execute(query,
                         (data.get('user_name'),
                          data.get('lvl'),
                          data.get('global_time'),
                          data.get('game_time')))
        conn.commit()
    finally:
        if conn:
            app.pool.putconn(conn)
    return 'true'
