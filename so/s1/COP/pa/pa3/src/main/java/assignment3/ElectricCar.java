/*
    Owen Lopez
    PID: 355592
    NID: ow281867

    This program is written for COP3330 course during the Fall 2026 semester. This driver read car brands from a file & summed their aggregate prices.
*/

package assignment3;

import java.util.StringTokenizer;

public class ElectricCar extends Car{

   private boolean isLithiumIon; 

    public ElectricCar(String brandName, int price) {
        setPrice(price);
        setBrandName(brandName);
        // Default not lithium ion
        isLithiumIon = false;
    }

    public ElectricCar(String line) {
        // Initialize the StringTokenizer
        StringTokenizer st = new StringTokenizer(line, " ");

        st.nextToken();

        // Get name, price, & battery status
        setBrandName(st.nextToken());
        setPrice(Integer.parseInt(st.nextToken()));
        isLithiumIon = st.nextToken().equals("1");
    }


    public String batteryType() {return (isLithiumIon) ? "LithiumIon" : "NickelMetal";}

    public String toString() {
        return "ECar brandname: " + getBrandName() + " price: " + Integer.toString(getPrice()) + " battery: " + batteryType();
  
    }

    public int getPrice() {return (isLithiumIon) ? (int)(1.2 * super.getPrice()) : super.getPrice();}
}
