
public class T extends Object{
	
	public static int x;
	public int y;
	
	public T() {}
	public T(int y) {
		super();
	}
	
	public static void m2() {}
	
	public static void m() {
		x = 100;
//		y = 100;
		m2();
//		o();
	}
	
	public void n() {
		x = 100;
		y = 100;
		m2();
		o();
	}
	
	public void o() {}
	
	
	public static void main(String[] args) {
		T t = new T(10);
		t.x = 100;
		
		T.x = 1000;
		
		System.out.println(T.x);
		System.out.println(T.x);
		
         T.x = 50;
		
		System.out.println(T.x);
		System.out.println(T.x);
		
	}

}
