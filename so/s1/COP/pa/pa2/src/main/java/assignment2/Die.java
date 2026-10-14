/*
Owen Lopez
PID: 5699462
NID: ow281867
This program is done for COP3330 course at year 2026.
Die class representing a 6-sided die with rolling and face value tracking. Assignment 2
*/
package assignment2;

import java.util.Random;

public class Die {

    // Instance variable representing the die face value (1 to 6)
    private int faceValue;

    // No-argument constructor initializes faceValue to 1
    public Die() {
        setFaceValue(1);
    }

    // Sets the faceValue of the die
    public void setFaceValue(int val) {
        faceValue = val;
    }

    // Returns the current faceValue of the die
    public int getFaceValue() {
        return faceValue;
    }

    // Rolls the die randomly, updating faceValue to a number between 1 and 6 inclusive
    public void roll() {
        Random r = new Random();

        setFaceValue(r.nextInt(6) + 1);
    }
}

