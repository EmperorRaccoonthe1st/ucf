package rooms;

public class Room {

	private int roomNumber;
	private String roomType; // single, double, suite
	private boolean occupied;

	private static int count = 0; // to keep track of created objects

	public Room() {
		this(1, "single", false);
	}

	public Room(int rn, String givenRoomType, boolean occ) {
		setRoomNumber(rn);
		setRoomType(givenRoomType);
		occupied = occ;
		count++;
	}

	public int getRoomNumber() {
		return roomNumber;
	}

	//this method does not touch the isntance variables
	// it is better if it stays as static
	public static boolean isValidRoomNo(int x){
		if(x>0 && x<1000){
			int val=x/100;
			if(val*100+20>x){
				return true;
			}
		}
		return false;
	}
	
	// this method should be only callable by the class
	private void setRoomNumber(int rn) {
		if(isValidRoomNo(rn)){
			roomNumber = rn;
		}else{
			System.out.println("Error in setting room number");
			roomNumber = 999;
		}
	}

	public boolean isOccupied() {
		return occupied;
	}

	public void checkin() {
		if (!isOccupied()) {
			occupied = true;
		}
	}

	public void checkout() {
		occupied = false;
	}

	public void setRoomType(String givenRoom) {
		if (givenRoom.equals("single") ||
			givenRoom.equals("double") ||
			givenRoom.equals("suite")) {
			roomType = givenRoom;
		} else {
			System.out.println("Invalid room type entered");
		}
	}

	public String getRoomType() {
		return roomType;
	}

	public String toString() {
		String result = "number " + roomNumber;
		if (isOccupied()){
			result += " is occupied";
		}else{
			result += " is vacant";
		}
		return result;
	}

	public void showRoom() {
		String result = "[ ]"; // assume the room is vacant
		if (isOccupied())
			result = "[x]"; // if occupied change the output
		System.out.print(result);
	}

	public static int getCount() { // since count is static this method should be static
		return count;
	}

} // end of class
