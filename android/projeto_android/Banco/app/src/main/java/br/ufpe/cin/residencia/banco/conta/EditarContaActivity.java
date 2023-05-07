package br.ufpe.cin.residencia.banco.conta;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import java.text.NumberFormat;

import br.ufpe.cin.residencia.banco.R;

//Ver anotações TODO no código
public class EditarContaActivity extends AppCompatActivity {

    public static final String KEY_NUMERO_CONTA = "numeroDaConta";
    // Variáveis adicionadas para mostrar valores da Conta selecionada
    public static final String CPF_CONTA = "CPFDaConta";
    public static final String Nome_CONTA = "NomeDaConta";
    public static final String Saldo_CONTA = "SaldoDaConta";
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
        campoNumero.setEnabled(false);



        Intent i = getIntent();
        // Modifiquei o parâmetro de getStringExtra para "numeroConta" assim ficando igual o do contaViewHolder
        // Carrega a informação do número da conta para posterior consulta
        String numeroConta = i.getStringExtra("numeroConta");
        // Utilizando o viewModel para buscar no banco a conta com o número passado na intent
        viewModel.buscarPeloNumero(numeroConta);
        viewModel.contaAtual.observe(
                this,
                conta -> {
                    campoNome.setText(conta.nomeCliente);
                    campoCPF.setText(conta.cpfCliente);
                    campoSaldo.setText(NumberFormat.getInstance().format(conta.saldo));
                }
        );
        // TODO usar o número da conta passado via Intent para recuperar informações da conta
        // Adicionei os métodos abaixo para colocar na tela os valores vindos da activity do contaViewHolder
        campoNumero.setText(numeroConta);
        btnAtualizar.setText("Editar");
        btnAtualizar.setOnClickListener(
                v -> {
                    String nomeCliente = campoNome.getText().toString();
                    String cpfCliente = campoCPF.getText().toString();
                    String saldoConta = campoSaldo.getText().toString();
                    //TODO: Incluir validações aqui, antes de criar um objeto Conta. Se todas as validações passarem, aí sim monta um objeto Conta.

                    // Essas variáveis booleanas serão definidas em funções específicas no final do código
                    boolean nomeSoLetras = validacaoLetras(nomeCliente) && nomeCliente.length() >= 5;
                    boolean cpfSoNumeros = validacaoNumeros(cpfCliente) && cpfCliente.length() == 11;
                    boolean saldoSoNumeros = validacaoNumeros(saldoConta) && (saldoConta.length() <= 30 && saldoConta.length() > 0);
                    // Garante que o nome só contém letras e possui no mínimo 5 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!nomeSoLetras){
                        campoNome.setError("Nome Inválido");
                        campoNome.requestFocus();
                    }
                    // Garante que o cpf só contém números e possui 11 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!cpfSoNumeros){
                        campoCPF.setError("CPF Inválido");
                        campoCPF.requestFocus();
                    }
                    // Garante que o saldo da conta só contém números e tem no máximo 30 caracteres, e que o campo não está vazio, caso contrário diz no campo que o valor está inválido
                    if (!saldoSoNumeros){
                        campoSaldo.setError("Saldo Inválido");
                        campoSaldo.requestFocus();
                    }
                    //TODO: chamar o método que vai atualizar a conta no Banco de Dados

                    // Instanciando uma nova conta apenas quando os dados forem válidos, assim chamando o método atualizar do viewModel somente
                    if (nomeSoLetras && cpfSoNumeros && saldoSoNumeros) {
                        Conta c = new Conta(numeroConta, Double.parseDouble(saldoConta), nomeCliente, cpfCliente);
                        viewModel.atualizar(c);
                        finish();
                    }
                }
        );

        btnRemover.setOnClickListener(v -> {
            //TODO implementar remoção da conta

            // Método adicionado para remover uma conta da aplicação e do banco de dados
            viewModel.remover(viewModel.contaAtual.getValue());
            finish();

        });
    }


    // Métodos criados para validação
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