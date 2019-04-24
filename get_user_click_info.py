from app import app
from flask import request, jsonify


@app.route('/dima', methods=['GET','POST'])
def get_user_click_info():
    conn = None
    lst = ["user_name", "page", "res_time", "type_elem", "x", "y", "x_size", "y_size", "device", "class_elem"]
    data = []
    try:
        conn = app.pool.getconn()
        query = 'select user_name,page,res_time::text,type_elem,x,y,x_size,y_size,device,class_elem from user_click'
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
