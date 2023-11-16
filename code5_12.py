def input_scores(name):
    print(f"{name}さんの試験結果を入力して下さい")
    network = int(input("ネットワークの得点？ >>"))
    database = int(input("データベースの得点？ >>"))
    security = int(input("セキュリティの得点？ >>"))
    scores = [network, database, security]

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f"平均点は{avg}desu")

input_scores("浅木")
calc_average(scores)