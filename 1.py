import csv #csvモジュールをインポート
#「ファイル名を入力してください」と出力してファイル名を入力した方が良さそう、下の'in.tsv'もinput()などに変える
with open('in1.tsv', mode='r', newline='', encoding='utf-8') as f: #読み込み用としてTSVファイルを開く
   tsv_reader = csv.reader(f, delimiter='\t') #データの読み込み
   data = [row for row in tsv_reader] #二次元リストとして取得

M = len(data[0]) #列数
N = len(data) #行数

#data[i][j]の中に:が含まれていたら分割して新しいリストに入れる
for i in range(N):
    for j in range(M):
        data[i][j]=data[i][j].split(':') #':'区切りで文字列を分割

import copy #元のリストの値を保持しながらコピーするために、copyモジュールをインポート

list1 = copy.deepcopy(data) #複数の値が入っているdataから、複数の値を別々に収納するためのlist1を作成

for i in range(N):
    for j in range(M):
        if(len(data[i][j])!=1): #要素数が1でなかったら
            for k in range(len(data[i][j])): #以下、行に複数の値が含まれるのは1列として考えている
                list1.append(copy.deepcopy(data[i])) #i行目のリストを末行に追加
                list1[-1][j]=copy.deepcopy(data[i][j][k]) #追加したリストの要素数を1つに書き換える
                list1[i][0]="@" #要素数を複数持つ列をマーク

list2 = [list1[i] for i in range(len(list1)) if not list1[i][0]=="@"] #マークされている列以外を抽出して新しいリストを作成

#2次元リストに成型する
out = []
for i in range(len(list2)):
    subout = []
    for j in range(M):
        if(type(list2[i][j])==list): #要素の型がリストになっている場合[]を外す
            subout.append(list2[i][j][0])
        else:
            subout.append(list2[i][j])
    out.append(subout)

#ファイルで出力する場合
with open('out1.tsv', mode='w', newline='', encoding='utf-8') as fo: #書き込み用としてTSVファイルを開く
    tsv_writer = csv.writer(fo, delimiter='\t') #データの書き込み
    tsv_writer.writerows(out)
#「out1.tsvが作成されました」と出力

#標準出力で出力する場合
for i in out:
    print(*i, sep='\t')

#python 1.py 実行するためのコマンド
