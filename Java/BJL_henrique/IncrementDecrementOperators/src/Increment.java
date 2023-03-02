
public class Increment {

	public static void main(String[] args) {
		// demonstrate prefix increment operator
		int c = 5;
		System.out.println(" c before preincrement: "+c);
		System.out.println("     preincrementing c: "+(++c));
		System.out.println("  c after preincrement: "+c);
		
		System.out.println(); // skip a line
		
		// demonstrate postfix increment operator
		c = 5;
		System.out.println(" c before postincrement: "+c);
		System.out.println("     postincrementing c: "+(c++));
		System.out.println("  c after postincrement: "+c); // -> c = 6;
		
		// c = c + 1;
		// c += 1;
		// c++;
		// ++c;
        int d, e;
        d = c++;
        System.out.println("c = "+c);
        System.out.println("d = "+d);
        e = ++c;
        System.out.println("c = "+c);
        System.out.println("e = "+e);
	}

}
