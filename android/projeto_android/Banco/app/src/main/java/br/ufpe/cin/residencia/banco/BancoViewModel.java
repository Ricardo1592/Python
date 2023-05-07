package br.ufpe.cin.residencia.banco;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import java.util.List;

import br.ufpe.cin.residencia.banco.conta.Conta;
import br.ufpe.cin.residencia.banco.conta.ContaDAO;
import br.ufpe.cin.residencia.banco.conta.ContaRepository;

//Ver anotações TODO no código
public class BancoViewModel extends AndroidViewModel {
    private ContaRepository repository;

    // Foram adicionados um MutableLiveData que vai atualizar uma lista de contas de acordo com os valores que forem postados pelos métodos implementados buscarPeloNome, buscarPeloCPF, buscarPeloNumero
    public LiveData<List<Conta>> contasLista;

    //
    private MutableLiveData<Double>  _saldoTotalAtual = new MutableLiveData<>();
    public LiveData<Double> bancoSaldoTotal = _saldoTotalAtual;

    private MutableLiveData<List<Conta>> _contasAtuais = new MutableLiveData<>();
    public LiveData<List<Conta>> contasAtuais = _contasAtuais;

    public BancoViewModel(@NonNull Application application) {
        super(application);
        this.repository = new ContaRepository(BancoDB.getDB(application).contaDAO());
        this.contasLista = repository.getContas();
    }

    void transferir(String numeroContaOrigem, String numeroContaDestino, double valor) {
        //TODO implementar transferência entre contas (lembrar de salvar no BD os objetos Conta modificados)

        // O método abaixo crédita o valor passado para a contaDestino e debita a contaOrigem
        new Thread(() -> {
            Conta contaOrigem = repository.buscarPeloNumero(numeroContaOrigem);
            Conta contaDestino = repository.buscarPeloNumero(numeroContaDestino);
            contaOrigem.debitar(valor);
            contaDestino.creditar(valor);
            repository.atualizar(contaOrigem);
            repository.atualizar(contaDestino);
        }).start();

    }

    void creditar(String numeroConta, double valor) {
        //TODO implementar creditar em conta (lembrar de salvar no BD o objeto Conta modificado)

        // O método abaixo crédita o valor passado como parâmetro na conta com numeroConta
        new Thread(() -> {
            Conta c = repository.buscarPeloNumero(numeroConta);
            c.creditar(valor);
            repository.atualizar(c);
        }).start();
    }

    void debitar(String numeroConta, double valor) {
        //TODO implementar debitar em conta (lembrar de salvar no BD o objeto Conta modificado)

        // O método abaixo debita o valor passado como parâmetro na conta com numeroConta
        new Thread(() -> {
            Conta c = repository.buscarPeloNumero(numeroConta);
            c.debitar(valor);
            repository.atualizar(c);
        }).start();
    }

    void buscarPeloNome(String nomeCliente) {
        //TODO implementar busca pelo nome do Cliente

        // Em um nova thread é feita a busca, no banco de dados, de uma conta pelo nome do cliente. Sendo utilizado um MutableLiveData para atualizar o objeto com a lista de contas retornadas do banco
        new Thread(() -> {
            List<Conta> contasList = repository.buscarPeloNome(nomeCliente);
            _contasAtuais.postValue(contasList);
        }).start();

    }

    void buscarPeloCPF(String cpfCliente) {
        //TODO implementar busca pelo CPF do Cliente

        // Em um nova thread é feita a busca, no banco de dados, de uma conta pelo CPF do cliente. Sendo utilizado um MutableLiveData para atualizar o objeto com a lista de contas retornadas do banco
        new Thread(() -> {
            List<Conta> contasList = repository.buscarPeloCPF(cpfCliente);
            _contasAtuais.postValue(contasList);
        }).start();

    }

    void buscarPeloNumero(String numeroConta) {
        //TODO implementar busca pelo número da Conta

        // Em um nova thread é feita a busca, no banco de dados, de uma conta pelo CPF do cliente. Sendo utilizado um MutableLiveData para atualizar o objeto com a lista de contas retornadas do banco
        new Thread(() -> {
            List<Conta> contasList = repository.buscarPelaConta(numeroConta);
            _contasAtuais.postValue(contasList);
        }).start();

    }

    // Método criado para postar um valor novo, na variável bancoSaldoTotal,
    // que representa a soma dos valores de todas as contas do banco de dados
    public void mostrarSaldoTotal(){
        new Thread(() -> {
            double novoSaldoTotal = repository.saldoTotal();
            _saldoTotalAtual.postValue(novoSaldoTotal);
        }).start();
    }

}
