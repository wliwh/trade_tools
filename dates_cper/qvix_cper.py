import sqlite3 as sq
import akshare as ak
import pandas as pd
import numpy as np
import datetime
import os

os.chdir(os.path.dirname(__file__))
sh_trade_date_list = ak.tool_trade_date_hist_sina()
today_date = datetime.datetime.now().date()
near_trade_date = sh_trade_date_list[sh_trade_date_list<=today_date].dropna().iloc[-1,0]
near_trade_date = near_trade_date.strftime('%Y-%m-%d')

def make_qvix_daily_db(cns, tb, nm: str):
    ''' 更新 qvix 日频数据
        cns: 打开的sql表
        tb: 下载好的qvix表格
        nm: 表格名称, 50或300 '''
    con = cns.cursor()
    names = con.execute('select name from sqlite_master')
    names = [n[0] for n in names.fetchall()]
    exit_db = 'QVIX{}_DAILY'.format(nm) in names
    if not exit_db:
        con.execute('''CREATE TABLE QVIX{}_DAILY
                    (ID     INTEGER PRIMARY KEY AUTOINCREMENT,
                    DT     DATE    NOT NULL,
                    OPEN   DOUBLE,
                    HIGH   DOUBLE,
                    LOW    DOUBLE,
                    CLOSE  DOUBLE);'''.format(nm))
    else:
        qdt = con.execute(
            'select * from QVIX{}_DAILY where ID=(select MAX(ID) from QVIX{}_DAILY)'.format(nm, nm))
        qdt = qdt.fetchall()[0][1]
        print("qvix_{} table closest day: {}".format(nm, qdt))
        tb = tb[tb['date'] > pd.to_datetime(qdt).date()]
    if tb.empty:
        return
    for k in tb.values:
        dt = k[0].strftime('%Y-%m-%d')
        con.execute("insert into QVIX{}_DAILY (DT,OPEN,HIGH,LOW,CLOSE) VALUES (?,?,?,?,?)".format(
            nm), (dt, k[1], k[2], k[3], k[4]))


def make_qvix_minute_db(cns, tb, nm: str):
    ''' 更新 qvix 分钟频数据
        cns: 打开的sql表
        tb: 下载好的qvix表格
        nm: 表格名称, 50或300 '''
    con = cns.cursor()
    names = con.execute('select name from sqlite_master')
    names = [n[0] for n in names.fetchall()]
    exit_db = 'QVIX{}_MIN'.format(nm) in names
    if not exit_db:
        con.execute('''create table QVIX{}_MIN
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     DT DATE NOT NULL,
                     TM TIME NOT NULL,
                     QVIX DOUBLE);'''.format(nm))
    else:
        qdt = con.execute(
            'select QVIX from QVIX{}_MIN where ID>=(select MAX(ID) from QVIX{}_MIN)-20'.format(nm, nm))
        qdt = np.array(qdt.fetchall())[:, 0]
        if all(qdt == tb.iloc[-21:, 1].values):
            print("qvix_{} trades date ready!".format(nm))
            return
    dtm = near_trade_date
    for k in tb.values:
        con.execute('insert into QVIX{}_MIN (DT,TM,QVIX) VALUES (?,?,?)'.format(
            nm), (dtm, k[0], k[1]))
    print("qvix_{} trades date ready ({}).".format(nm, dtm))


def db_update(tb, nm: str, freq: str = 'd'):
    etf_vix = tb
    etf_vix.dropna(inplace=True)
    db_fun_dict = {'d': make_qvix_daily_db, 'm': make_qvix_minute_db}
    conn = sq.connect('vix_daily.db')
    db_fun_dict[freq](conn, etf_vix, nm)
    conn.commit()
    conn.close()


def vix_update():
    ''' vix 数据更新 '''
    db_update(ak.option_50etf_qvix(), '50')
    db_update(ak.option_300etf_qvix(), '300')
    db_update(ak.option_50etf_min_qvix(), '50', 'm')
    db_update(ak.option_300etf_min_qvix(), '300', 'm')


# vix_update()