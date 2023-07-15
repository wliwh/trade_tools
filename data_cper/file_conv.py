import markdown
import os
import pdfkit

os.chdir(os.path.dirname(__file__))

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']

    html = '''
    <html lang="zh-cn">
    <head>
    <meta content="text/html; charset=utf-8" http-equiv="content-type" />
    <link href="default.css" rel="stylesheet">
    <link href="github.css" rel="stylesheet">
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
               'minimum-font-size': "26",
               'enable-local-file-access': True}

    with open(hp,'a',encoding='utf-8') as hf:
        hf.write(md2html(mds))

    with open(hp,'r',encoding='utf-8') as hf:
        pdfkit.from_file(hf,pdfp,options=optionp,configuration=configp,css='../data_save/github.css')


markdown2pdf('../data_save/index_report.md')