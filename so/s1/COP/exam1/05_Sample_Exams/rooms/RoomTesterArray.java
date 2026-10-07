package rooms;
import java.util.Random;

public class RoomTesterArray {

	private static Random rand = new Random();

	public static Room randomRoom(boolean validRoom) {
		Room r = null;
		if (validRoom) {
			int rnum = rand.nextInt(1000 - 100) + 100;
			//try a random number until we get a good one.
			//isValidRoomNo is a static method. We can call from outside
			// as long as it is not private
			while(Room.isValidRoomNo(rnum) == false){
				rnum = rand.nextInt(1000 - 100) + 100;
			}
			r = new Room(rnum, "single", false);
		}
		return r;
	}

	public static void printAll(Room[] arr) {
		for (Room myRoom:arr) { //we will only read the array
		//similar to ArrayLists arrays can be traversed with enhanced for loop
			if(myRoom!=null){
				System.out.println(myRoom);
			}else{
				System.out.println("null");
			}
		}
	}

	public static void printHotel(Room[] arr) {
		for (int i = 0; i < arr.length; i++) {
			if(arr[i]!=null){
				arr[i].showRoom();
			}
		}
		System.out.println();
	}

	public static void main(String[] args) {

		Room[] hotel = new Room[5];
	
		
		// we are not using 4 as hardcoded here. We could have done in that way also
		// but here we are trying to impose the reader that we are filling every spot until the last 
		// position. In this way the code is more descriptive. If the array size change, hardwritten
		// number 4 will look weird. The reader need to guess why it is 4.
		for (int i = 0; i < hotel.length-1; i++) {
			hotel[i]= randomRoom(true);
		}

		printAll(hotel);

		boolean randbool = false;
		//we are flipping a coin here
		if (Math.random() > 0.5) { // Math.random creates a floating point number [0,1)
			randbool = true;
		}

		hotel[4] = randomRoom(randbool);

		System.out.println(Room.getCount() + " rooms are created");

		boolean done = false;
		//reverse traverse
		for (int i = hotel.length - 1; i >= 0 && !done; i--) {
			if (hotel[i] != null) {
				hotel[i].setRoomType("single");
				done = true;
			}
		}

		printHotel(hotel);

	} // end of main

} // end of class
