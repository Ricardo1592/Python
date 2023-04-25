package br.ufpe.cin.residencia.background;

import static br.ufpe.cin.residencia.background.MainActivity.logThreadInfo;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class CounterViewModel extends ViewModel {
    //O que vai entrar aqui no ViewModel?
    // tudo aquilo que queremos guardar de dados,
    // independentemente de mudança de configuração
    // - qtde de toasts gerados --> INTEGER
    // - está contando tempo atualmente? --> BOOOLEAN
    // - quantos segundos já passaram? --> INTEGER

    private MutableLiveData<Integer> _segundos = new MutableLiveData<>(0);
    public LiveData<Integer> segundos = _segundos;

    private MutableLiveData<Boolean> _estaContandoTempo= new MutableLiveData<>(false);
    public LiveData<Boolean> estaContandoTempo = _estaContandoTempo;

    int toastsGerados = 0;
    private MutableLiveData<Integer> _toastsGerados = new MutableLiveData<>(0);
    public LiveData<Integer> qtdeToasts = _toastsGerados;

    public void incrementarToasts() {
        this.toastsGerados++;
        _toastsGerados.setValue(_toastsGerados.getValue()+1);
        MainActivity.logThreadInfo("incrementarToasts no ViewModel: "+toastsGerados + " | " + _toastsGerados.getValue());
    }

    public void alternarContagem() {
        if (estaContandoTempo.getValue()) {
            encerrarContagem();
        } else {
            iniciarContagem();
        }
    }

    private void encerrarContagem() {
        _estaContandoTempo.setValue(false);
        logThreadInfo("encerrarContagem()");
    }

    private void iniciarContagem() {
        _estaContandoTempo.setValue(true);
        logThreadInfo("iniciarContagem()");

        new Thread(
                () -> {
                    logThreadInfo("iniciando contagem");
                    _segundos.postValue(0);
                    while (_estaContandoTempo.getValue()) {
                        try {
                            logThreadInfo("Total de segundos: " + _segundos.getValue());
                            Thread.sleep(1000);
                            _segundos.postValue(_segundos.getValue()+1);
                        } catch (InterruptedException e) {
                            throw new RuntimeException(e);
                        }
                    }
                    logThreadInfo("encerrando contagem");
                }
        ).start();

    }
}
