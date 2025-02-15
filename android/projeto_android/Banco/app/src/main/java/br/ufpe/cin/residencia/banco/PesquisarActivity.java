package br.ufpe.cin.residencia.banco;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioGroup;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

import br.ufpe.cin.residencia.banco.conta.Conta;
import br.ufpe.cin.residencia.banco.conta.ContaAdapter;

//Ver anotações TODO no código
public class PesquisarActivity extends AppCompatActivity {
    BancoViewModel viewModel;
    ContaAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pesquisar);
        viewModel = new ViewModelProvider(this).get(BancoViewModel.class);
        EditText aPesquisar = findViewById(R.id.pesquisa);
        Button btnPesquisar = findViewById(R.id.btn_Pesquisar);
        RadioGroup tipoPesquisa = findViewById(R.id.tipoPesquisa);
        RecyclerView rvResultado = findViewById(R.id.rvResultado);
        adapter = new ContaAdapter(getLayoutInflater());
        rvResultado.setLayoutManager(new LinearLayoutManager(this));
        rvResultado.setAdapter(adapter);

        btnPesquisar.setOnClickListener(
                v -> {
                    String oQueFoiDigitado = aPesquisar.getText().toString();
                    //TODO implementar a busca de acordo com o tipo de busca escolhido pelo usuário

                    // Para utilizar os valores do RadioGroup podemos utilizar o comando, abaixo, do elemento tipoPesquisa.
                    switch (tipoPesquisa.getCheckedRadioButtonId()) {
                        case R.id.peloNomeCliente:
                            viewModel.buscarPeloNome(oQueFoiDigitado);
                            break;
                        case R.id.peloCPFcliente:
                            viewModel.buscarPeloCPF(oQueFoiDigitado);
                            break;
                        case R.id.peloNumeroConta:
                            viewModel.buscarPeloNumero(oQueFoiDigitado);
                            break;
                    }


                }

        );



        //TODO atualizar o RecyclerView com resultados da busca na medida que encontrar

        // Atualiza um MutableLiveData que vai sendo modificado de acordo com a escolha de pesquisa do usuário
        viewModel.contasAtuais.observe(this, contas -> {
            adapter.submitList(contas);
        });


    }

    // Esses métodos abaixo exibem a lista de todas as contas do banco,
    // quando a activity é criada. Ao editar uma conta, passará a ser exibido,
    // novamente, a lista inteira, mas com a atualização feita já aparecendo na tela
    protected void onStart() {
        super.onStart();
        viewModel.contasLista.observe(this, contasLista -> {
            adapter.submitList(contasLista);
        });

    }

    protected void onResume() {
        super.onResume();
        viewModel.contasLista.observe(this, contasLista -> {
            adapter.submitList(contasLista);
        });

    }
}