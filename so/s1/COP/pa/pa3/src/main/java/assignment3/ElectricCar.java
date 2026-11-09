package assignment3;

import java.util.StringTokenizer;

public class ElectricCar extends Car{

   private boolean isLithiumIon; 

    public ElectricCar(String brandName, int price) {
        setPrice(price);
        setBrandName(brandName);
        isLithiumIon = false;
    }

    public ElectricCar(String line) {
        StringTokenizer st = new StringTokenizer(line, " ");

        st.nextToken();

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
