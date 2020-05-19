# -*- coding: utf-8 -*-
# 从pyspark.context模块导入SparkContext
import jieba
from pyspark.context import SparkContext

if __name__ == "__main__":
    # 实例化一个SparkContext，用于连接Spark集群
    # 第一个参数“local”表示以本地模式加载集群
    # 第二个参数“WordCount”表示appName，不能有空格
    spark = SparkContext("local", "WordCount")

    # 读取数据，创建弹性式分布数据集（RDD）
    data = spark.textFile("transaction_gz.txt")

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
    # 房型
    # type = data.map(lambda line:line.replace(" ","").split("|")[1]).map(lambda string: string[:2])\
    #     .map(reduceOtherType)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # type.foreach(print)
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
    # area = data.map(lambda line:line.replace(" ","").split("|")[2])\
    #     .map(reduceArea)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # area.foreach(print)

    # # 朝向
    # orientation = data.map(lambda line:line.replace(" ","").split("|")[3]) \
    #     .map(lambda string:string[:1])\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # orientation.foreach(print)

    # 楼层
    # floor = data.map(lambda line:line.replace(" ","").split("|")[4]) \
    #     .map(lambda string:string[:3])\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # floor.foreach(print)

    # def reduceAge(str):
    #     if str != '未知':
    #         age = 2020 - int(str)
    #         if age < 5:
    #             return "0~5年"
    #         elif age < 15:
    #             return "5~15年"
    #         elif age < 30:
    #             return "15~30年"
    #         else:
    #             return "30年以上"
    #     else:
    #         return str
    # # 房龄
    # age = data.map(lambda line:line.replace(" ","").split("|")[5]) \
    #     .map(reduceAge)\
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # age.foreach(print)

    # # 房屋用途
    # purpose = data.map(lambda line:line.replace(" ","").split("|")[6]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # purpose.foreach(print)

    # # 供暖
    # heating = data.map(lambda line:line.replace(" ","").split("|")[7]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # heating.foreach(print)

    # # 装修情况
    # fitment = data.map(lambda line:line.replace(" ","").split("|")[8]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # fitment.foreach(print)

    # # 电梯
    # elevator = data.map(lambda line:line.replace(" ","").split("|")[9]) \
    #     .map(lambda string:(string,1))\
    #     .reduceByKey(lambda a,b:a+b)\
    #     .sortByKey()
    # elevator.foreach(print)



