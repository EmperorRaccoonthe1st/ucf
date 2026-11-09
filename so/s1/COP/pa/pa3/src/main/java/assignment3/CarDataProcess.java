/*
    Owen Lopez
    UCF ID: 355592

    Programming Assignment 3
*\
package assignment3;

import java.util.ArrayList;
import java.io.*;
import java.util.Scanner;

public class CarDataProcess {

   public static int getTotal(ArrayList<Car> arr) {
        int sum = 0;

        for (Car car : arr) {
            sum += car.getPrice();
        }

        return sum;
    } 


    public static void printCars(ArrayList<Car> arr) {
        for (Car car : arr) {
            System.out.println(car.toString());
        }
    }

    
    public static ArrayList<Car> readIntoArrayList(String fname) {
        ArrayList<Car> arr = new ArrayList<Car>();

        try {
            BufferedReader br = null;
            br = new BufferedReader(new FileReader(fname));
            String line = null;
    
            while ((line = br.readLine()) != null ) {
                if (line.substring(0,1).equals("g")) {
                    arr.add(new Car(line));
                } else {
                    arr.add(new ElectricCar(line));
                }
            }

            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        return arr;
    }


    public static void main(String args[]) {

        System.out.print("Input file name:");

        Scanner sc = new Scanner(System.in);
        String fname = sc.nextLine();

        ArrayList<Car> arr = readIntoArrayList(fname); 

        printCars(arr); 

        System.out.println("Total price is " + Integer.toString(getTotal(arr)));
    }
}
