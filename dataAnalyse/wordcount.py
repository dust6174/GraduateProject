# -*- coding: utf-8 -*-
from pyspark.context import SparkContext
import re

if __name__ == "__main__":
    # 实例化一个SparkContext，用于连接Spark集群
    # 第一个参数“local”表示以本地模式加载集群
    # 第二个参数“WordCount”表示appName，不能有空格
    spark = SparkContext("local", "WordCount")

    # 读取数据，创建弹性式分布数据集（RDD）
    data = spark.textFile("./transaction/transaction_sz.txt")

    def cleanData(line):
        line[10] = re.findall(r"\d+", line[10])[0]
        return line
    data = data.map(lambda line: line.replace(" ", "").split("|")).map(cleanData).cache()



    # def reduceOtherType(str):
    #     if '室' in str:
    #         if int(str.replace("室","")) < 5:
    #             return str
    #         else:
    #             return "5室及以上"
    #     elif str == '车位':
    #         return str
    #     else:
    #         return "5室及以上"
    # # 房型
    # type_number = data.map(lambda line:line[1]).map(lambda string: string[:2])\
    #     .map(reduceOtherType)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # def print2file(str):
    #     file_out = open("result_gz.txt", 'a')
    #     print(str, file=file_out)
    #     file_out.close()
    #     return str
    # def listAdd(list1,list2):
    #     return [int(list1[0])+int(list2[0]),list1[1]+list2[1]]

    # # 均价
    # # 提取出房屋户型和均价信息 放在list里
    # # 将房屋户型中的户数提取出来
    # # 将列表扩充为字典 key 为户型 value 为【均价，1】
    # # reduce value两列分别相加
    # # map value[0]//value[1]
    #
    # type_average_area_price = data.map(lambda line:[line[1][:2],line[10]])\
    #     .map(lambda list:[reduceOtherType(list[0]),list[1]])\
    #     .map(lambda list:(list[0],[list[1],1]))\
    #     .reduceByKey(lambda a,b:listAdd(a,b))\
    #     .map(lambda dict:(dict[0],dict[1][0]//dict[1][1]))\
    #     .sortByKey()
    # type_average_area_price.foreach(lambda line:print2file(line))

    # type_average_area_price = data.map(lambda line:[line[1][:2],line[11]])\
    #     .map(lambda list:[reduceOtherType(list[0]),list[1]])\
    #     .map(lambda list:(list[0],[list[1],1]))\
    #     .reduceByKey(lambda a,b:listAdd(a,b))\
    #     .map(lambda dict:(dict[0],dict[1][0]//dict[1][1]))\
    #     .sortByKey()
    # type_average_area_price.foreach(lambda line:print2file(line))

    # def reduceArea(str):
    #     if "㎡" in str:
    #         area = float(str.replace("㎡",""))
    #         if area < 50:
    #             return "50㎡以下"
    #         elif area < 70:
    #             return "50-70㎡"
    #         elif area < 90:
    #             return "70-90㎡"
    #         elif area < 120:
    #             return "90-120㎡"
    #         elif area < 150:
    #             return "120-150㎡"
    #         elif area < 200:
    #             return "150-200㎡"
    #         else:
    #             return "200㎡以上"
    #     else:
    #         return "其他"
    # # 面积
    # area = data.map(lambda line:line[2])\
    #     .map(reduceArea)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # # 朝向
    # orientation = data.map(lambda line:line[3]) \
    #     .map(lambda string:string[:1])\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # 楼层
    floor = data.map(lambda line:line[4]) \
        .map(lambda string:string[:3])\
        .map(lambda string:(string,1))\
        .reduceByKey(lambda a,b:a+b)\
        .sortByKey()
    floor.foreach(print)
    #
    def reduceAge(str):
        if str != '未知':
            age = 2020 - int(str)
            if age < 5:
                return "0~5年"
            elif age < 15:
                return "5~15年"
            elif age < 30:
                return "15~30年"
            else:
                return "30年以上"
        else:
            return str
    # # 房龄
    # age = data.map(lambda line:line[5]) \
    #     .map(reduceAge)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # # 房屋用途
    # purpose = data.map(lambda line:line[6]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # # 供暖
    # heating = data.map(lambda line:line[7]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # # 装修情况
    # fitment = data.map(lambda line:line[8]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # # 电梯
    # elevator = data.map(lambda line:line[9]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    #
    # result = type.union(area).union(orientation).union(floor).union(age).union(purpose).union(heating).union(fitment).union(elevator)
    # result.foreach(print)



