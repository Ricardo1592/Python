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

        // Método adicionado que utiliza o método do dao para atualizar a conta
        dao.atualizar(c);
    }

    @WorkerThread
    public void remover(Conta c) {
        //TODO implementar remover

        // Método adicionado que utiliza o método do dao para remover a conta
        dao.remover(c);
    }

    @WorkerThread
    public List<Conta> buscarPeloNome(String nomeCliente) {
        //TODO implementar busca

        // Método adicionado que utiliza o método buscarPeloNome para retornar uma lista de contas
        return dao.buscarPeloNome(nomeCliente);
    }

    @WorkerThread
    public List<Conta> buscarPeloCPF(String cpfCliente) {
        //TODO implementar busca

        // Método adicionado que utiliza o método buscarPeloCPF para retornar uma lista de contas
        return dao.buscarPeloCPF(cpfCliente);
    }

    @WorkerThread
    public Conta buscarPeloNumero(String numeroConta) {
        //TODO implementar busca

        // Método adicionado que utiliza o método buscarPelaConta para retornar uma conta
        return dao.buscarPelaConta(numeroConta);
    }

    // Método adicionado para retornar o valor total de dinheiro no banco
    public Double saldoTotal(Double saldoTotal){
        return dao.saldoTotal();
    }
}
