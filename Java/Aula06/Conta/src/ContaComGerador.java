
public class ContaComGerador {
	
	private int numero; // mandatorio
	private double saldo;  // opcional!
	
	private static int proximo; // auxiliar para geracao de numero de conta
	
	public ContaComGerador(double saldo) {
		this.numero = ContaComGerador.getProximo();
		this.saldo = saldo;
	}
	
	public ContaComGerador() {
		this(0.0);
	}

	public void creditar(double valor) {
		this.saldo += valor;
	}
	
	public void debitar(double valor) {
		this.saldo -= valor;
	}

	public int getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}	
	
	// helper method
	private static int getProximo() {
		return ++ContaComGerador.proximo;
	}
}
