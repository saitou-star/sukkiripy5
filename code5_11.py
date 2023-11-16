def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f"平均点は{avg}です")


scores = [4, 5, 1, 3, 1]
calc_average(scores)