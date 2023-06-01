import matplotlib.pyplot as plt
import mplfinance as mpf

_Mpf_Mark_Color = mpf.make_marketcolors(
    up="red",  # 上涨K线的颜色
    down="green",  # 下跌K线的颜色
    edge="black",  # 蜡烛图箱体的颜色
    volume="inherit",  # 成交量柱子的颜色
    wick="black"  # 蜡烛图影线的颜色
)

Mpf_Style = mpf.make_mpf_style(
    gridaxis='both',
    gridstyle='-.',
    y_on_right=False,
    marketcolors=_Mpf_Mark_Color,
    rc={'font.family': 'SimHei', 'axes.unicode_minus': 'False'}
    )

def mark_color_float(nums, color_pos:dict)->str:
    for conj, marks in color_pos.items():
        if conj(nums):
            return '**<font color="{}">{:.1f}</font>**'.format(marks,nums)
    return str(round(nums,1))

def M80_20(n):
    return mark_color_float(n,
        {lambda x:x>=80:"red",lambda x:x<=20:"green"})