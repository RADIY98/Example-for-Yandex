import datetime
import json
from app import app
from flask import request
from app import Parsing
from flask import jsonify


@app.route('/get_uptime', methods=['POST'])
def get_location_loadtime_timeins():
    conn = None
    try:
        conn = app.pool.getconn()
        query = 'select location,load_time,time_ins::date from loads'
        with conn.cursor() as curs:
            curs.execute(query)
            temp = curs.fetchall()
            tm = []
            loc_load = ['name','data']
            loc_load[0] = temp[0][0]
            loc_load[1] = []
            for i in range(len(temp)):
                loc_load[1].append(temp[i][1])

            for i in temp:
                tm.append(str(i[2]))
        conn.commit()
    finally:
        if conn:
            app.pool.putconn(conn)
    return jsonify({'dates': tm, 'map': [{'name': loc_load[0], 'data': loc_load[1]}]})
