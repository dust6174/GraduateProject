package com.sunlei.datavisual.Service;

import com.sunlei.datavisual.Model.DataAnalyseFactor;
import com.sunlei.datavisual.Model.DataAnalyseUnit;

import java.io.*;
import java.util.*;

public class DataExtractor {
    private String data_path = "H:\\codes\\graduateProject\\data\\visual";

    private DataAnalyseFactor[] bj = new DataAnalyseFactor[15];
    private DataAnalyseFactor[] sh = new DataAnalyseFactor[15];
    private DataAnalyseFactor[] gz = new DataAnalyseFactor[15];
    private DataAnalyseFactor[] sz = new DataAnalyseFactor[15];

    private HashMap<String, Integer> map = new HashMap<String,Integer>();

    public DataExtractor() throws IOException {

        map.put("type",0);
        map.put("area",1);
        map.put("orientation",2);
        map.put("floor",3);
        map.put("age",4);
        map.put("purpose",5);
        map.put("heating",6);
        map.put("fitment",7);
        map.put("elevator",8);
        map.put("typeandorientation",9);
        map.put("typeandfloor",10);
        map.put("typeandage",11);
        map.put("orientationandfloor",12);
        map.put("orientationandage",13);
        map.put("floorandage",14);

        File data = new File(data_path);
        File[] dirs = data.listFiles();
        for (File dir:dirs){
            File[] files = dir.listFiles();
            for (File file:files){
                DataAnalyseFactor dataAnalyseFactor = parser(file);
                String city = dataAnalyseFactor.getCity();
                int order = map.get(dataAnalyseFactor.getFactor()).intValue();
                if ( city.equals("bj")){
                    bj[order] = dataAnalyseFactor;
                }else if (city.equals("sh")){
                    sh[order] = dataAnalyseFactor;
                }else if (city.equals("gz")){
                    gz[order] = dataAnalyseFactor;
                }else if (city.equals("sz")){
                    sz[order] = dataAnalyseFactor;
                }
            }
        }
    }

    private DataAnalyseFactor parser(File file) throws IOException {
        String city = file.getName().split("_")[1];
        String factor = file.getName().replace(".txt","").split("_")[2];
        BufferedReader in = new BufferedReader(new FileReader(file));
        LinkedList<String> infos = new LinkedList<String>();
        String info;
        while((info = in.readLine()) != null){
            infos.add(info);
        }

        int step = infos.size()/9;

        String[] description = new String[step-1];
        int[] number = new int[step-1];
        double[] average_area_price = new double[step-1];
        double[] average_transaction_price = new double[step-1];
        double[] average_transaction_cycle = new double[step-1];
        double[] average_listing_transaction_price_rate = new double[step-1];
        double[] average_views = new double[step-1];
        double[] average_price_adjustment = new double[step-1];
        double[] average_followers = new double[step-1];
        double[] average_pageviews = new double[step-1];
        // 读取影响因素具体类型描述
        for(int i=step*0+1;i<step*1;i++){
            description[i-1] = infos.get(i).replaceAll("\\(|\\)|'","").split(",")[0];
        }
        // 读取数量
        for(int i=step*0+1;i<step*1;i++){
            number[i-1] = Integer.parseInt(infos.get(i).replaceAll("\\(|\\)|'| ","").split(",")[1]);
        }
        // 读取平均均价
        for(int i=step*1+1;i<step*2;i++){
            average_area_price[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均成交价
        for(int i=step*2+1;i<step*3;i++){
            average_transaction_price[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均成交周期
        for(int i=step*3+1;i<step*4;i++){
            average_transaction_cycle[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均挂牌价/成交价
        for(int i=step*4+1;i<step*5;i++){
            average_listing_transaction_price_rate[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均带看
        for(int i=step*5+1;i<step*6;i++){
            average_views[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均调价次数
        for(int i=step*6+1;i<step*7;i++){
            average_price_adjustment[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均关注
        for(int i=step*7+1;i<step*8;i++){
            average_followers[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        // 读取平均浏览量
        for(int i=step*8+1;i<step*9;i++){
            average_pageviews[i%step-1] = Double.parseDouble(infos.get(i).replaceAll("\\(|\\)|'","").split(",")[1]);
        }
        DataAnalyseUnit unit = new DataAnalyseUnit(description,number,average_area_price,average_transaction_price,average_transaction_cycle,average_listing_transaction_price_rate,average_views,average_price_adjustment,average_followers,average_pageviews);
        DataAnalyseFactor dataAnalyseFactor = new DataAnalyseFactor(city,factor,unit);
        return  dataAnalyseFactor;
    }

    public DataAnalyseFactor[] getBj() {
        return bj;
    }

    public DataAnalyseFactor[] getSh() {
        return sh;
    }

    public DataAnalyseFactor[] getGz() {
        return gz;
    }

    public DataAnalyseFactor[] getSz() {
        return sz;
    }

    public HashMap<String, Integer> getMap() {
        return map;
    }
}
