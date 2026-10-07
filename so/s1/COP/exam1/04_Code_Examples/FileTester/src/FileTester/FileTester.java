package FileTester;
import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class FileTester {

	public static void writeFile(String fname,ArrayList<String> lines) {
		BufferedWriter bw=null;
		try {
			bw=new BufferedWriter(new FileWriter(fname));
			for(int i=0;i<lines.size();i++) {
				bw.write(lines.get(i)+"\n");
			}
			bw.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	//reads the file word by word
	public static ArrayList<String> readFile(String fname){
		BufferedReader br=null;
		ArrayList<String> arr=new ArrayList<>();
		StringTokenizer st=null;
		try {
			br = new BufferedReader(new FileReader(fname));
			String line=null;
			while((line=br.readLine())!=null) {
				// each line will be stored in line
				st=new StringTokenizer(line," ");
				while(st.hasMoreTokens()) {
					String token = st.nextToken(); // one word
					arr.add(token);
				}				
			}
			br.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
		return arr;
	}
	
	public static void main(String[] args) {
		ArrayList<String> arr=new ArrayList<>();
		arr.add("first line");
		arr.add("second line");
		arr.add("third line");
		//writeFile("example.txt", arr);
		arr=readFile("example.txt");
		System.out.println(arr.toString());
		System.out.println("Size is "+arr.size());
	}

	
}
