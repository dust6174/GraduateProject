import re
if __name__ == "__main__":
    # with open('transaction_gz.txt', 'r',encoding="utf-8") as f:
    #     s = f.readline()
    # infos = s.replace(" ","").split("|")
    # print(re.findall(r"\d+",infos[10])[0])
    # print(infos[10])

    file_out = open("./gz/result_gz_type.txt", 'a')
    file_out.write("hello~")
    file_out.close()