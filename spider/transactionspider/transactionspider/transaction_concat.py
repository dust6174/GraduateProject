import os
if __name__ == '__main__':
    source_path = "H:/codes/graduateProject/data/source/transaction/transaction_bj/"
    filenames = os.listdir(source_path)
    transactions = []
    for filename in filenames:
        file = open(source_path + filename,'r')
        transactions.extend(file.readlines())
        file.close()
    file_out = open(source_path+"transaction_bj.txt",'w')
    file_out.writelines(transactions)
    file_out.close()