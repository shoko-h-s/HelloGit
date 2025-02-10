n = int(input())  # ピラミッドのサイズ（n辺の長さ）を入力として受け取る

pyramid = []  # ピラミッドを格納する2次元リスト（リストのリスト）を初期化

for i in range(n):  # 0からn-1まで、n行のピラミッドを作るループ
    line = []  # i行目の行を表すリストを初期化

    for j in range(n):  # 0からn-1まで、i行目の各要素を埋めるループ
        left = j  # j列目の左側の距離
        right = n - (j+1)  # j列目の右側の距離
        top = i  # i行目の上側の距離
        bottom = n - (i+1)  # i行目の下側の距離

        d = min(left, right, top, bottom)  # 四方の距離のうち最小値を計算

        line.append(d+1)  # 最小値+1をi行目のj列目の要素として追加

    pyramid.append(line)  # 完成したi行目のリストをピラミッドに追加

# 完成したピラミッドを表示
for line in pyramid:
    print(line)
