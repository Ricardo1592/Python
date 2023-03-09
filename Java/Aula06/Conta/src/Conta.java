
public class Conta {
	private String numero;
	private double saldo;
	
	// desing by contract
	// invariant de classe [numero da conta jamais mudar apos criacao]
	// invariant de classe [saldo >= 0] [contrato, regra de consistencia]
	
	public Conta(String numero) {
		this(numero, 0.0);
	}
	
	public Conta(String numero, double saldo) {
		this.numero = numero;
		if(saldo >= 0) {
			this.saldo = saldo;
		}
	}
	
	public void creditar(double valor) {
		if(valor >= 0) {
			this.saldo += valor;
		}
		else {
			System.err.println("Valor a ser creditado tem de ser positivo!");
		}
	}
	
	public void debitar(double valor) {
		if(valor >= 0) {
			if(valor <= this.saldo) {
				this.saldo -= valor;
			}
			else {
				System.err.println("Saldo insuficiente!!");
			}
		}
		else {
			System.err.println("Valor a ser debitado tem de ser positivo!");
		}
	}

	public String getNumero() {
		return numero;
	}

	public double getSaldo() {
		return saldo;
	}

	@Override
	public String toString() {
		return "Conta [numero=" + numero + ", saldo=" + saldo + "]";
	}
}
