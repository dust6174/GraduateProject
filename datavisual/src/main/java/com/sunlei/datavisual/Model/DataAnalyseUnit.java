package com.sunlei.datavisual.Model;

import java.util.Arrays;

public class DataAnalyseUnit {
    private String[] description;
    private int[] number;
    private double[] average_area_price;
    private double[] average_transaction_price;
    private double[] average_transaction_cycle;
    private double[] average_listing_transaction_price_rate;
    private double[] average_views;
    private double[] average_price_adjustment;
    private double[] average_followers;
    private double[] average_pageviews;

    public DataAnalyseUnit(String[] description, int[] number, double[] average_area_price, double[] average_transaction_price, double[] average_transaction_cycle, double[] average_listing_transaction_price_rate, double[] average_views, double[] average_price_adjustment, double[] average_followers, double[] average_pageviews) {
        this.description = description;
        this.number = number;
        this.average_area_price = average_area_price;
        this.average_transaction_price = average_transaction_price;
        this.average_transaction_cycle = average_transaction_cycle;
        this.average_listing_transaction_price_rate = average_listing_transaction_price_rate;
        this.average_views = average_views;
        this.average_price_adjustment = average_price_adjustment;
        this.average_followers = average_followers;
        this.average_pageviews = average_pageviews;
    }

    public String[] getDescription() {
        return description;
    }

    public void setDescription(String[] description) {
        this.description = description;
    }

    public int[] getNumber() {
        return number;
    }

    public void setNumber(int[] number) {
        this.number = number;
    }

    public double[] getAverage_area_price() {
        return average_area_price;
    }

    public void setAverage_area_price(double[] average_area_price) {
        this.average_area_price = average_area_price;
    }

    public double[] getAverage_transaction_price() {
        return average_transaction_price;
    }

    public void setAverage_transaction_price(double[] average_transaction_price) {
        this.average_transaction_price = average_transaction_price;
    }

    public double[] getAverage_transaction_cycle() {
        return average_transaction_cycle;
    }

    public void setAverage_transaction_cycle(double[] average_transaction_cycle) {
        this.average_transaction_cycle = average_transaction_cycle;
    }

    public double[] getAverage_listing_transaction_price_rate() {
        return average_listing_transaction_price_rate;
    }

    public void setAverage_listing_transaction_price_rate(double[] average_listing_transaction_price_rate) {
        this.average_listing_transaction_price_rate = average_listing_transaction_price_rate;
    }

    public double[] getAverage_views() {
        return average_views;
    }

    public void setAverage_views(double[] average_views) {
        this.average_views = average_views;
    }

    public double[] getAverage_price_adjustment() {
        return average_price_adjustment;
    }

    public void setAverage_price_adjustment(double[] average_price_adjustment) {
        this.average_price_adjustment = average_price_adjustment;
    }

    public double[] getAverage_followers() {
        return average_followers;
    }

    public void setAverage_followers(double[] average_followers) {
        this.average_followers = average_followers;
    }

    public double[] getAverage_pageviews() {
        return average_pageviews;
    }

    public void setAverage_pageviews(double[] average_pageviews) {
        this.average_pageviews = average_pageviews;
    }

    @Override
    public String toString() {
        return "DataAnalyseUnit{" +
                "description=" + Arrays.toString(description) +
                ", number=" + Arrays.toString(number) +
                ", average_area_price=" + Arrays.toString(average_area_price) +
                ", average_transaction_price=" + Arrays.toString(average_transaction_price) +
                ", average_transaction_cycle=" + Arrays.toString(average_transaction_cycle) +
                ", average_listing_transaction_price_rate=" + Arrays.toString(average_listing_transaction_price_rate) +
                ", average_views=" + Arrays.toString(average_views) +
                ", average_price_adjustment=" + Arrays.toString(average_price_adjustment) +
                ", average_followers=" + Arrays.toString(average_followers) +
                ", average_pageviews=" + Arrays.toString(average_pageviews) +
                '}';
    }
}
