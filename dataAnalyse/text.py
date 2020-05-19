if __name__ == "__main__":
    with open('transaction_gz.txt', 'r',encoding="utf-8") as f:
        s = f.readline()
    infos = s.replace(" ","").split("|")
    print(infos)
    for info in infos:
        print(info )