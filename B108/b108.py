# 宣言
# ゴンドラ
gn = []
# グループ
gr = []
# ゴンドラのカウント
c = []
# 今のゴンドラ
now_gn = 0
# 今のグループ
now_gr = 0

# データの取得
ip = input().rstrip().split(" ")

# ゴンドラの取得
for i in range(int(ip[0])):
    gn.append(int(input()))
    c.append(0)

# グループん取得
for i in range(int(ip[1])):
    gr.append(int(input()))

# データの確認
# print(gn)
# print(c)
# print(gr)


# ゴンドラを回す
def move_gn():
    global now_gn
    if now_gn < len(gn)-1:
        now_gn += 1
    else:
        now_gn = 0

# 計算
while True:
    # デバッグ
    # print("now_gn")
    # print(now_gn)
    # print("now_gr")
    # print(now_gr)
    # グループがなくなれば終了
    if now_gr > len(gr)-1:
        break
    # ゴンドラが大きければ
    if gn[now_gn] >= gr[now_gr]:
        # カウントして
        c[now_gn] += gr[now_gr]
        # 次のゴンドラとグループに行く
        move_gn()
        now_gr += 1
    # ゴンドラが小さければ
    else:
        # ゴンドラにマックス入れて
        c[now_gn] += gn[now_gn]
        # グループを減らして
        gr[now_gr] -= gn[now_gn]
        # 次のゴンドラにいく
        move_gn()

# 出力
for i in range(len(gn)):
    print(c[i])
