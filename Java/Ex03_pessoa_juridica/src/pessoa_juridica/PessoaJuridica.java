package pessoa_juridica;

public class PessoaJuridica {
	
	protected String nome;
	protected String cnpj;
	private int contaBanco;
	
	public PessoaJuridica(String nome, String cnpj, int contaBanco) {
		
		this.nome=nome;
		this.cnpj=cnpj;
		this.contaBanco=contaBanco;	
		
	}
	
	public String get_nome() {
		return this.nome;
	}

	public String get_cnpj() {
		return this.cnpj;
	}
	
	public int contaBanco() {
		return this.contaBanco;
	}
	
	public void set_nome(String novo_nome) {
		this.nome=novo_nome;
		
	}
	
	public void set_cnpj(String novo_cnpj) {
		this.cnpj=novo_cnpj;
	}
	
	public void set_contaBanco(int conta) {
		this.contaBanco=conta;
	}
	@Override	
	public String toString(){
		return "Empresa "+this.nome + " com cnpj " + this.cnpj;
	}
		
			
}
