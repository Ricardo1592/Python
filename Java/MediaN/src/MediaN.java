import java.util.Scanner;

public class MediaN {
	
	public static double calcular_MediaN() {
		double media=0;
		
		double n;
		double soma=0;
		int qtd_n=0;
		Scanner input= new Scanner(System.in);
		
		do {
		
		n=input.nextInt();
		if (n!=0) {
			soma=soma+n;
			qtd_n=qtd_n+1;
//			System.out.println(n);
			
		}
		
		
			
		}while(n!=0);
		
		media=soma/qtd_n;
		return media;
	}
	
	public static void main(String [] args){
		
		double media=calcular_MediaN();
		System.out.println(media);
		
	}

}
