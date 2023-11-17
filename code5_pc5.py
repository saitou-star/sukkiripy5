# 一人あたりの支払額は支払総額を参加人数で割った金額にする
# 支払いの単位は１００円とし、１００円未満の金額がある場合は切り上げる
# 支払額を超過した分は、幹事が受け取ることが出来る

# (1)
def int_input(amount, people):
    #計算データの入力
    amount = int(input("支払総額を入力して下さい >>"))
    people = int(input("参加人数を入力して下さい >>"))
    return amount, people

# (2)
def calc_payment(amount, people):
    # 割り勘の計算
    if people == "":
        people = 2
        dnum = amount / people
    dnum = amount / people   # 総額を人数で割る（端数も保持）
    pay = dnum // 100 * 100  # １００円未満を切り捨てる
    
    if dnum > pay:            # 元の値と比較して、
        pay = int(pay + 100)  # 小さければ１００円未満があったので上乗せ
    
    # 幹事の支払額の計算
    payorg = amount - pay * (people - 1)
    return pay, payorg, people

# (3)
def payment(pay, payorg, people):

    # 結果の表示
    print("*** 支払額 ***")
    print(f"一人当たり{pay}円({people - 1}人)、幹事は{payorg}円です")