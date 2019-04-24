from app import app
from flask import request, jsonify


@app.route('/get_pages', methods=['GET','POST'])
def get_pages():
    conn = None
    lst = ["name", "data"]
    data = []
    lst2=[]
    try:
        conn = app.pool.getconn()
        query = 'select page, count(page) from user_click group by page order by count(page) desc limit 5;'
        with conn.cursor() as curs:
            curs.execute(query)
            lst1 = curs.fetchall()
            for i in lst1:
                lst2.append(list(i))
            for i in lst2:
                i[1]=[i[1]]
            conn.commit()
            for i in lst2:
                data.append({key: value for key, value in zip(lst, i)})

    finally:
        if conn:
            app.pool.putconn(conn)
    return jsonify(data)
