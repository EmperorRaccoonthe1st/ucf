/*
Owen Lopez
PID: 5699462
NID: ow281867
This program is done for COP3330 course at year 2026.
Dice class holding two Die objects and calculating their combined sum. Assignment 2
*/
package assignment2;

public class Dice {

    // Two private Die objects representing the pair of dice
    private Die die1;
    private Die die2;

    // No-argument constructor initializes both dice (each die's faceValue defaults to 1)
    public Dice() {
        die1 = new Die();
        die2 = new Die();
    }

    // Returns the sum of the face values of both dice
    public int getFaceValue() {
        return die1.getFaceValue() + die2.getFaceValue();
    }

    // Rolls both Die objects
    public void roll() {
        die1.roll();
        die2.roll();
    }
}
