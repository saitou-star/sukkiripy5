# (1) def weather():  ,なし
# (2) def calc_circle_area(radius):  ,float
# (3) def nowstr(): ,str
# (4) def nowint(): ,リスト・タプル・ディクショナリ
# (5) def is_leapyear(Western calendar): ,bool


# 5-2
def is_leapyear(year):
    return (year % 100 == 0 and year != 400)

year = int(input("現在の西暦を入力 >>"))

if is_leapyear(year):
    print(f"西暦{year}は、うるう年ではありません。")

else:
    print(f"西暦{year}は、うるう年です。")
