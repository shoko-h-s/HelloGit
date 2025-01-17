# 回文判定
s = input("回文判定を行う文字列を入力：")

# スライスで文字列を逆順にして、回文判定を行う
if s == s[::-1]:
    print("Yes")
else:
    print("No")
