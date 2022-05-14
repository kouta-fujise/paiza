# データ取得
ip = input().rstrip().split(" ")
# debug
# print(ip)

# 宣言
# カードの枚数
n = int(ip[0])
# 1セットの枚数
m = int(ip[1])
# シャッフルの回数
k = int(ip[2])
# シャッフル前の配列
c =[]
for i in range(n):
    # カードを保存
    c.append(i+1)
# シャッフル後の配列
s_c= []

# セット数
s = 0
# 割り切れるかどうか
mode = 0
# 余り
a = n % m
# 割り切れるなら
if a == 0:
    # 割った数がセット数
    s = int(n/m)
# 割り切れないなら
else:
    # 余を引いて割った値に１足した数がセット数
    s = int((n-(n%m))/m + 1)


# debug
# print(m)
# print(n)
# print(k)
# print(c)
# print(s)

# 関数

# 計算

# これをシャッフルの数繰り返す
for i in range(k):
    # シャッフルのたびにモードは初期化される
    if a == 0:
        mode = 0
    else:
        mode = 1
    # これをセットの数繰り返す
    for i in range(s):
        # 最後のセットから順に配列に入れていく
        # 捜査対象の数。
        # セットの個数から１引く。さらに繰り返した分だけ引く。そこにmをかけて1足す。
        # さらに配列のインデックスだから1引く
        num = (s-1-i)*m
        # mode0なら
        if mode == 0:
            for i in range(m):
                s_c.append(c[num+i])
        # mode1なら
        if mode == 1:
            # 余の回数操作して
            for i in range(a):
                s_c.append(c[num+i])
            # モードを0にする
            mode = 0
    # シャッフルのたびにcをs_cで置き換える
    c = s_c
    s_c = []

# 割り切れるなら最後のセットの最初の数から配列に入れていく
# 割り切れないなら余の数を配列に入れていく# 数がなくなるまで繰り返す


# 出力
for i in range(len(c)):
    print(c[i])
