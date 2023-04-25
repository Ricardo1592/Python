package br.ufpe.cin.residencia.services;

import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class MusicPlayerWithBindingActivity extends AppCompatActivity {
    String activityID = Integer.toHexString(new Random().nextInt());

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
        botaoStartService.setVisibility(View.VISIBLE);
        botaoStopService.setVisibility(View.VISIBLE);
        botaoBindService.setVisibility(View.VISIBLE);
        botaoUnbindService.setVisibility(View.VISIBLE);
        TextView hashId = findViewById(R.id.hashId);
        hashId.setText(activityID);

        botaoPlay.setOnClickListener(v -> {

        });
        botaoPause.setOnClickListener(v -> {

        });
        botaoStartService.setOnClickListener(v -> {

        });
        botaoStopService.setOnClickListener(v -> {

        });
        botaoBindService.setOnClickListener(v -> {

        });
        botaoUnbindService.setOnClickListener(v -> {

        });

    }

}