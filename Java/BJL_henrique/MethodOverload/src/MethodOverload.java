
public class MethodOverload {

	public static void main(String[] args) {	
//		System.out.println("Square of integer 7 is "+MethodOverload.square(7));
//		System.out.println("Square of double 7.5 is "+MethodOverload.square(7.5));
		
		System.out.println("Square of integer 7 is "+square(7));
		System.out.println("Square of double 7.5 is "+square(7.5));
		
//		method1(1.0f, 1);
	}

	public static int square(int intValue) {
		return intValue * intValue;
	}
	
	public static double square(double doubleValue) {
		return doubleValue * doubleValue;
	}
	
	// we can define overload methods with argument types 
	// presenting different order
	static void method1(int a, float b){
		System.out.println("meth1 with int,float args");
	}
	static void method1(float a, int b){
		System.out.println("meth1 with float,int args");
	}
}
