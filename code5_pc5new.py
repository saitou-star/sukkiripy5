# (1)
def int_input(msg):
    return int(input(f"{msg}を入力して下さい"))

# (2)
def calc_payment(amount, people = 2):
    dnum = amount / people
    pay = dnum // 100 * 100
    if dnum > pay:
        pay = pay + 100
    payorg = amount - pay * (people - 1)

    return [int(pay), int(payorg)]

# (3)
def show_payment(pay, payorg, people = 2):
    print("*** 支払額 ***")
    print(f"一人当たり{pay}円({people - 1}人)、幹事は{payorg}円です")




# (1)
amount = int_input("支払総額")
people = int_input("参加人数")

# (2)
[pay, payorg] = calc_payment(amount, people)

# (3)
show_payment(pay, payorg, people)