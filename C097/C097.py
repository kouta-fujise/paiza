# 宣言
# 人数
n = 0
# Aの当選
a = 0
# Bの当選
b = 0
# 当選結果
r = []

# データ取得
ip = input().rstrip().split(" ")
n = int(ip[0])
a = int(ip[1])
b = int(ip[2])

for i in range(n):
    r.append("N")

# print(n)
# print(a)
# print(b)
# print(r)

# 関数

# 計算

# nの中で、aの倍数の人にA,bの倍数の人にBをあげる
# 一旦全部にN入れて、倍数のところにA,B,ABを追加
# 逆に倍数から考える
# for i in range(大きめの数):
#   if iかけるAがn以下だった時
#       r[iかけるA]　= "A"
#   if iかけるBがn以下だった時
#       r[iかけるB]　= "B"
#   if iかけるABがn以下
#       r[iかけるAB]　= "AB"
# リストの0を考慮
# 公倍数が考慮されてない
#


for i in range(n):
    if (i+1) * a <= n:
        r[(i+1) * a-1] = "A"
for i in range(n):
    if (i+1) * b <= n:
        if r[(i+1) * b-1] == "A":
            r[(i+1) * b-1] = "AB"
        else:
            r[(i+1) * b-1] = "B"


# 出力
for i in range(len(r)):
    print(r[i])


# デバッグ
