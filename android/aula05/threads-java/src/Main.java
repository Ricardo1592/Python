public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        new Thread( ()->a()).start();
        new Thread( ()->b()).start();
        new Thread( ()->c()).start();
//        b();
//        new Thread(
//                () -> {
//                    b();
//                }
//        ).start();
//        c();
    }
    private static void a() {
        System.out.println("a");
    }

    private static void operacaoLonga() {
        int iteracoes = 500;
        int i = 0;
        int numPassos = 0;
        while (i<iteracoes) {
            int j = 0;
            while (j<iteracoes) {
                j++;
                int k = 0;
                while (k<iteracoes) {
                    numPassos++;
                    String m = String.valueOf(numPassos);
                    //System.out.println(m);
                    k++;
                }
            }
            i++;
        }
    }
    private static void b() {
        System.out.println("b");
        operacaoLonga();
        d();
    }
    private static void c() {
        e();
        System.out.println("c");
    }
    private static void d() {
        System.out.println("d");
    }
    private static void e() {
        System.out.println("e");
    }
}