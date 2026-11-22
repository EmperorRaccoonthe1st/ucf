/*
    Owen Lopez
    PID: 355592
    NID: ow281867

    This program is written for COP3330 course during the Fall 2026 semester. This driver read car brands from a file & summed their aggregate prices.
*/

package assignment3;

import java.util.StringTokenizer;

public class Car {
    private int price;
    private String brandName;

    public Car(String brandName, int price) {
        setPrice(price);
        setBrandName(brandName);
    }

    public Car(String line) {
        // Declare tokenzier
        StringTokenizer st = new StringTokenizer(line, " ");

        st.nextToken();

        // Get name & price
        setBrandName(st.nextToken());
        setPrice(Integer.parseInt(st.nextToken()));
    }

    public Car() {
        // If car object initialized w/o parameters, invalid state
        setPrice(-1);
        setBrandName("Invalid");
    }


    public int getPrice() {return price;}
    public void setPrice(int price) {this.price = price;}

    public String getBrandName() {return brandName;}
    public void setBrandName(String brandName) {this.brandName = brandName;}

    public String toString() {
        return "GCar brandname: " + getBrandName() + " price: " + Integer.toString(price);
    }
}
