package com.sunlei.datavisual.Model;

import com.sun.org.apache.xml.internal.resolver.helpers.PublicId;

import java.util.Arrays;

public class DataAnalyseFactor {
    private String city;
    private String factor;
    private DataAnalyseUnit unit;

    public DataAnalyseFactor(String city, String factor, DataAnalyseUnit unit) {
        this.city = city;
        this.factor = factor;
        this.unit = unit;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getFactor() {
        return factor;
    }

    public void setFactor(String factor) {
        this.factor = factor;
    }

    public DataAnalyseUnit getUnit() {
        return unit;
    }

    public void setUnit(DataAnalyseUnit unit) {
        this.unit = unit;
    }

    @Override
    public String toString() {
        return "DataAnalyseFactor{" +
                "city='" + city + '\'' +
                ", factor='" + factor + '\'' +
                ", unit=" + unit +
                '}';
    }
}
