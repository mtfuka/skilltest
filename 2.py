import csv #TSVファイルを開くために、csvモジュールをインポート
#入力ファイル名は「input2.tsv」として、「2.py」と同じ階層に置いてください
with open('input2.tsv', mode='r', newline='', encoding='utf-8') as f: #読み込み用としてTSVファイル(input2.tsv)を開く
   tsv_reader = csv.reader(f, delimiter='\t') #データの読み込み
   data = [row for row in tsv_reader] #二次元リストとして取得

#同じキーを持つ値を連結
N = len(data) #行数
for i in range(N-1): #最終の2行の比較までなので、iは(行数-1)まで
    for j in range(i+1,N): #i列目とi列目以降の全ての列を比較
        if(data[i][0]==data[j][0]): #i列目とj列目のキーが同じ場合
            data[i][1]+=":"+data[j][1] #同じキーを持つ値を連結
            data[j][0]="あ" #結合に使った列をマーク

list = [data[i] for i in range(N) if not data[i][0]=="あ"] #マークされている列以外を抽出して新しいリストを作成

#TSVファイルで出力
with open('output2.tsv', mode='w', newline='', encoding='utf-8') as fo: #書き込み用としてTSVファイル(output2.tsv)を開く
    tsv_writer = csv.writer(fo, delimiter='\t') #データの書き込み
    tsv_writer.writerows(list) #listのデータを取得
print("output2.tsvが作成されました") #「out2.tsvが作成されました」と出力
