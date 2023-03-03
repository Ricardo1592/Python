package calc;

public class Main {
	
	public static void main(String[] args) {
		int x, y = 0;
		x = 10;
		y = 10;
		int resultAdd = Calc.add(x, y);
		int resultSub = Calc.sub(20, 10);
		int resultMul = Calc.mul(10, 10);
		int resultDiv = Calc.div(10, 10);
		System.out.println("resultAdd = "+resultAdd);
		System.out.println("resultSub = "+resultSub);
		System.out.println("resultMul = "+resultMul);
		System.out.println("resultDiv = "+resultDiv);
	}

}
