# -*- coding: utf-8 -*-

from app import app

import psycopg2.pool

from flask import request
from flask import render_template
from flask import redirect


# Подключение к БД при первом обращении
@app.before_first_request
def activate_job():
    app.pool = psycopg2.pool.PersistentConnectionPool(
        #dsn='postgres://postgres:1qaz2wsx@/postgres?host=/cloudsql/activemanager:europe-west1:activity',
        #dsn='postgres://postgres:1qaz2wsx@104.155.115.32:5432/postgres',
        dsn='postgres://postgres:postgres@127.0.0.1:5432/postgres',
        minconn=8,
        maxconn=8)
    

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/game')
@app.route('/login')
@app.route('/activity')
@app.route('/account')
@app.route('/active')
def redirect_game():
    return redirect('/')

@app.route('/user-loads', methods=['POST'])
def user_loads():
    conn = app.pool.getconn()
    query = '''INSERT INTO "LoadStat"(
  "c.e",
  "c.tti.m",
  "rt.start",
  "rt.bmr",
  "rt.tstart",
  "rt.bstart",
  "rt.end",
  t_resp,
  t_page,
  t_done,
  t_other,
  "rt.tt",
  "rt.obo",
  "pt.fp",
  "pt.fcp",
  u,
  v,
  "rt.si",
  "rt.ss",
  "rt.sl",
  "vis.st",
  "ua.plt",
  "ua.vnd",
  pid,
  n,
  "c.tti.vr",
  "c.lt.n",
  "c.lt.tt",
  "c.lt",
  "c.f",
  "c.f.d",
  "c.f.m",
  "c.f.l",
  "c.f.s",
  sb,
  "User") values (
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::text,
  %s::integer)'''
    with conn.cursor() as curs:
        curs.execute(query,
                     (request.form.get('c.e', ''),
                      request.form.get('c.tti.m', ''),
                      request.form.get('rt.start', ''),
                      request.form.get('rt.bmr', ''),
                      request.form.get('rt.tstart', ''),
                      request.form.get('rt.bstart', ''),
                      request.form.get('rt.end', ''),
                      request.form.get('t_resp', ''),
                      request.form.get('t_page', ''),
                      request.form.get('t_done', ''),
                      request.form.get('t_other', ''),
                      request.form.get('rt.tt', ''),
                      request.form.get('rt.obo', ''),
                      request.form.get('pt.fp', ''),
                      request.form.get('pt.fcp', ''),
                      request.form.get('u', ''),
                      request.form.get('v', ''),
                      request.form.get('rt.si', ''),
                      request.form.get('rt.ss', ''),
                      request.form.get('rt.sl', ''),
                      request.form.get('vis.st', ''),
                      request.form.get('ua.plt', ''),
                      request.form.get('ua.vnd', ''),
                      request.form.get('pid', ''),
                      request.form.get('n', ''),
                      request.form.get('c.tti.vr', ''),
                      request.form.get('c.lt.n', ''),
                      request.form.get('c.lt.tt', ''),
                      request.form.get('c.lt', ''),
                      request.form.get('c.f', ''),
                      request.form.get('c.f.d', ''),
                      request.form.get('c.f.m', ''),
                      request.form.get('c.f.l', ''),
                      request.form.get('c.f.s', ''),
                      request.form.get('sb', ''),
                      request.form.get('User', None)
                      ))
    conn.commit()
    return 'true'
