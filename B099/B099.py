# 宣言
# 道の本数
n = 0
# 降水量のライン
m = 0
# 地図
# 多次元配列で入れる
# 例えば一番左のルートはmp[0][i]になる
mp_all = []
mp_part = []
mp = []

result = []
# debug

# データ取得
ip = input().rstrip().split(" ")
n = int(ip[0])
m = int(ip[1])

# ルート分繰り返す
for i in range(n):
    ip = input().rstrip().split(" ")
    # ルートの情報を全て入れる
    for i in range(n):
        mp_all.append(int(ip[i]))

# mp_allからmpに多次元配列化する
for j in range(n):
    mp_part = []
    for i in range(n):
        # print(i)
        mp_part.append(mp_all[i*n + j])
    mp.append(mp_part)


# debug

# print(n)
# print(m)
# print(mp_all)
# print(mp_part)
# print(mp)

# 関数

# その道が通れるかどうかチェック
# xは1-n
def can_pass(x):
    # その道の全てのますで降水量がオーバーしないかチェック
    for i in range(n):
        # mを超えていたら
        if mp[x-1][i] >= m:
            # 通れない
            # print("通れない")
            return
    # print("通れる")
    result.append(x)
    return x

# debug

# 計算

# debug

# 出力
# 全てNoneだった場合はwait
for i in range(n):
    can_pass(i+1)

if result == []:
    print("wait")
else:
    print(*result)

# debug
