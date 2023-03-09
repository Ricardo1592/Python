
public class ClienteContaComGerador {

	public static void main(String[] args) {		
		ContaComGerador c1 = new ContaComGerador();
		ContaComGerador c2 = new ContaComGerador(100);
		ContaComGerador c3 = new ContaComGerador();
		ContaComGerador c4 = new ContaComGerador();
		
		System.out.println(c1.getNumero());
		System.out.println(c2.getNumero());
		System.out.println(c3.getNumero());
		System.out.println(c4.getNumero());
//		System.out.println("********");
//		System.out.println(c2.toString());

	}
}
