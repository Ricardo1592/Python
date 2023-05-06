package br.ufpe.cin.residencia.banco.conta;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import br.ufpe.cin.residencia.banco.R;

//Ver anotações TODO no código
public class AdicionarContaActivity extends AppCompatActivity {

    ContaViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_adicionar_conta);
        viewModel = new ViewModelProvider(this).get(ContaViewModel.class);

        Button btnAtualizar = findViewById(R.id.btnAtualizar);
        Button btnRemover = findViewById(R.id.btnRemover);
        EditText campoNome = findViewById(R.id.nome);
        EditText campoNumero = findViewById(R.id.numero);
        EditText campoCPF = findViewById(R.id.cpf);
        EditText campoSaldo = findViewById(R.id.saldo);

        btnAtualizar.setText("Inserir");
        btnRemover.setVisibility(View.GONE);

        btnAtualizar.setOnClickListener(
                v -> {
                    String nomeCliente = campoNome.getText().toString();
                    String cpfCliente = campoCPF.getText().toString();
                    String numeroConta = campoNumero.getText().toString();
                    String saldoConta = campoSaldo.getText().toString();
                    // Essas variáveis booleanas serão definidas em funções específicas no final do código
                    boolean nomeSoLetras = validacaoLetras(nomeCliente) && nomeCliente.length() >= 5;
                    boolean cpfSoNumeros = validacaoNumeros(cpfCliente) && cpfCliente.length() == 11;
                    boolean numeroSoNumeros = validacaoNumeros(numeroConta) && (numeroConta.length() <= 20 && numeroConta.length() > 0);
                    boolean saldoSoNumeros = validacaoNumeros(saldoConta) && (saldoConta.length() <= 30 && saldoConta.length() > 0);
                    // Garante que o nome só contém letras e possui no mínimo 5 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!nomeSoLetras){
                       campoNome.setText("Nome Inválido");
                    }
                    // Garante que o cpf só contém números e possui 11 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!cpfSoNumeros){
                        campoCPF.setText("CPF Inválido");
                    }
                    // Garante que o número da conta só contém números e tem no máximo 20 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!numeroSoNumeros){
                        campoNumero.setText("Número da conta inválido");
                    }
                    // Garante que o saldo da conta só contém números e tem no máximo 30 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!saldoSoNumeros){
                        campoSaldo.setText("Saldo Inválido");
                    }
                    //TODO: Incluir validações aqui, antes de criar um objeto Conta (por exemplo, verificar que digitou um nome com pelo menos 5 caracteres, que o campo de saldo tem de fato um número, assim por diante). Se todas as validações passarem, aí sim cria a Conta conforme linha abaixo.
                    // Essa verificação garante a criação do objeto conta apenas após as validações
                    if (nomeSoLetras && cpfSoNumeros && numeroSoNumeros && saldoSoNumeros) {
                        Conta c = new Conta(numeroConta, Double.valueOf(saldoConta), nomeCliente, cpfCliente);
                        //TODO: chamar o método que vai salvar a conta no Banco de Dados
                        // Adicionei na linha abaixo o método para inserir no banco de dados
                        viewModel.inserir(c);
                        finish();
                    }
                }
        );

    }

    // Métodos adicionados para validação
    public static boolean validacaoLetras(String nome){
        int i = 0;
        while (i < nome.length()) {
            char c = nome.charAt(i);
            if (!Character.isLetter(c) && c != ' ') {
                return false;
            }
            i++;
        }
        return true;
    }

    public static boolean validacaoNumeros(String cpf){
        int i = 0;
        while (i < cpf.length()) {
            char c = cpf.charAt(i);
            if (!Character.isDigit(c) && c != ' ') {
                return false;
            }
            i++;
        }
        return true;
    }
}