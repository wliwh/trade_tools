import configparser
from enum import Enum
import time
from typing import List, Dict, Tuple
from urllib.parse import urlencode, quote
from Crypto.Cipher import AES
from base64 import b64encode
import efinance as ef
import akshare as ak
import mplfinance as mpf
import datetime
import numpy as np
import requests
import json
import pandas as pd
import os
import sys
sys.path.append('..')
os.chdir(os.path.dirname(__file__))

from common.smooth_tool import log_min_max_dist_pd, smart_min_max_dist_pd
from common.mpf_set import Mpf_Style, M80_20
from common.trade_date import get_trade_list


Keyword_Index_Dic = {'股市':'ZZQZ','股票':'ZZQZ','a股':'SZZS',
    '上证':'SZZS','上证指数':'SZZS',
    '基金':'BK0536','牛市':'上证','熊市':'上证',
    '港股':'HSI','恒生指数':'HSI','恒生科技指数':'HSTECH',
    '美股行情':'IXIC','道琼斯指数':'DQS','纳斯达克指数':'IXIC','中概股':'PGJ',
    '上证50':'SZ50','沪深300':'HS300',
    '中证500':'ZZ500', '创业板指':'399006','科创50':'KC50',
    '螺纹钢':'RB0'}

Index_Plt_Dic = {'SZZS':['股市','股票','a股','上证','上证指数'],
                 'ZZQZ':['股市','股票','a股','上证','上证指数'],
                 '上证':['牛市','熊市'],
                 'HSI':['港股','恒生指数'],
                 'HSTECH':['恒生科技指数'],
                 'IXIC':['美股行情','道琼斯指数','纳斯达克指数'],
                #  'DQS':['美股行情','道琼斯指数','纳斯达克指数'],
                #  'PGJ':['中概股'],
                 'SZ50':['股市', '上证50'],
                 'HS300':['股市', '沪深300'],
                 'ZZ500':['股市', '中证500'],
                 '399006':['股市', '创业板指'],
                 'KC50':['股市', '科创50'],
                 'RB0':['螺纹钢']}


class ErrorCode(int, Enum):
    UNKNOWN = 10002
    NETWORK_ERROR = 10003

    # 百度指数
    NO_LOGIN = 20000
    KEYWORD_LIMITED = 20001
    REQUEST_LIMITED = 20002
    CHECK_KEYWORD_LIMITED = 20003

    # 百度的登录
    GET_QR_FAIL = 20010
    LOGIN_FAIL = 20011
    INDEX_LOGIN_FAIL = 20012


CODE_MSG_MAP = {
    ErrorCode.NO_LOGIN: 'cookies失效，请重新获取cookies',
    ErrorCode.UNKNOWN: '未知错误',
    ErrorCode.NETWORK_ERROR: '网络错误',
    ErrorCode.KEYWORD_LIMITED: ('关键词最多传递5个, '
                                '可以使用`from qdata.baidu_index.common import split_keywords`,'
                                '对关键词进行切分'),
    ErrorCode.REQUEST_LIMITED: "该账号请求过于频繁, 请降低请求频率",
    ErrorCode.CHECK_KEYWORD_LIMITED: "最多传入15个关键词",
    ErrorCode.GET_QR_FAIL: "获取二维码失败",
    ErrorCode.LOGIN_FAIL: "百度登录失败",
    ErrorCode.INDEX_LOGIN_FAIL: "百度指数登录失败"
}


class GopupError(Exception):
    def __init__(self, code: ErrorCode, info: str = ""):
        self.code = code
        self.msg = CODE_MSG_MAP.get(code) + (info and f", {info}")

    def __str__(self):
        return repr(f"ERROR-{self.code}: {self.msg}")
    

HEADERS = {
    'Host': 'index.baidu.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
}

ALL_KIND = ['all', 'pc', 'wise']


def decrypt_func(key: str, data: str) -> List[str]:
    """
        数据解密方法
    """
    a = key
    i = data
    n = {}
    s = []
    for o in range(len(a)//2):
        n[a[o]] = a[len(a)//2 + o]
    for r in range(len(data)):
        s.append(n[i[r]])
    return ''.join(s).split(',')


def http_get(url: str, cookies: str, cipher_text: str = "") -> str:
    """
        发送get请求, 程序中所有的get都是调这个方法
        如果想使用多cookies抓取, 和请求重试功能
        在这自己添加
    """
    _headers = HEADERS.copy()
    _headers['Cookie'] = cookies
    if cipher_text:
        _headers["Cipher-Text"] = cipher_text
    try:
        response = requests.get(url, headers=_headers, timeout=30)
    except requests.Timeout:
        raise GopupError(ErrorCode.NETWORK_ERROR)
    if response.status_code != 200:
        raise GopupError(ErrorCode.NETWORK_ERROR)
    return response.text


def get_cipher_text(keyword: str) -> str:
    byte_list = [
        b"\x00", b"\x01", b"\x02", b"\x03", b"\x04", b"\x05", b"\x06", b"\x07",
        b"\x08", b"\x09", b"\x0a", b"\x0b", b"\x0c", b"\x0d", b"\x0e", b"\x0f",
        b"\x10"
    ]
    # 这个数是从acs-2057.js里写死的，但这个脚本请求时代时间戳，不确定是不是一个动态变化的脚本
    start_time = 1652338834776
    end_time = int(datetime.datetime.now().timestamp()*1000)

    wait_encrypted_data = {
        "ua": HEADERS["User-Agent"],
        "url": quote(f"https://index.baidu.com/v2/main/index.html#/trend/{keyword}?words={keyword}"),
        "platform": "MacIntel",
        "clientTs": end_time,
        "version": "2.1.0"
    }
    password = b"yyqmyasygcwaiyaa"
    iv = b"1234567887654321"
    aes = AES.new(password, AES.MODE_CBC, iv)
    wait_encrypted_str = json.dumps(wait_encrypted_data).encode()
    filled_count = 16 - len(wait_encrypted_str) % 16
    wait_encrypted_str += byte_list[filled_count] * filled_count
    encrypted_str = aes.encrypt(wait_encrypted_str)
    cipher_text = f"{start_time}_{end_time}_{b64encode(encrypted_str).decode()}"
    return cipher_text


def get_encrypt_json(
    *,
    start_date: str,
    end_date: str,
    keywords: List[List[str]],
    type: str,
    area: int,
    cookies: str
) -> Dict:
    pre_url_map = {
        'search': 'http://index.baidu.com/api/SearchApi/index?',
        'live': 'http://index.baidu.com/api/LiveApi/getLive?',
        'news': 'http://index.baidu.com/api/NewsApi/getNewsIndex?',
        'feed': 'http://index.baidu.com/api/FeedSearchApi/getFeedIndex?'
    }

    pre_url = pre_url_map[type]
    word_list = [
        [{'name': keyword, 'wordType': 1} for keyword in keyword_list]
        for keyword_list in keywords
    ]
    if type == 'live':
        request_args = {
            'word': json.dumps(word_list),
            'region': area
        }
    else:
        request_args = {
            'word': json.dumps(word_list),
            'startDate': start_date,
            'endDate': end_date,
            'area': area
        }
    url = pre_url + urlencode(request_args)
    cipher_text = get_cipher_text(keywords[0][0])
    html = http_get(url, cookies, cipher_text=cipher_text)
    datas = json.loads(html)
    if datas['status'] == 10000:
        raise GopupError(ErrorCode.NO_LOGIN)
    if datas["status"] == 10001:
        raise GopupError(ErrorCode.REQUEST_LIMITED)
    if datas['status'] != 0:
        raise GopupError(ErrorCode.UNKNOWN, str(datas))
    return datas


def get_key(uniqid: str, cookies: str) -> str:
    url = 'http://index.baidu.com/Interface/api/ptbk?uniqid=%s' % uniqid
    html = http_get(url, cookies)
    datas = json.loads(html)
    key = datas['data']
    return key


def format_data(data: Dict, kind: str):
    """
        格式化堆在一起的数据
    """
    keyword = str(data['word'])
    start_date = datetime.datetime.strptime(data['all']['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['all']['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    # for kind in ALL_KIND:
    index_datas = data[kind]['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'type': kind,
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data


def format_data_feed(data: Dict):
    keyword = str(data['key'])
    start_date = datetime.datetime.strptime(data['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    index_datas = data['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data


def format_data_new(data: Dict):
    keyword = str(data['key'])
    start_date = datetime.datetime.strptime(data['startDate'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(data['endDate'], '%Y-%m-%d')
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date)
        start_date += datetime.timedelta(days=1)

    index_datas = data['data']
    for i, cur_date in enumerate(date_list):
        try:
            index_data = index_datas[i]
        except IndexError:
            index_data = ''
        formated_data = {
            'keyword': [keyword_info['name'] for keyword_info in json.loads(keyword.replace('\'', '"'))][0],
            'date': cur_date.strftime('%Y-%m-%d'),
            'index': index_data if index_data else '0'
        }
        yield formated_data


def baidu_search_index(word, start_date, end_date, cookie, type="all"):
    ''' 百度搜索数据 '''
    try:
        if isinstance(word,str):
            keywords_list = [[word]]
        elif isinstance(word,(List,Tuple)):
            keywords_list = [[x] for x in word]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='search',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['userIndexes']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data[type]['data'] = decrypt_func(key, encrypt_data[type]['data'])

            for formated_data in format_data(encrypt_data, kind=type):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        print(e)
        return None
    
def get_time_lst(tml:str)->List:
    st, ed = tml.split('|')
    sth, edh = int(st.split()[1][:2]), int(ed.split()[1][:2])
    stl = ['{} {:02d}:00:00'.format(st[:10],i) for i in range(sth,24)]
    edl = ['{} {:02d}:00:00'.format(ed[:10],i) for i in range(edh+1)]
    return stl+edl

def baidu_search_hour_index(word, cookie, kind="all"):
    try:
        if isinstance(word,str):
            keywords_list = [[word]]
        elif isinstance(word,(List,Tuple)):
            keywords_list = [[x] for x in word]
        encrypt_json = get_encrypt_json(
            start_date='000',
            end_date='000',
            keywords=keywords_list,
            type='live',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['result']
        uniqid = encrypt_json['data']['uniqid']
        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_all = decrypt_func(key, encrypt_data['index'][0]['_'+kind])
            time_lst = get_time_lst(encrypt_data['index'][0]['period'])
            cname = encrypt_data['key'][0]['name']
            result.append(pd.DataFrame({cname:encrypt_all},index=time_lst))
        return pd.concat(result, axis=1)
    except Exception as e:
        print(e)
        return None
    

def baidu_info_index(word, start_date, end_date, cookie):
    ''' 百度资讯指数 '''
    try:
        keywords_list = [[word]]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='feed',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['index']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data['data'] = decrypt_func(key, encrypt_data['data'])

            for formated_data in format_data_feed(encrypt_data):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        return None


def baidu_media_index(word, start_date, end_date, cookie):
    ''' 百度媒体指数 '''
    try:
        keywords_list = [[word]]
        encrypt_json = get_encrypt_json(
            start_date=start_date,
            end_date=end_date,
            keywords=keywords_list,
            type='news',
            area=0,
            cookies=cookie
        )

        encrypt_datas = encrypt_json['data']['index']
        uniqid = encrypt_json['data']['uniqid']

        result = []
        key = get_key(uniqid, cookie)
        for encrypt_data in encrypt_datas:
            encrypt_data['data'] = decrypt_func(key, encrypt_data['data'])

            for formated_data in format_data_new(encrypt_data):
                result.append(formated_data)
                # yield formated_data

        data_df = pd.DataFrame(result)
        data_df.index = pd.to_datetime(data_df["date"])
        del data_df["date"]
        return data_df
    except Exception as e:
        return None

def change_search_names_line(l,start_mark):
    l = l.strip()
    if start_mark is None:
        if ',' in l:
            name,date = l.split(',')
        else:
            name,date = l,'2011-01-01'
        name = name[1:] if name[0] in ('*','+','^') else name
    elif start_mark in ('*','+','^'):
        if ',' in l and l[0] not in ('*','+','^'):
            return
        l = l[1:] if l[0] in ('*','+','^') else l
        name, date = l.split(',') if ',' in l else (l, '2011-01-01')
    return (name.strip(), date.strip())

def get_bd_search_table(start_mark=None):
    ''' 生成待检索词列表 '''
    with open('../data_save/search_names', 'r', encoding='utf8') as f:
        name_lst = f.readlines()
    name_lst = [change_search_names_line(s,start_mark) for s in name_lst]
    return [n for n in name_lst if n is not None]

def _bd_search_tonow(cookie,sdate='2023-05-07',bsup='*'):
    now_date = sdate
    nml = get_bd_search_table(bsup)
    tbs = list()
    for nm,sd in nml:
        QS1 = pd.date_range(start=sd,end=now_date,freq='QS-JAN')
        QS2 = pd.date_range(start=sd,end=now_date,freq='Q-MAR')
        QS2 = QS2.append(pd.DatetimeIndex([now_date]))
        for d1,d2 in zip(QS1,QS2):
            time.sleep(0.2)
            dt1, dt2 = d1.strftime('%Y-%m-%d'), d2.strftime('%Y-%m-%d')
            print(nm,dt1,dt2,'...')
            tbs.append(baidu_search_index(nm,dt1,dt2,cookie))
    search_pd = pd.concat(tbs,axis=0)
    return search_pd


def bd_search_nearday(words, sd, ed, cookie):
    ''' 获取最近一段时间内关键词的检索量 '''
    bnear_tb = []
    btime = (len(words)+4)//5
    for i in range(btime):
        ed_i = None if i==btime-1 else i*5+5
        bnear_tb.append(baidu_search_index(words[slice(i*5,ed_i)], sd, ed, cookie))
    search_pd = pd.concat(bnear_tb, axis=0)
    recent_date = search_pd.index.max().strftime('%Y-%m-%d')
    return recent_date, search_pd

def bd_search_nearhour(words, cookie):
    ''' 获取小时级别的关键词检索量 '''
    bnear_tb = []
    btime = (len(words)+4)//5
    for i in range(btime):
        time.sleep(0.6)
        ed_i = None if i==btime-1 else i*5+5
        bnear_tb.append(baidu_search_hour_index(words[slice(i*5,ed_i)], cookie))
    search_pd = pd.concat(bnear_tb, axis=1)
    recent_time = search_pd.index.max()
    recent_day, recent_hour = recent_time.split()[0], recent_time.split(':')[0][-2:]
    return recent_day, recent_hour, search_pd


def append_bsearch_day_file(cfg_file=''):
    ''' 更新每日的关键词检索量
        不更新添加的检索词
    '''
    bsearch_words = [n[0] for n in get_bd_search_table()]
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'BSearch_Day'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get(cfg_sec, 'fpath'))
    cookpth = os.path.join('../data_save', '.cooks')
    with open(cookpth,'r') as ckf:
        cookie = ckf.read()
    up_date = config.get(cfg_sec, 'update_date')
    next_date = (pd.to_datetime(up_date) + pd.offsets.Day(1)).strftime('%Y-%m-%d')
    now_date = datetime.date.today().strftime('%Y-%m-%d')
    next_day = (pd.to_datetime(now_date) + pd.offsets.Day(1)).strftime('%Y-%m-%d')
    if now_date > next_date:
        bdt, bwd_tb = bd_search_nearday(bsearch_words, next_date, now_date, cookie.strip())
        bwd_tb.to_csv(fpth,mode='a',header=False)
        config.set(cfg_sec, 'update_date', bdt)
        config.set(cfg_sec, 'next_update', next_day)
        config.write(open(cfg_file,'w'))
        return bdt
    else:
        return 0

def append_bsearch_hour_file(cfg_file=''):
    ''' 更新检索词的小时频数据 '''
    bsearch_words = [n[0] for n in get_bd_search_table()]
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'BSearch_Hour'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    fpth = os.path.join('../data_save', config.get(cfg_sec, 'fpath'))
    cookpth = os.path.join('../data_save', '.cooks')
    with open(cookpth,'r') as ckf:
        cookie = ckf.read()
    up_date = config.get(cfg_sec, 'update_date')
    up_hour = config.get(cfg_sec, 'update_time')
    next_tm = (pd.to_datetime(up_date) + pd.offsets.Hour(int(up_hour)+10)).strftime('%Y-%m-%d %H')
    now_tm = datetime.datetime.today().strftime('%Y-%m-%d %H')
    next_day = (pd.to_datetime(now_tm) + pd.offsets.Hour(10)).strftime('%Y-%m-%d')
    # print(up_date+up_hour, next_tm, now_tm)
    if now_tm > next_tm:
        bdt, btm, bwd_tb = bd_search_nearhour(bsearch_words, cookie.strip())
        bwd_tb = bwd_tb[bwd_tb.index>up_date+' '+up_hour+':00:00']
        config.set(cfg_sec, 'update_date', bdt)
        config.set(cfg_sec, 'update_time', btm)
        config.set(cfg_sec, 'next_update', next_day)
        bwd_tb.to_csv(fpth, mode='a', header=False)
        config.write(open(cfg_file,'w'))
        return bdt + ' ' + btm
    else:
        return 0
    
def _get_bady_trade_day(fpth:str,tday_lst)->pd.DataFrame:
    bday_sor = pd.read_csv(fpth,index_col=0)
    bday_sor = bday_sor[bday_sor.index.map(lambda x:x in tday_lst)]
    bday_sor.sort_index(axis=0,inplace=True)
    return bday_sor
    
def _get_bwords_pd(sym:str, bday:pd.DataFrame, mday=400):
    ''' 重排检索词表格 '''
    sym_index = Keyword_Index_Dic[sym]
    inner_syms = Index_Plt_Dic[sym_index]
    qul = []
    for s in inner_syms:
        q = bday.loc[bday.keyword==s,'count']
        q.name = s
        qul.append(q)
    qpd = pd.concat(qul, axis=1)
    qpd.sort_index(axis=0,inplace=True)
    return qpd.tail(mday)

def _get_idx_ochl(idx_n:str,rng=None,
                  start:str='20220101')->pd.DataFrame:
    if 2<=len(idx_n)<=3 and idx_n[-1]=='0':
        index_cl = ak.futures_main_sina(idx_n,start_date=start)
        index_cl.rename(columns={'日期':'date','开盘价':'open','收盘价':'close', '最高价':'high', '最低价':'low', '成交量':'volume'},inplace=True)
    else:
        index_cl = ef.stock.get_quote_history(idx_n,beg=start)
        index_cl.rename(columns={'日期':'date','开盘':'open','收盘':'close', '最高':'high', '最低':'low', '成交量':'volume', '成交额':'amount'},inplace=True)
    index_cl.set_index('date',inplace=True)
    index_cl.index = pd.to_datetime(index_cl.index)
    if rng is not None:
        index_cl = index_cl[index_cl.index.map(lambda x:x.strftime('%Y-%m-%d') in rng)]
        index_cl.sort_index(axis=0,inplace=True)
    return index_cl
    
def make_bsearch_day_qu(winds, bdf:pd.DataFrame, is_norm:bool=True):
    ''' 对某几个关键词的历史分位 '''
    qut_l = [bdf]
    for w in winds:
        bper = log_min_max_dist_pd(bdf,w) if is_norm else smart_min_max_dist_pd(bdf,w,fn=np.log)
        bper.rename(columns=lambda x:x+'_'+str(w),inplace=True)
        qut_l.append(bper)
    return pd.concat(qut_l,axis=1)

def make_bsearch_day_tline(sym:str, winds, bqut:dict):
    ''' 输出一组关键词的列表 '''
    inner_syms = Index_Plt_Dic[Keyword_Index_Dic[sym]]
    bsets = list()
    for s in inner_syms:
        bper = '1. {:6s}\t{:6d}'.format(s+':',int(bqut[s]))
        bsr = ','.join([M80_20(bqut[s+'_'+str(w)]) for w in winds])
        bsets.append(bper+' ('+bsr+')')
    return '\n'.join(bsets) if len(bsets)>1 else bsets[0][3:]

def make_bsearch_day_plt(sym:str,fpth:str,idx_pd:pd.DataFrame,bpd:pd.DataFrame,bqut:pd.DataFrame,wind:int):
    ''' 根据检索量绘图 
        sym: 指数名称
        fpth: 设定保存图片的地址
        inx_pd: 指数每日行情
        bpd: 检索量
        bqut: 检索量分位数
        wind: 计算分位数所用时间窗口'''
    idx_n = Keyword_Index_Dic[sym]
    index_cl = idx_pd.tail(75)
    bpd_n = bpd.tail(75)
    bqut_n = bqut.tail(75)
    xadd_plots = []
    for i,s in enumerate(Index_Plt_Dic[idx_n]):
        xadd_plots.extend([
            mpf.make_addplot(bpd_n[s],type='bar',panel=i+1,width=0.7, color='darkgray',secondary_y=False,ylabel='{}({})'.format(s,wind)),
            mpf.make_addplot(bqut_n[s+'_'+str(wind)],panel=i+1,linewidths=0.7, color='tomato',secondary_y=True)
        ])
    mpf.plot(index_cl,type='candle',ylabel=idx_n,
             style=Mpf_Style, addplot=xadd_plots,
             datetime_format='%m-%d',xrotation=15,
             savefig={'fname':fpth,'dpi':400,'bbox_inches':'tight'},
             figratio=(6,6),figscale=1.5)


def doc_bsearch_info(cfg_file=''):
    ''' 填写 检索量 数据 '''
    if not cfg_file:
        cfg_file = '../trade.ini'
    cfg_sec = 'BSearch_Day'
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding='utf-8')
    up_date = config.get(cfg_sec, 'update_date')
    main_plt_idx = config.get(cfg_sec, 'bsearch_day_main_idx')
    main_period = int(config.get(cfg_sec, 'bsearch_day_main_periods'))
    all_periods = config.get(cfg_sec, 'bsearch_day_periods')
    all_prds = [int(a.strip()) for a in all_periods.split(',')]
    assert main_period in all_prds, "分位数周期配置有误."

    bday_doc_dic = dict(bsearch_day_periods=all_periods,bsearch_day_date=up_date)
    fpth = os.path.join('../data_save', config.get(cfg_sec, 'fpath'))
    _base_idx = [d.strftime('%Y-%m-%d') for d in _get_idx_ochl(main_plt_idx).index]
    bday_main_pd = _get_bady_trade_day(fpth,_base_idx)
    bday_sym_set = set()
    for s in Keyword_Index_Dic.keys():
        ## TODO: 牛熊的别名
        idx_name, idx_sig = Keyword_Index_Dic[s], None
        if idx_name == '上证': 
            idx_sig = 'cowbear'
        if not Index_Plt_Dic.get(idx_name):
            continue
        if idx_name in bday_sym_set:
            continue
        idx_cl = _get_idx_ochl(idx_name,set(bday_main_pd.index))
        idx_nname = idx_name if idx_sig is None else idx_sig
        img_pth = os.path.join('../data_save', config.get('Basic_Info','doc_img_pth'),'bday_{}.png'.format(idx_nname))
        bday_pd = _get_bwords_pd(s,bday_main_pd,500)
        if idx_nname in ('HSTECH','IXIC','PGJ'):
            bday_qut = make_bsearch_day_qu(all_prds,bday_pd,False)
        else:
            bday_qut = make_bsearch_day_qu(all_prds,bday_pd,True)
        bday_stas = make_bsearch_day_tline(s,all_prds,dict(bday_qut.iloc[-1]))
        make_bsearch_day_plt(s,img_pth,idx_cl,bday_pd,bday_qut,main_period)
        bday_doc_dic.update({
            'bsearch_day_{}_tlst'.format(idx_nname):bday_stas,
            'bsearch_day_{}_ppth'.format(idx_nname):os.path.abspath(img_pth)
        })
        bday_sym_set.add(idx_name)
    bday_doc_dic['bsearch_day_main_tlst'] = bday_doc_dic['bsearch_day_{}_tlst'.format(main_plt_idx)]
    bday_doc_dic['bsearch_day_main_ppth'] = bday_doc_dic['bsearch_day_{}_ppth'.format(main_plt_idx)]
    return bday_doc_dic

if __name__=='__main__':
    # append_bsearch_day_file()
    # append_bsearch_hour_file()
    kk = doc_bsearch_info()
    print(kk)
    pass
