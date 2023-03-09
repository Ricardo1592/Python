package c;

import p.*;

public class Main {

	public static void main(String[] args) {
		Point p1 = new Point(0, 0); // instancia
		Point p2 = new Point(0, 0); // instance
		Point p3 = new Point(150, 200);
//		Point p4 = new Point(50);
//		Point p5 = new Point();
		
		// outra forma de pegar o enderecamento de um objeto na heap!
		System.out.println(System.identityHashCode(p1));
		System.out.println(System.identityHashCode(p2));
		System.out.println(System.identityHashCode(p3));
		System.out.println();
		
		System.out.println(p1); // imprimi o valor default
		System.out.println(p2);// imprimi o valor default
		System.out.println(p3);
//		System.out.println(p4);
//		System.out.println(p5);
		System.out.println();
		
		p1.setX(10);
		p1.setY(20);
//		System.out.println(p1.getX());
//		System.out.println(p1.getY());
		System.out.println(p1);
		System.out.println(p1.toString());
		System.out.println();
		
		p2.setX(100);
		p2.setY(200);
//		System.out.println(p2.getX());
//		System.out.println(p2.getY());
		System.out.println(p2);
		System.out.println(p2.toString());
		
		p2.moveBy(10,10);
		System.out.println();
		System.out.println(p2.toString());
		

	}

}
