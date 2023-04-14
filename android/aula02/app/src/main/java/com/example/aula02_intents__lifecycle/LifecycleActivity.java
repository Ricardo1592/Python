package com.example.aula02_intents__lifecycle;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class LifecycleActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lifecycle);
    }
}