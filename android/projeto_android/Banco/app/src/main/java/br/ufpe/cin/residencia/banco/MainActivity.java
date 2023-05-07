package br.ufpe.cin.residencia.banco;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import java.text.NumberFormat;

import br.ufpe.cin.residencia.banco.cliente.ClientesActivity;
import br.ufpe.cin.residencia.banco.conta.ContasActivity;

//Ver anotações TODO no código
public class MainActivity extends AppCompatActivity {
    BancoViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        viewModel = new ViewModelProvider(this).get(BancoViewModel.class);

        Button contas = findViewById(R.id.btnContas);
        Button clientes = findViewById(R.id.btnClientes);
        Button transferir = findViewById(R.id.btnTransferir);
        Button debitar = findViewById(R.id.btnDebitar);
        Button creditar = findViewById(R.id.btnCreditar);
        Button pesquisar = findViewById(R.id.btnPesquisar);
        TextView totalBanco = findViewById(R.id.totalDinheiroBanco);

        //Remover a linha abaixo se for implementar a parte de Clientes
        clientes.setEnabled(false);

        contas.setOnClickListener(
                v -> startActivity(new Intent(this, ContasActivity.class))
        );
        clientes.setOnClickListener(
                v -> startActivity(new Intent(this, ClientesActivity.class))
        );
        transferir.setOnClickListener(
                v -> startActivity(new Intent(this, TransferirActivity.class))
        );
        creditar.setOnClickListener(
                v -> startActivity(new Intent(this, CreditarActivity.class))
        );
        debitar.setOnClickListener(
                v -> startActivity(new Intent(this, DebitarActivity.class))
        );
        pesquisar.setOnClickListener(
                v -> startActivity(new Intent(this, PesquisarActivity.class))
        );

        // Foi adicionado um MutableLiveData que observa mudanças no saldo
        // total do banco. Os métodos abaixo são responsáveis por monitorar
        // mudanças e solicitar do banco a soma total de todas as contas cadastradas.
        viewModel.mostrarSaldoTotal();
        viewModel.bancoSaldoTotal.observe(this, novoSaldoTotal -> {
            totalBanco.setText(NumberFormat.getCurrencyInstance().format(novoSaldoTotal));
        });
    }

    // Os métodos abaixo foram adicionados para que haja uma nova consulta
    // sempre que voltar das activities de Creditar, Debitar e Transferir,
    // Assim, atualizando o valor da soma de todas as contas, para que o
    // o MutableLiveData seja capaz de capturar as mudanças e a alteração
    // na soma delas.
    protected void onStart() {
        super.onStart();
        viewModel.mostrarSaldoTotal();

    }

    protected void onResume() {
        super.onResume();
        viewModel.mostrarSaldoTotal();

    }


    //TODO Neste arquivo ainda falta a atualização automática do valor total de dinheiro armazenado no banco
}