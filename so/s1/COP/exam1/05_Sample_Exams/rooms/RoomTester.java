package rooms;

import java.util.ArrayList;
import java.util.Random;

public class RoomTester {

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
	
	public static void printAll(ArrayList<Room> arr) {
		for (int i = 0; i < arr.size(); i++) {
			if(arr.get(i)!=null){
				System.out.println(arr.get(i));
			}else{
				System.out.println("null");
			}
		}
	}

	public static void printHotel(ArrayList<Room> arr) {
		for (int i = 0; i < arr.size(); i++) {
			if(arr.get(i)!=null){
				arr.get(i).showRoom();
			}
		}
		System.out.println();
	}

	public static void main(String[] args) {

		ArrayList<Room> hotel = new ArrayList<Room>();

		for (int i = 0; i < 4; i++) {
			hotel.add(randomRoom(true));
		}

		printAll(hotel);

		boolean randbool = false;
		if (rand.nextInt(6) > 3) {
			randbool = true;
		}

		hotel.add(randomRoom(randbool));

		System.out.println(Room.getCount() + " rooms are created");

		boolean done = false;
		for (int i = hotel.size() - 1; i >= 0 && !done; i--) {
			if (hotel.get(i) != null) {
				hotel.get(i).setRoomType("single");
				done = true;
			}
		}

		printHotel(hotel);

	} // end of main

} // end of class
