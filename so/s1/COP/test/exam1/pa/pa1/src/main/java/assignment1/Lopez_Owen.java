/*
Owen Lopez
PID: 5699462
NID: ow281867
This program is done for COP3330 course at year 2026. This program created a formatted receipt. Assignment 1
*/
package assignment1;

import java.util.Scanner;
import java.util.Random;


public class Lopez_Owen {
    public static String generateDate(Random ran) {
        StringBuilder sb = new StringBuilder(17);

        int year = ran.nextInt(1900, 2100);
        int day  = ran.nextInt(1, 29);
        int month = ran.nextInt(1, 13);

        // Month
        sb.append(switch (month) {
            case 1 -> "January"; 
            case 2 -> "February"; 
            case 3 -> "March"; 
            case 4 -> "April"; 
            case 5 -> "May"; 
            case 6 -> "June"; 
            case 7 -> "July"; 
            case 8 -> "August"; 
            case 9 -> "September"; 
            case 10 -> "October"; 
            case 11 -> "November"; 
            case 12 -> "December"; 
            default -> "ERROR";
        });
        sb.append(" ");

        // Day
        if (day < 10) {
            sb.append("0" + Integer.toString(day));
        } else {
            sb.append(Integer.toString(day));
        }
        sb.append(" ");

        // Year
        sb.append(Integer.toString(year));

        return sb.toString(); 
    }


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random rand = new Random();

        // Header
        System.out.print("""
        ******************************
        ****** S store ***************
        ******************************
        """);

        // Receipt Number
        int id = rand.nextInt(1000, 2000);
        System.out.println("receipt number      " + id);

        // Date 
        String date = generateDate(rand);
        System.out.println(date);

        // Input Loop
        int items = 0;
        double total = 0;
        String s = new String();

        while (true) {
            System.out.print("Write item name ");
            s = scanner.next(); 

            if (s.equals("DONE")) {
                break; 
            }

            System.out.print("Write price ");
            double price = scanner.nextDouble();

            if (!s.replace("F", "f").equals("food")) {
                price *= 1.3;
            }
            
            total += price;
            items++;
            
            // Per Item Output
            System.out.print("item number " + Integer.toString(items));
            System.out.print(" " + s.substring(0, 1).toUpperCase() + s.substring(1) + " ");
            System.out.println(String.format("%,.2f", price));
        }

        // Final Output
        System.out.print(Integer.toString(items) + " items");     
        System.out.print("      ");
        System.out.println("total " + String.format("%,.2f", total));

        System.out.print("""
        ******************************
        ******************************
        ******************************
        """);
    }
}
