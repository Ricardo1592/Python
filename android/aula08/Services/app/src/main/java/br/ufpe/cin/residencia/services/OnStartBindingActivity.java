package br.ufpe.cin.residencia.services;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class OnStartBindingActivity extends AppCompatActivity {
    private int activityID = new Random().nextInt();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_music_player);

        Button botaoPlay = findViewById(R.id.botaoPlay);
        Button botaoPause = findViewById(R.id.botaoPause);
        Button botaoStartService = findViewById(R.id.botaoStartService);
        Button botaoStopService = findViewById(R.id.botaoStopService);
        Button botaoBindService = findViewById(R.id.botaoBindService);
        Button botaoUnbindService = findViewById(R.id.botaoUnbindService);
        botaoStartService.setVisibility(View.GONE);
        botaoStopService.setVisibility(View.GONE);
        botaoBindService.setVisibility(View.GONE);
        botaoUnbindService.setVisibility(View.GONE);
        TextView hashId = findViewById(R.id.hashId);
        hashId.setText(Integer.toHexString(activityID));


        botaoPlay.setOnClickListener(v -> {

        });
        botaoPause.setOnClickListener(v -> {

        });
    }

}