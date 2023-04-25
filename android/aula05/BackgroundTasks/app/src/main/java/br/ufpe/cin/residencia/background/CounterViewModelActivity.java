package br.ufpe.cin.residencia.background;

import static br.ufpe.cin.residencia.background.MainActivity.logThreadInfo;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.Observer;
import androidx.lifecycle.ViewModelProvider;

public class CounterViewModelActivity extends AppCompatActivity {

    private TextView statusOperacao;
    private TextView contadorToasts;
    private Button botaoContagem;

    private CounterViewModel counterViewModel;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_countdown);
        counterViewModel = new ViewModelProvider(this).get(CounterViewModel.class);


        statusOperacao = findViewById(R.id.statusOperacao);
        contadorToasts = findViewById(R.id.contadorToasts);
        botaoContagem = findViewById(R.id.btnLongOperation);
        Button btnToast = findViewById(R.id.btnToast);

        btnToast.setOnClickListener(
                v -> {
                    logThreadInfo("Callback do botão de toasts");
                    counterViewModel.incrementarToasts();
                }
        );

        counterViewModel.qtdeToasts.observe(
                this,
                new Observer<Integer>() {
                    @Override
                    public void onChanged(Integer qtde) {
                        contadorToasts.setText(getString(R.string.contadorToasts, qtde));
                    }
                }
        );

        botaoContagem.setOnClickListener(
                v -> {
                    logThreadInfo("clicou no botão de contagem");
                    counterViewModel.alternarContagem();
                }
        );

        counterViewModel.estaContandoTempo.observe(
                this,
                estaContandoTempoAgora -> {
                    if (estaContandoTempoAgora) {
                        botaoContagem.setText(R.string.pararContador);
                    }
                    else {
                        botaoContagem.setText(R.string.iniciarContador);
                    }
                }
//        new Observer<Boolean>() {
//            @Override
//            public void onChanged(Boolean estaContandoTempoAgora) {
//                if (estaContandoTempoAgora) {
//                    botaoContagem.setText(R.string.pararContador);
//                }
//                else {
//                    botaoContagem.setText(R.string.iniciarContador);
//                }
//
//            }
//        }
        );

        counterViewModel.segundos.observe(
                this,
                quantoTempoPassou -> {
                    if (quantoTempoPassou > 1) {
                        statusOperacao.setText(quantoTempoPassou + " segundos passaram");
                    }
                    else {
                        statusOperacao.setText(quantoTempoPassou + " segundo passou");
                    }
                }
        );


    }
}