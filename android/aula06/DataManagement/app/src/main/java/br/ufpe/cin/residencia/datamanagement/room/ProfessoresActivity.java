package br.ufpe.cin.residencia.datamanagement.room;

import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import br.ufpe.cin.residencia.datamanagement.R;


public class ProfessoresActivity extends AppCompatActivity {

    ProfessorAdapter adapter;
    ProfessorViewModel vm;
    int i = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_professores);
        adapter = new ProfessorAdapter(getLayoutInflater());
        vm = new ViewModelProvider(this).get(ProfessorViewModel.class);

        Button adicionarProfessor = findViewById(R.id.btn_Adiciona);
        RecyclerView rv = findViewById(R.id.rvPessoas);
        rv.setLayoutManager(new LinearLayoutManager(this));
        rv.setAdapter(adapter);

        adicionarProfessor.setOnClickListener(
                v -> {

                }
        );

    }
}