import os,csv
import shutil
import re

class Main:
    def __init__(self):
        if os.path.exists("./magazines") == False:
            os.mkdir("./magazines")
    
        ########################################################################
        #65号以降の読み込み
        ########################################################################
        # csvファイルの読み込み
        csv_data = ReadCsv('sample.csv')
        data_list = csv_data.ReadCsv()
        # 1つの記事のフォルダを作成
        for article_data in data_list:
            make_folder = ArticleFolder(article_data)
            make_folder.MakeFolder()
        print("1step done")

        ########################################################################
        # 65号以前の読み込み
        ########################################################################
        # csvファイルの読み込み
        csv_data_2 = ReadCsv('sample2.csv')
        data_list_2 = csv_data_2.ReadCsv()
        # 1つの記事のフォルダを作成
        for article_data in data_list_2:
            make_folder_2 = ArticleFolder(article_data)
            make_folder_2.MakeFolder()

class ArticleFolder:
    def __init__(self,data):
        self.data = data
        self.folder_path = "./magazines/"+self.data[3][:-3]
        self.pdf_path = "./pdf/"+self.data[4]+"/"+self.data[3]

    def MakeFolder(self):
        # PDFファイルふぁ存在しなかった場合中断
        if os.path.exists(self.pdf_path) == False:
            return

        # 記事用のfolderが存在しなかった場合、新たにフォルダを作成
        if os.path.exists(self.folder_path) == False:
            os.mkdir(self.folder_path)
        
        # htmlファイルの作成
        html_maker = HtmlFile(self.data)
        html_maker.MakeHtml(self.folder_path+'/index.mdx')

        # PDFファイルのコピー
        copy_path=self.folder_path+"/"+self.data[3]
        shutil.copyfile(self.pdf_path,copy_path)

#もととなるcsvファイルの読み込み
class ReadCsv:
    data=[]

    def __init__(self,path):
        self.data_path = path
    def ReadCsv(self):
        #csvファイルを開く
        f=open(self.data_path, encoding="utf-8_sig")
        reader = csv.reader(f)

        for row in reader:
            self.data.append(row[0:7])
        return self.data

class HtmlFile:
    def __init__(self,data):
        self.data = data

    def MakeHtml(self,out_path):
        #もととなるhtmlファイルを開く
        #ここでは元のtxtファイルはbase.txt
        #ファイルはhtml(文字列)として格納
        html_path = 'base.txt'
        s = open(html_path,'r',encoding="utf-8_sig")
        html=s.read()

        #出力するファイルを開く
        #ここでは出力先のtxtファイルはhtml.txt
        out = open(out_path,'w', encoding="utf-8_sig")

        text=html
        text_mod = text.replace("要約",self.data[0])
        text_mod = text_mod.replace("題名",self.data[1])
        text_mod = text_mod.replace("教授名",self.data[2])
        text_mod = text_mod.replace("パス",self.data[3])
        text_mod = text_mod.replace("号数",self.data[4])
        text_mod = text_mod.replace("学院",self.data[5])
        print(text_mod, file=out)

if __name__ == '__main__':
    Main()