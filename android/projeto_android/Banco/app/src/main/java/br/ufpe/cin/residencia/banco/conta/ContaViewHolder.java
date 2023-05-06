package br.ufpe.cin.residencia.banco.conta;

import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.text.NumberFormat;

import br.ufpe.cin.residencia.banco.R;

//Ver anotações TODO no código
public class ContaViewHolder  extends RecyclerView.ViewHolder {
    TextView nomeCliente = null;
    TextView infoConta = null;
    ImageView icone = null;

    public ContaViewHolder(@NonNull View linha) {
        super(linha);
        this.nomeCliente = linha.findViewById(R.id.nomeCliente);
        this.infoConta = linha.findViewById(R.id.infoConta);
        this.icone = linha.findViewById(R.id.icone);
    }

    void bindTo(Conta c) {
        // adicionei as variáveis saldo e saldo_string
        Double saldo = c.saldo;
        // O comando abaixo transforma um double e já o formata com R$ por isso estava repetindo duas vezes antes
//        String saldo_string = NumberFormat.getCurrencyInstance().format(c.saldo);
        String saldo_string = NumberFormat.getInstance().format(c.saldo);
        this.nomeCliente.setText(c.nomeCliente);
        this.infoConta.setText(c.numero + " | " + "Saldo atual: R$ " + saldo_string);

        //TODO Falta atualizar a imagem de acordo com o valor do saldo atual

        // Lógica adicionada para atualizar a imagem de acordo com o valor em conta
        if (saldo >= 0.0) {
            this.icone.setImageResource(R.drawable.ok);
        }
        else{
            this.icone.setImageResource(R.drawable.delete);
        }

        this.addListener(c.numero, saldo_string, c.nomeCliente, c.cpfCliente);
    }

    public void addListener(String numeroConta, String saldoConta, String nomeConta, String cpfConta) {
        this.itemView.setOnClickListener(
                v -> {
                    Context c = this.itemView.getContext();
                    Intent i = new Intent(c, EditarContaActivity.class);
                    //TODO Está especificando a Activity mas não está passando o número da conta pelo Intent
                    // Adicionei o método i.putExtra para capturar o número da conta e joga-lo para outra activity
                    i.putExtra("numeroConta", numeroConta);
                    i.putExtra("cpfConta", cpfConta);
                    i.putExtra("nomeConta", nomeConta);
                    i.putExtra("saldoConta", saldoConta);
                    c.startActivity(i);
                }
        );
    }
}
