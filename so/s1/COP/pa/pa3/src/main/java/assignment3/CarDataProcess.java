/*
    Owen Lopez
    PID: 355592
    NID: ow281867

    This program is written for COP3330 course during the Fall 2026 semester. This driver read car brands from a file & summed their aggregate prices.
*/
package assignment3;

import java.util.ArrayList;
import java.io.*;
import java.util.Scanner;

public class CarDataProcess {

   public static int getTotal(ArrayList<Car> arr) {
        int sum = 0;

        // Sums prices in Car Array
        for (Car car : arr) {
            sum += car.getPrice();
        }

        return sum;
    } 


    public static void printCars(ArrayList<Car> arr) {
        // Print each Car
        for (Car car : arr) {
            System.out.println(car.toString());
        }
    }

    
    public static ArrayList<Car> readIntoArrayList(String fname) {
        // Declare ArrayList to be returned
        ArrayList<Car> arr = new ArrayList<Car>();

        try {
            // Create a new reader
            BufferedReader br = null;
            br = new BufferedReader(new FileReader(fname));
            String line = null;
    
            // While there is something in the reader's buffer
            while ((line = br.readLine()) != null ) {
                // Check first Character in Line
                if (line.substring(0,1).equals("g")) {
                    arr.add(new Car(line));
                } else {
                    arr.add(new ElectricCar(line));
                }
            }

            br.close();

        // Throw if file isn't found
        } catch (Exception e) {
            e.printStackTrace();
        }

        return arr;
    }


    public static void main(String args[]) {

        // Intake file name
        System.out.print("Input file name:");

        Scanner sc = new Scanner(System.in);
        String fname = sc.nextLine();

        // Fill array
        ArrayList<Car> arr = readIntoArrayList(fname); 

        printCars(arr); 

        // Perform operations then print
        System.out.println("Total price is " + Integer.toString(getTotal(arr)));
    }
}
