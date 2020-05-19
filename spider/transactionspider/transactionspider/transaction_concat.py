import os
if __name__ == '__main__':
    source_path = "H:/codes/graduateProject/data/source/transaction/all/"
    filenames = os.listdir(source_path)
    transactions = []
    for filename in filenames:
        file = open(source_path + filename,'r')
        transactions.extend(file.readlines())
        file.close()
    file_out = open(source_path+"transaction_all.txt",'w')
    file_out.writelines(transactions)
    file_out.close()