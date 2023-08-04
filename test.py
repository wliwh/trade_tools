import datetime
import logging
import os
from data_cper import *
from common.trade_date import get_trade_day
from data_cper.file_conv import markdown2pdf, sendMail

logging.basicConfig(
    format='%(asctime)s [%(filename)s] - %(levelname)s: %(message)s',
    level=logging.INFO,
    filename='../trade_info.log',
    filemode='a')

Doc_Gen_Funs = [
    doc_qvix_day,
    doc_bsearch_info,
    doc_high_low_legu,
    doc_north_flow ]
    # docs_funds_amt]

Doc_Paras_List = [
    Qvix_Day_Texts,
    Bsearch_Pred_Texts,
    High_Low_Texts,
    North_Flow_Texts,
    # ETF_Amount_Texts,
    Second_Header,
    SZ50_Texts, HS300_Texts, ZZ500_Texts,
    CYB_Texts, KC_Texts,
    HSI_Texts, IXIC_Texts,
    RB0_Texts
]

Doc_Gen_Funs_Even = [
    doc_qvix_day,
    doc_high_low_legu,
]

Doc_Gen_Funs_Morn = [
    doc_bsearch_info,
    doc_north_flow
]

def basic_append_fun(fn,retry,**kwds):
    args, wsec = kwds.get('args',[]), kwds['words']
    args = args if isinstance(args,(list,tuple)) else [args]
    for r in range(retry):
        try:
            res = fn(*args)
            ks = 'ready' if res==0 else 'to '+res
            logging.info("Update {} {}.".format(wsec, ks))
            break
        except Exception as e:
            logging.warning("Try update {} {} times. ({})".format(wsec,r+1,e))
        if r==retry-1:
            logging.error("Can't update {}.".format(wsec))


def update_files(retry:int=3):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    if now_time[11:]>='21-20' and now_time[11:]<='23-50':
        download_type = 1
    elif now_time[11:]>='07-50' and now_time[11:]<='10-05':
        download_type = 2
    # 交易日 QVIX 分钟级数据
    if download_type==1:
        basic_append_fun(append_qvix_minute_file,retry,words='qvix minute')
    # ;; QVIX 数据
    # bdsearch 检索词数据
    if download_type==2:
        basic_append_fun(append_bsearch_day_file,retry,words='bdsearch day')
        basic_append_fun(append_bsearch_hour_file,retry,words='bdsearch hour')
    # ;; 北上资金
    # 延迟的两融数据
        basic_append_fun(append_margin_file,retry,args='sh',words='margin-sh')
        basic_append_fun(append_margin_file,retry,args='sz',words='margin-sz')
    # 交易日新高新低-乐股数据
    if download_type==1:
        basic_append_fun(append_high_low_legu_file,retry,words='high-low-legu')
    # 当日ETF成交数据
        for r in range(retry):
            try:
                tm_rg, res = append_funds_trade_file()
                ks = 'ready' if res==0 else 'to '+res
                tm_rg = '' if tm_rg==0 else ' '+tm_rg
                logging.info("Update{} etf amount {}.".format(tm_rg,ks))
                break
            except Exception as e:
                logging.warning("Try update etf amount {} times. ({})".format(r+1,e))
            if r==retry-1:
                logging.error("Can't update etf amount.")

def doc_file(paras:list):
    trade_date = get_trade_day(7).strftime('%Y-%m-%d')
    basic_doc = [Plain_Headers.format(now_date=trade_date)]
    all_doc_dics = dict()
    for d in Doc_Gen_Funs: all_doc_dics.update(d())
    for p in paras: basic_doc.append(p.format(**all_doc_dics))
    new_doc = ''.join(basic_doc)
    # new_doc.format(**all_doc_dics)
    fpth = os.path.join('..', 'data_save', 'index_report.md')
    with open(fpth,'w',encoding='utf-8') as f:
        f.write(new_doc)
    

if __name__=='__main__':
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    update_files()
    if now_time[11:]>='07-50' and now_time[11:]<='11-05':
        doc_file(Doc_Paras_List)
        doc_date = markdown2pdf('../data_save/index_report.md')
        sendMail('...','重要指数信息 '+doc_date,'../data_save/index_report.pdf','wljhwh@126.com')
    pass