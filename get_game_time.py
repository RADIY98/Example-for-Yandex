
from app import app
from flask import request, jsonify


@app.route('/get_game_time', methods=['GET', 'POST'])
def get_game_time():
    conn = None
    data=[]
    lst=["user_player","lvl","global_time","game_time"]
    try:
        conn = app.pool.getconn()
        query = 'select * from game_time gt order by gt.game_time limit 5;'
        with conn.cursor() as curs:
            curs.execute(query)
            lst1 = curs.fetchall()
            conn.commit()
            for i in lst1:
                data.append({key: value for key, value in zip(lst, i)})
    finally:
        if conn:
            app.pool.putconn(conn)
    return jsonify(data)
    # return json.dumps(data)
