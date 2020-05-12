if __name__ == '__main__':
    base_path = "H:/codes/graduateProject/data/source/microdistrict/"
    f_origin = open(base_path+'microdistrict_bj.txt','r')
    microdistrict_list = f_origin.readlines()
    microdistrict_num = len(microdistrict_list)
    split_num = microdistrict_num // 400
    for i in range(split_num):
        f_out = open(base_path+"bj/microdistrict_bj_"+str(i)+".txt",'w')
        f_out.writelines(microdistrict_list[i*400:(i+1)*400])
        f_out.close()
    # 最后不满一百个时写入一个文件
    f_out = open(base_path+"bj/microdistrict_bj_"+str(split_num)+".txt",'w')
    f_out.writelines(microdistrict_list[split_num*400:])
    f_out.close()