package com.sunlei.datavisual.Controller;

import com.sunlei.datavisual.Model.DataAnalyseFactor;
import com.sunlei.datavisual.Service.DataExtractor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;
import java.util.HashMap;

@Controller
public class DataController {

    private static DataExtractor dataExtractor;

    private static HashMap<String, String> map = new HashMap<String,String>();

    static {
        try {
            dataExtractor = new DataExtractor();
            map.put("bj","北京");
            map.put("sh","上海");
            map.put("gz","广州");
            map.put("sz","深圳");
            map.put("type","房屋户型");
            map.put("area","面积大小");
            map.put("orientation","房屋朝向");
            map.put("floor","所在楼层");
            map.put("age","房屋寿命");
            map.put("purpose","房屋用途");
            map.put("heating","供暖方式");
            map.put("fitment","装修情况");
            map.put("elevator","有无电梯");
            map.put("typeandorientation","房屋户型、房屋朝向");
            map.put("typeandfloor","房屋户型、所在楼层");
            map.put("typeandage","房屋户型、房屋寿命");
            map.put("orientationandfloor","房屋朝向、所在楼层");
            map.put("orientationandage","房屋朝向、房屋寿命");
            map.put("floorandage","所在楼层、房屋寿命");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @RequestMapping("")
    public String dataDisplay(
            @RequestParam(value = "city",required = false,defaultValue = "bj") String city,
            @RequestParam(value = "factor",required = false,defaultValue = "type") String factor,
            Model model
    ){
        System.out.println("new request: "+city+" and "+factor);
        int order = dataExtractor.getMap().get(factor).intValue();
        DataAnalyseFactor result = null;
        if ( city.equals("bj")){
            result = dataExtractor.getBj()[order];
        }else if (city.equals("sh")){
            result = dataExtractor.getSh()[order];
        }else if (city.equals("gz")){
            result = dataExtractor.getGz()[order];
        }else if (city.equals("sz")){
            result = dataExtractor.getSz()[order];
        }
        else{
            System.out.println("unmatched request...");
            return "homepage";
        }
        System.out.println(result.toString());
        model.addAttribute("res",new DataAnalyseFactor(map.get(result.getCity()),map.get(result.getFactor()),result.getUnit()));
        return "homepage";
    }
}
