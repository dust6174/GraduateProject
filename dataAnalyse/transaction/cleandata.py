if __name__ == "__main__":
    file_in = open("./transaction/transaction_bj.txt",'r',encoding='UTF-8')
    file_out = open("./transaction/transaction_bj2.txt",'w',encoding='UTF-8')
    lines = file_in.readlines()
    for line in lines:
        file_out.write(line.replace("暂无数据","0"))
    file_in.close()
    file_out.close()

