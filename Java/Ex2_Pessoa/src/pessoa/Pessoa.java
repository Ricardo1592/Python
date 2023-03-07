package pessoa;

public class Pessoa {
	
	protected String nome;
	protected int idade;
	protected String sexo;
	protected String cpf;
	
	public Pessoa(String nome, int idade){
		this.nome=nome;
		this.idade=idade;

	}

	public String get_nome() {
		return this.nome;
	}
	
	public int get_idade() {
		return this.idade;
	}
	
	public String get_sexo() {
		return this.sexo;
	}
	
	public String get_cpf() {
		return this.cpf;
	}
	
	public void set_nome(String novo_nome) {
		this.nome=novo_nome;
				
	}
	
	public void set_idade(int nova_idade) {
		this.idade=nova_idade;
				
	}
	
	public void set_sexo(String novo_sexo) {
		this.sexo=novo_sexo;
				
	}
	
	public void set_cpf(String novo_cpf) {
		this.cpf=novo_cpf;
				
	}
	
	
}
