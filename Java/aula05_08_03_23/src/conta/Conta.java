package conta;

public class Conta {
	
	private int numero;
	private int saldo;
	
	public Conta(int numero) {
		this.numero=numero;
		
	}   // Mudar para aceitar apenas um atributo como inicializador da instância
	public Conta(int numero, int saldo) {
		
		this.numero=numero;
		this.saldo=saldo;
		
	}
}
