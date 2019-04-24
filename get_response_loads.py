import json
from app import app
from flask import request, jsonify


@app.route('/get_response_loads', methods=['GET','POST'])
def get_response_loads():
    conn = None
    data=[]
    lst=['location', 'user_name','device','load_time','time_ins']
    try:
        conn = app.pool.getconn()
        query = 'table loads_1'
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