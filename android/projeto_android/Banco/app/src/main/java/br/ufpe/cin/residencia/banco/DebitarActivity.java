package br.ufpe.cin.residencia.banco;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

//Ver anotações TODO no código
public class DebitarActivity extends AppCompatActivity {
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

        labelContaDestino.setVisibility(View.GONE);
        numeroContaDestino.setVisibility(View.GONE);

        valorOperacao.setHint(valorOperacao.getHint() + " debitado");
        tipoOperacao.setText("DEBITAR");
        btnOperacao.setText("Debitar");

        btnOperacao.setOnClickListener(
                v -> {
                    //TODO lembrar de implementar validação do número da conta e do valor da operação, antes de efetuar a operação de crédito.
                    // O método abaixo está sendo chamado, mas precisa ser implementado na classe BancoViewModel para funcionar.

                    // As comparações abaixo foram adicionadas para garantir
                    // que algum valor tenha sido digitado, e isso sendo
                    // válido, só assim realiza a operação
                    String numOrigem = numeroContaOrigem.getText().toString();
                    String valorDaOperacao = valorOperacao.getText().toString();
                    Boolean numOrigemValido = true;
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
                    // Só realiza a operação quando os dois booleanos forem
                    // verdadeiros, sinalizando que os dois campos foram preenchidos
                    if (numOrigemValido && numOperacaoValido){
                        double valor = Double.valueOf(valorDaOperacao);
                        viewModel.debitar(numOrigem,valor);
                        finish();
                    }

                }
        );
    }
}