import org.apache.spark.{SparkConf, SparkContext}

object snifferTest {
  def main(args: Array[String]): Unit={
    val conf = new SparkConf()
      .setAppName("sniffer test: spark app(scala)")
      .setMaster("local[1]");
    conf.set("spark.testing.memory","10737440000")

    new SparkContext(conf)
      .parallelize(List(1,2,3,4,5,6))
      .map(x=>x*x)
      .filter(_>10)
      .collect()
      .foreach(println);
  }
}
