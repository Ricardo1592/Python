package br.ufpe.cin.residencia.banco;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

//Ver anotações TODO no código
public class TransferirActivity extends AppCompatActivity {

    BancoViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_operacoes);
        viewModel = new ViewModelProvider(this).get(BancoViewModel.class);

        TextView tipoOperacao = findViewById(R.id.tipoOperacao);
        EditText numeroContaOrigem = findViewById(R.id.numeroContaOrigem);
        TextView labelContaDestino = findViewById(R.id.labelContaDestino);
        EditText numeroContaDestino = findViewById(R.id.numeroContaDestino);
        EditText valorOperacao = findViewById(R.id.valor);
        Button btnOperacao = findViewById(R.id.btnOperacao);

        valorOperacao.setHint(valorOperacao.getHint() + " transferido");
        tipoOperacao.setText("TRANSFERIR");
        btnOperacao.setText("Transferir");

        btnOperacao.setOnClickListener(
                v -> {
                    String numOrigem = numeroContaOrigem.getText().toString();
                    String numDestino = numeroContaDestino.getText().toString();
                    String valorDaOperacao = valorOperacao.getText().toString();
                    //TODO lembrar de implementar validação dos números das contas e do valor da operação, antes de efetuar a operação de transferência.
                    // O método abaixo está sendo chamado, mas precisa ser implementado na classe BancoViewModel para funcionar.


                    Boolean numOrigemValido = true;
                    Boolean numDestinoValido = true;
                    Boolean numOperacaoValido = true;

                    if (numOrigem.length()<1){
                        // Levanta uma mensagem de campo inválido ao lado dele,
                        // pois nenhum valor foi digitado
                        numeroContaOrigem.setError("Campo invalido");
                        numeroContaOrigem.requestFocus();
                        numOrigemValido = false;
                    }
                    else{
                        numOrigemValido = true;
                    }

                    if (valorDaOperacao.length()<1){
                        // Levanta uma mensagem de campo inválido ao lado dele,
                        // pois nenhum valor foi digitado
                        valorOperacao.setError("Campo invalido");
                        valorOperacao.requestFocus();
                        numOperacaoValido = false;
                    }
                    else{
                        numOperacaoValido = true;
                    }

                    if (numDestino.length()<1){
                        // Levanta uma mensagem de campo inválido ao lado dele,
                        // pois nenhum valor foi digitado
                        numeroContaDestino.setError("Campo invalido");
                        numeroContaDestino.requestFocus();
                        numDestinoValido = false;
                    }
                    else{
                        numDestinoValido = true;
                    }
                    // Só realiza a operação quando os três booleanos forem
                    // verdadeiros, sinalizando que os três campos foram preenchidos
                    if (numOrigemValido && numOperacaoValido && numDestinoValido){
                        double valor = Double.valueOf(valorDaOperacao);
                        viewModel.transferir(numOrigem, numDestino, valor);
                        finish();
                    }
                }
        );

    }
}