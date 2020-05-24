package com.sunlei.datavisual.Controller;

import com.sunlei.datavisual.Model.DataAnalyseFactor;
import com.sunlei.datavisual.Service.DataExtractor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.io.IOException;

@Controller
public class DataController {

    private static DataExtractor dataExtractor;

    static {
        try {
            dataExtractor = new DataExtractor();
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
        if ( city.equals("bj")){
            model.addAttribute("res",dataExtractor.getBj()[order]);
        }else if (city.equals("sh")){
            model.addAttribute("res",dataExtractor.getSh()[order]);
        }else if (city.equals("gz")){
            model.addAttribute("res",dataExtractor.getGz()[order]);
        }else if (city.equals("sz")){
            model.addAttribute("res",dataExtractor.getSz()[order]);
        }
        else{
            System.out.println("unmatched request...");
        }
        return "homepage";
    }
}
