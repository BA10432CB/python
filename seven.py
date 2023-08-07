#7以上7777777以下の7の倍数を全て書き出したとき、数字「7」は何回現れるか。
seven_total = 0

for i in range(1, 1111112):
    # seven_multiple = i * 7
    # seven_total += seven_multiple
    seven_multiple = str(i * 7)
    seven_total += seven_multiple.count('7')

print(seven_total)