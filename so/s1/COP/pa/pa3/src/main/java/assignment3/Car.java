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
        StringTokenizer st = new StringTokenizer(line, " ");

        st.nextToken();

        setBrandName(st.nextToken());
        setPrice(Integer.parseInt(st.nextToken()));
    }

    public Car() {
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
