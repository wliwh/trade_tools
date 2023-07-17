import markdown
import os
import pdfkit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

os.chdir(os.path.dirname(__file__))

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link type="text/css" href="C:/Users/84066/Documents/trade_tools/data_save/docs/default.css" rel="stylesheet">
    <link type="text/css" href="C:/Users/84066/Documents/trade_tools/data_save/docs/github.css" rel="stylesheet">
    </head>
    <body>
    %s
    </body>
    </html>
    '''

    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret


def markdown2pdf(mdp:str):
    with open(mdp,'r',encoding='utf-8') as mdf:
        mds = mdf.read()
    
    hp = os.path.splitext(mdp)[0]+'.html'
    pdfp = os.path.splitext(mdp)[0]+'.pdf'
    configp = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    optionp = {'encoding': 'utf-8',
            #    'page-size': 'A4',
            #    'dpi': '96',
               'minimum-font-size': "22",
               'enable-local-file-access': True}
    
    if os.path.exists(hp): os.remove(hp)
    if os.path.exists(pdfp): os.remove(pdfp)

    with open(hp,'a',encoding='utf-8') as hf:
        hf.write(md2html(mds))

    with open(hp,'r',encoding='utf-8') as hf:
        pdfkit.from_file(hf,pdfp,options=optionp,configuration=configp)


def sendMail(message,
             Subject,
             fpth,
             addrs2,
             sender_show='xxx',
             recipient_show='xxx',
             cc_show=''):
    '''
    :param message: str 邮件内容
    :param Subject: str 邮件主题描述
    :param sender_show: str 发件人显示，不起实际作用如："xxx"
    :param recipient_show: str 收件人显示，不起实际作用 多个收件人用','隔开如："xxx,xxxx"
    :param addrs2: str 实际收件人
    :param cc_show: str 抄送人显示，不起实际作用，多个抄送人用','隔开如："xxx,xxxx"
    '''
    # 填写真实的发邮件服务器用户名、密码
    user = 'wljhwh@126.com'
    password = 'VFICMOIDWUUFRCJM'
    # 邮件内容
    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'html', _charset="utf-8"))
    # 构造附件1，传送当前目录下的 test.txt 文件
    att = MIMEText(open(fpth, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 附件名称为中文时的写法
    # att.add_header("Content-Disposition", "attachment", filename=("gbk", "", filename))
    # 附件名称非中文时的写法,这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="{}"'.format('index-report.pdf')
    msg.attach(att)
    # 邮件主题描述
    msg["Subject"] = Subject
    # 发件人显示，不起实际作用
    msg["from"] = sender_show
    # 收件人显示，不起实际作用
    msg["to"] = recipient_show
    # 抄送人显示，不起实际作用
    msg["Cc"] = cc_show

    smtps = smtplib.SMTP()
    smtps.connect("smtp.126.com",port=25)
    # 登录发送邮件服务器
    smtps.login(user=user,password=password)
    # 实际发送、接收邮件配置
    smtps.sendmail(user, addrs2, msg=msg.as_string())
    smtps.close()

markdown2pdf('../data_save/index_report.md')
# sendMail('...','重要指数信息','../data_save/index_report.pdf','wljhwh@126.com')