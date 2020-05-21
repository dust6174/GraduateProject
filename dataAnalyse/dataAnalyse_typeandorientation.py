# -*- coding: utf-8 -*-
from pyspark.context import SparkContext
import re

if __name__ == "__main__":
    spark = SparkContext("local","dataAnalyse_typeandorientation")

    data = spark.textFile("./transaction/transaction_bj.txt")

    def reduceOtherType(str):
        if '室' in str:
            if int(str.replace("室","")) < 5:
                return str
            else:
                return "5室及以上"
        elif str == '车位':
            return str
        else:
            return "5室及以上"

    # 均价 成交价和挂牌价的数据清洗
    # 部分房屋没有均价，会错误的提取到成交年份，需要从成交价和面积自己计算,时间原因 暂时放弃
    def cleanData(line):
        line[1] = reduceOtherType(line[1][:2])
        line[3] = line[3][:1]
        line[10] = re.findall(r"\d+", line[10])[0]
        line[11] = re.findall(r"\d+", line[11])[0]
        # if float(line[10]) < 2100:
        #     line[10] = float(line[11]) // float(line[4].replace("㎡","")) * 10000
        return line

    data = data.map(lambda line: line.replace(" ", "").split("|")).map(cleanData).cache()

    def print2file(str):
        file_out = open("./bj/result_bj_typeandorientation.txt", 'a')
        print(str, file=file_out)
        file_out.close()
        return str

    # 数量
    typeandorientation_number = data.map(lambda line:line[1] + "&" + line[3])\
        .map(lambda line:(line,1))\
        .reduceByKey(lambda a,b:a+b)\
        .sortByKey()
    print2file("number:")
    typeandorientation_number.foreach(lambda line:print2file(line))

    def listAdd(list1,list2):
        if ("暂无数据" == list1[0]):
            list1 = [0,list1[1]]
        if("暂无数据" == list2[0]):
            list2 = [0,list2[1]]
        return [int(list1[0])+int(list2[0]),list1[1]+list2[1]]

    # def listAdd(list1,list2):
    #     return [int(list1[0])+int(list2[0]),list1[1]+list2[1]]

    # 平均均价
    # 提取出房屋户型和均价信息 放在list里
    # 将房屋户型中的户数提取出来
    # 将列表扩充为字典 key 为户型 value 为[均价，1]
    # reduce value两列分别相加
    # map value[0]//value[1]

    typeandorientation_average_area_price = data.map(lambda line:[line[1] + "&" + line[3],line[10]])\
        .map(lambda list:(list[0],[list[1],1]))\
        .reduceByKey(lambda a,b:listAdd(a,b))\
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average area price:")
    typeandorientation_average_area_price.foreach(lambda line:print2file(line))

    # 平均成交价

    typeandorientation_average_transaction_price = data.map(lambda line:[line[1] + "&" + line[3],line[11]])\
        .map(lambda list:(list[0],[list[1],1]))\
        .reduceByKey(lambda a,b:listAdd(a,b))\
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average transaction price:")
    typeandorientation_average_transaction_price.foreach(lambda line:print2file(line))

    # 平均成交周期

    typeandorientation_average_transaction_cycle = data.map(lambda line: [line[1] + "&" + line[3], line[12]]) \
        .map(lambda list: (list[0], [list[1], 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average transaction cycle:")
    typeandorientation_average_transaction_cycle.foreach(lambda line: print2file(line))

    def price_rate(a,b):
        if ("暂无数据" == a) or ("暂无数据" == b):
            return 1
        else:
            return float(a) / float(b)
    # 平均挂牌价/成交价

    typeandorientation_average_listing_transaction_price_rate = data.map(lambda line: [line[1] + "&" + line[3], line[13],line[11]]) \
        .map(lambda list: (list[0], [price_rate(list[1],list[2]), 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average listing price / transaction price:")
    typeandorientation_average_listing_transaction_price_rate.foreach(lambda line: print2file(line))

    # 平均带看次数

    typeandorientation_average_views = data.map(lambda line: [line[1] + "&" + line[3], line[14]]) \
        .map(lambda list: (list[0], [list[1], 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average views:")
    typeandorientation_average_views.foreach(lambda line: print2file(line))

    # 平均调价次数

    typeandorientation_average_price_adjustment = data.map(lambda line: [line[1] + "&" + line[3], line[14]]) \
        .map(lambda list: (list[0], [list[1], 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average price adjustment:")
    typeandorientation_average_price_adjustment.foreach(lambda line: print2file(line))

    # 平均关注

    typeandorientation_average_followers = data.map(lambda line: [line[1] + "&" + line[3], line[14]]) \
        .map(lambda list: (list[0], [list[1], 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average followers:")
    typeandorientation_average_followers.foreach(lambda line: print2file(line))

    # 平均浏览

    typeandorientation_average_pageviews = data.map(lambda line: [line[1] + "&" + line[3], line[14]]) \
        .map(lambda list: (list[0], [list[1], 1])) \
        .reduceByKey(lambda a, b: listAdd(a, b)) \
        .map(lambda dict: (dict[0], int(dict[1][0]) / dict[1][1])) \
        .sortByKey()
    print2file("Average pageviews:")
    typeandorientation_average_pageviews.foreach(lambda line: print2file(line))

