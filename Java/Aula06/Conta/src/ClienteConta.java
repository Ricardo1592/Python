
public class ClienteConta {

	public static void main(String[] args) {
		
		Conta c1 = new Conta("123", 100);
		Conta c2 = new Conta("124", 100);
		Conta c3 = new Conta("125");
		
		c1.creditar(50);
		System.out.println(c1);
		System.out.println(c3);

	}
}
