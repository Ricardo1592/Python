package br.ufpe.cin.residencia.banco.conta;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import java.util.List;

import br.ufpe.cin.residencia.banco.BancoDB;

//Ver métodos anotados com TODO
public class ContaViewModel extends AndroidViewModel {

    private ContaRepository repository;
    public LiveData<List<Conta>> contas;
    private MutableLiveData<Conta> _contaAtual = new MutableLiveData<>();
    public LiveData<Conta> contaAtual = _contaAtual;

    public ContaViewModel(@NonNull Application application) {
        super(application);
        this.repository = new ContaRepository(BancoDB.getDB(application).contaDAO());
        this.contas = repository.getContas();

    }

    void inserir(Conta c) {
        new Thread(() -> repository.inserir(c)).start();
    }

    void atualizar(Conta c) {
        //TODO implementar

        // Método adicionado para atualizar uma conta, rodando em outra thread para evitar o bloqueio do programa
        new Thread(() -> repository.atualizar(c)).start();
    }

    void remover(Conta c) {
        //TODO implementar

        // Método adicionado para remover uma conta, rodando em outra thread para evitar o bloqueio do programa
        new Thread(() -> repository.remover(c)).start();
    }

    void buscarPeloNumero(String numeroConta) {
        //TODO implementar

        // Método adicionado para buscar uma conta pelo seu número,
        // rodando em outra thread para evitar o bloqueio do programa.
        // Usa também o método postValue do MutableLiveData para mostrar esse professor na tela
        new Thread(() -> {
            Conta c = repository.buscarPeloNumero(numeroConta);
            _contaAtual.postValue(c);
        }).start();
    }

}
