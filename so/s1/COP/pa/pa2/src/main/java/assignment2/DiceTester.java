/*
Owen Lopez
PID: 5699462
NID: ow281867
This program is done for COP3330 course at year 2026.
DiceTester class simulating 1000 dice rolls and displaying distribution counts and a histogram graph. Assignment 2
*/
package assignment2;

public class DiceTester {

    public static void main(String[] args) {

        // Getting Rolls
        Dice d = new Dice();

        int[] rolls = new int[12];

        for (int i = 0; i < 1000; i++) {
            d.roll(); 

            rolls[d.getFaceValue()-1] += 1;
        }

        for (int i = 2; i <= 12; i++) {
            System.out.println("Number of " + Integer.toString(i) + "s are " + Integer.toString(rolls[i-1]));
        }

        // Histogram
        System.out.println("\n" + "Graph");

        for (int i = 0; i < 8; i++) {
            if ((175 - (i *25)) < 10) {
                System.out.print("  ");
            } else if ((175 - (i *25)) < 100) {
                System.out.print(" ");
            }
            System.out.print((175 - (i * 25)) + "|");
        
            for (int j = 1; j <= 11; j++) {
                if (rolls[j] >= (175 - (i * 25))) {
                    System.out.print("*  ");
                } else {
                    System.out.print("   ");
                }
            } 

            System.out.print("\n");
        } 

        System.out.print("    ");
        for (int i = 0; i <= 15; i++) {
            System.out.print("--"); 
        } 
        System.out.print("\n"); 

        System.out.print("    ");
        for (int i = 2; i <= 11; i++) {
            System.out.print(Integer.toString(i) + ((i > 9)? " " : "  "));
        }
        System.out.print("12\n");
    }
}
