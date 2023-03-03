


import java.util.ArrayList;
import java.util.Iterator;

public class ArrayLists {

	public static void main(String[] args) {
		ArrayList<String> names = new ArrayList<>(); // size 0
		
		names.add("Emily"); // size 1
		names.add("Bob"); // size 2
		names.add("Cindy"); // size 3
		
		String name = names.get(2);
		System.out.println(name);
		names.set(2, "Carolyn");
		System.out.println(names.get(2));
		names.add(1, "Ann"); // size 4
		System.out.println(names.get(2));
		names.remove(1); // size 3
		System.out.println(names.get(1));
		System.out.println(names.size());
		
		System.out.println();
		for (Iterator<String> iterator = names.iterator(); iterator.hasNext();) {
			String currentName = iterator.next();
			System.out.println(currentName);
		}
		System.out.println();
		for (String currentName : names) {
			System.out.println(currentName);
		}	
	}
}
