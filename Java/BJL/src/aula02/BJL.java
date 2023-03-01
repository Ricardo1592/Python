package aula02;

public class BJL {

	public static void main(String [] args) {
		// primitive types
		int x=10;
		int x2=30;
		long l= 20;
		byte b = 8;
		short s = 16;
		boolean bool= true;
		
		float f = 12.5f;
		double d= 12.5;
		char c='c';
		
		// widening conversion
		l=x;
		d=f;
		x=b;
		x=s;
		s=b;
			
		// narrowing conversion
		x=(int)d;
		f=(float)d;
		b=(byte)s;
		
		int w=0,y=0,z=0;
		
		w= y+z;
		
		System.out.println(x);
		
		// Object types
		String s="java";
		
		System.out.println(s);
	}
	
}
