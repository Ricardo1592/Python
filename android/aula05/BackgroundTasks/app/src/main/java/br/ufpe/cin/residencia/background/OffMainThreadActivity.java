package br.ufpe.cin.residencia.background;

import static br.ufpe.cin.residencia.background.MainActivity.JSON_URL;
import static br.ufpe.cin.residencia.background.MainActivity.getContentFromURL;
import static br.ufpe.cin.residencia.background.MainActivity.logThreadInfo;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class OffMainThreadActivity extends AppCompatActivity {

    private int toastsGerados = 0;
    private int iteracoes = 30;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tasks);

        Button btnToast = findViewById(R.id.btnToast);
        Button btnNetwork = findViewById(R.id.btnNetwork);
        Button btnLongOperation = findViewById(R.id.btnLongOperation);
        TextView contadorToasts = findViewById(R.id.contadorToasts);
        TextView contadorSegundos = findViewById(R.id.contaSegundos);
        TextView resultadoOperacaoLonga = findViewById(R.id.resultadoOperacao);
        TextView resultadoOperacaoRede = findViewById(R.id.resultadoOperacaoRede);

        contadorToasts.setText(getString(R.string.contadorToasts, toastsGerados));
        btnToast.setOnClickListener(
                v -> {
                    logThreadInfo("botão do Toast de MainThreadActivity");
                    toastsGerados++;
                    String msg = getString(R.string.contadorToasts, toastsGerados);
                    Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
                    contadorToasts.setText(msg);
                }
        );

        btnLongOperation.setOnClickListener(
                v -> {
                    logThreadInfo("Iniciando operação longa, esta mensagem é antes de iniciar a thread");
                    resultadoOperacaoLonga.setText(R.string.comecouOperacao);
                    new Thread(() -> {
                        logThreadInfo("Iniciando execução da thread");
                        int i = 0;
                        int numPassos = 0;
                        while (i < iteracoes) {
                            int j = 0;
                            while (j < iteracoes) {
                                j++;
                                int k = 0;
                                while (k < iteracoes) {
                                    numPassos++;
                                    String m = String.valueOf(numPassos);
                                    //logThreadInfo(m);
                                    runOnUiThread(() -> contadorSegundos.setText(m));
                                    k++;
                                }
                            }
                            i++;
                        }
                        int finalNumPassos = numPassos;
                        runOnUiThread(
                                () -> {
                                    String msg = getString(R.string.terminouOperacao, finalNumPassos);
                                    resultadoOperacaoLonga.setText(msg);
                                    logThreadInfo("esta mensagem roda ao final da execução da thread, só que a partir da main thread");
                                }
                        );
                    }).start();
                    logThreadInfo("Esta mensagem está logo depois de iniciar a thread");

                }
        );

        btnNetwork.setOnClickListener(
                v -> {
                    logThreadInfo("Iniciando operação de rede");
                    new Thread(
                            () -> {
                                try {
                                    logThreadInfo("Iniciando operação de rede dentro da thread");
                                    String conteudo = getContentFromURL(JSON_URL);
                                    runOnUiThread(
                                            () -> resultadoOperacaoRede.setText(conteudo)
                                    );
                                    logThreadInfo("Terminei operação de rede");
                                } catch (IOException e) {
                                    //Toast.makeText(this, "Houve um erro ao baixar o arquivo.", Toast.LENGTH_SHORT).show();

                                    runOnUiThread(
                                            () -> resultadoOperacaoRede.setText("Erro: " + e.getMessage())
                                    );
                                }
                            }
                    ).start();

                }
        );
    }

}