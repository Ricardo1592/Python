package br.ufpe.cin.residencia.banco.conta;

import androidx.annotation.WorkerThread;
import androidx.lifecycle.LiveData;

import java.util.List;

//Ver anotações TODO no código
public class ContaRepository {
    private ContaDAO dao;
    private LiveData<List<Conta>> contas;

    public ContaRepository(ContaDAO dao) {
        this.dao = dao;
        this.contas = dao.contas();
    }

    public LiveData<List<Conta>> getContas() {
        return contas;
    }

    @WorkerThread
    public void inserir(Conta c) {
        dao.adicionar(c);
    }

    @WorkerThread
    public void atualizar(Conta c) {
        //TODO implementar atualizar
    }

    @WorkerThread
    public void remover(Conta c) {
        //TODO implementar remover
    }

    // Criei um método que busca todas as contas no banco de dados e retorna um objeto livedata com uma lista de contas
    @WorkerThread
    public LiveData<List<Conta>> listarTodasContasLive() {return dao.contas();}

    @WorkerThread
    public List<Conta> listarTodasContas() {return dao.todasContas();}

    @WorkerThread
    public List<Conta> buscarPeloNome(String nomeCliente) {
        //TODO implementar busca
        return null;
    }

    @WorkerThread
    public List<Conta> buscarPeloCPF(String cpfCliente) {
        //TODO implementar busca
        return null;
    }

    @WorkerThread
    public Conta buscarPeloNumero(String numeroConta) {
        //TODO implementar busca
        return null;
    }
}
