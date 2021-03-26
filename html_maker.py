#モジュールの準備
import csv
data=[]

#もととなるhtmlファイルを開く
#ここでは元のtxtファイルはbase.txt
#ファイルはhtml(文字列)として格納
html_path = 'base.txt'
s = open(html_path,'r',encoding="utf-8_sig")
html=s.read()

#出力するファイルを開く
#ここでは出力先のtxtファイルはhtml.txt
out_path = 'html.txt'
out = open(out_path,'w', encoding="utf-8_sig")

#csvファイルを開く
#ここでは読み込むcsvファイルはsample.txt
data_path='sample.csv'
f=open('sample.csv', encoding="utf-8_sig")
reader = csv.reader(f)
#必要な部分だけを切り取ったdataリストを作る    
for row in reader:
    data.append(row[0:6])

for test in data:
    text=html
    text_mod = text.replace("要約",test[0])
    text_mod = text_mod.replace("題名",test[1])
    text_mod = text_mod.replace("教授名",test[2])
    text_mod = text_mod.replace("パス",test[3])
    text_mod = text_mod.replace("号数",test[4])
    text_mod = text_mod.replace("学院",test[5])
    text_mod = text_mod.replace("研究室のURL",test[6])
    print(text_mod, file=out)