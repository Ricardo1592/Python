package c;

import java.util.ArrayList;

import p.Point;

public class Main2 {

	public static void main(String[] args) {
		Point p1 = new Point(10, 10); // instancia
		Point p2 = new Point(10, 10); // instance
		
		ArrayList<Point > list1 = new ArrayList<>();
		ArrayList<Point > list2 = new ArrayList<>();
		
		list1.add(new Point(10, 20));
		list1.add(p1);
	
		System.out.println(list1.contains(p2));
		System.out.println(list1.equals(list2));

	}

}
