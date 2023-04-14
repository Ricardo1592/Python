package com.example.aula02_intents__lifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final Button btnIntentExplicitoLifecycle = findViewById(R.id.btnIntentExplicito);
        final Button btnIntentImplicitoWeb = findViewById(R.id.btnIntentImplicitoWeb);
        final Button btnIntentImplicitoMapa = findViewById(R.id.btnIntentImplicitoMapa);

        btnIntentExplicitoLifecycle.setOnClickListener(
                v -> {
                    //ir para a LifecycleActivity
                    //Intent Explícito - estamos definindo qual componente vai ser executado
                    Intent i = new Intent(
                            getApplicationContext(),
                            LifecycleActivity.class
                    );
                    startActivity(i);
                }
        );



    }
}