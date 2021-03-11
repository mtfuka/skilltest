import csv #TSVファイルを開くために、csvモジュールをインポート
#入力ファイル名は「input1.tsv」として、「1.py」と同じ階層に置いてください
with open('input1.tsv', mode='r', newline='', encoding='utf-8') as f: #読み込み用としてTSVファイル(input1.tsv)を開く
   tsv_reader = csv.reader(f, delimiter='\t') #データの読み込み
   data = [row for row in tsv_reader] #二次元リストとして取得

M = len(data[0]) #列数
N = len(data) #行数

#data[i][j]の中に':'が含まれていたら分割する
for i in range(N):
    for j in range(M):
        data[i][j]=data[i][j].split(':') #':'区切りで文字列を分割してリストに入れる

import copy #元のリストの値を保持しながらコピーするために、copyモジュールをインポート

list1 = copy.deepcopy(data) #dataをコピー
#複数の値が入っているdataから、複数の値を別々にしてlist1に収納
for i in range(N):
    for j in range(M):
        if(len(data[i][j])!=1): #要素数が1でない場合
            for k in range(len(data[i][j])): #以下、1行に複数の値が含まれるのは1列として考えている
                list1.append(copy.deepcopy(data[i])) #複数の値が含まれる行を末行に追加
                list1[-1][j]=copy.deepcopy(data[i][j][k]) #追加した行の要素数を1つに書き換える
                list1[i][0]="あ" #要素数を複数持つ列をマーク

list2 = [list1[i] for i in range(len(list1)) if not list1[i][0]=="あ"] #マークされている列以外を抽出して新しいリストを作成

#2次元リストに成型する
list3 = []
for i in range(len(list2)):
    sublist3 = []
    for j in range(M):
        if(type(list2[i][j])==list): #要素の型がリストになっている場合[]を外す
            sublist3.append(list2[i][j][0])
        else:
            sublist3.append(list2[i][j])
    list3.append(sublist3)

#TSVファイルで出力
with open('output1.tsv', mode='w', newline='', encoding='utf-8') as fo: #書き込み用としてTSVファイル(output1.tsv)を開く
    tsv_writer = csv.writer(fo, delimiter='\t') #データの書き込み
    tsv_writer.writerows(list3) #list3のデータを取得
print("output1.tsvが作成されました") #「out1.tsvが作成されました」と出力
