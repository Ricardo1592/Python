package br.ufpe.cin.residencia.banco.conta;

import android.database.Cursor;
import androidx.lifecycle.LiveData;
import androidx.room.EntityInsertionAdapter;
import androidx.room.RoomDatabase;
import androidx.room.RoomSQLiteQuery;
import androidx.room.util.CursorUtil;
import androidx.room.util.DBUtil;
import androidx.sqlite.db.SupportSQLiteStatement;
import java.lang.Class;
import java.lang.Exception;
import java.lang.Override;
import java.lang.String;
import java.lang.SuppressWarnings;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.Callable;

@SuppressWarnings({"unchecked", "deprecation"})
public final class ContaDAO_Impl implements ContaDAO {
  private final RoomDatabase __db;

  private final EntityInsertionAdapter<Conta> __insertionAdapterOfConta;

  public ContaDAO_Impl(RoomDatabase __db) {
    this.__db = __db;
    this.__insertionAdapterOfConta = new EntityInsertionAdapter<Conta>(__db) {
      @Override
      public String createQuery() {
        return "INSERT OR REPLACE INTO `contas` (`numero`,`saldo`,`nomeCliente`,`cpfCliente`) VALUES (?,?,?,?)";
      }

      @Override
      public void bind(SupportSQLiteStatement stmt, Conta value) {
        if (value.numero == null) {
          stmt.bindNull(1);
        } else {
          stmt.bindString(1, value.numero);
        }
        stmt.bindDouble(2, value.saldo);
        if (value.nomeCliente == null) {
          stmt.bindNull(3);
        } else {
          stmt.bindString(3, value.nomeCliente);
        }
        if (value.cpfCliente == null) {
          stmt.bindNull(4);
        } else {
          stmt.bindString(4, value.cpfCliente);
        }
      }
    };
  }

  @Override
  public void adicionar(final Conta c) {
    __db.assertNotSuspendingTransaction();
    __db.beginTransaction();
    try {
      __insertionAdapterOfConta.insert(c);
      __db.setTransactionSuccessful();
    } finally {
      __db.endTransaction();
    }
  }

  @Override
  public LiveData<List<Conta>> contas() {
    final String _sql = "SELECT * FROM contas ORDER BY numero ASC";
    final RoomSQLiteQuery _statement = RoomSQLiteQuery.acquire(_sql, 0);
    return __db.getInvalidationTracker().createLiveData(new String[]{"contas"}, false, new Callable<List<Conta>>() {
      @Override
      public List<Conta> call() throws Exception {
        final Cursor _cursor = DBUtil.query(__db, _statement, false, null);
        try {
          final int _cursorIndexOfNumero = CursorUtil.getColumnIndexOrThrow(_cursor, "numero");
          final int _cursorIndexOfSaldo = CursorUtil.getColumnIndexOrThrow(_cursor, "saldo");
          final int _cursorIndexOfNomeCliente = CursorUtil.getColumnIndexOrThrow(_cursor, "nomeCliente");
          final int _cursorIndexOfCpfCliente = CursorUtil.getColumnIndexOrThrow(_cursor, "cpfCliente");
          final List<Conta> _result = new ArrayList<Conta>(_cursor.getCount());
          while(_cursor.moveToNext()) {
            final Conta _item;
            final String _tmpNumero;
            if (_cursor.isNull(_cursorIndexOfNumero)) {
              _tmpNumero = null;
            } else {
              _tmpNumero = _cursor.getString(_cursorIndexOfNumero);
            }
            final double _tmpSaldo;
            _tmpSaldo = _cursor.getDouble(_cursorIndexOfSaldo);
            final String _tmpNomeCliente;
            if (_cursor.isNull(_cursorIndexOfNomeCliente)) {
              _tmpNomeCliente = null;
            } else {
              _tmpNomeCliente = _cursor.getString(_cursorIndexOfNomeCliente);
            }
            final String _tmpCpfCliente;
            if (_cursor.isNull(_cursorIndexOfCpfCliente)) {
              _tmpCpfCliente = null;
            } else {
              _tmpCpfCliente = _cursor.getString(_cursorIndexOfCpfCliente);
            }
            _item = new Conta(_tmpNumero,_tmpSaldo,_tmpNomeCliente,_tmpCpfCliente);
            _result.add(_item);
          }
          return _result;
        } finally {
          _cursor.close();
        }
      }

      @Override
      protected void finalize() {
        _statement.release();
      }
    });
  }

  public static List<Class<?>> getRequiredConverters() {
    return Collections.emptyList();
  }
}
