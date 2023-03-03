import java.util.Scanner;

public class Media3 {
	public static void main(String [] args){
		
		System.out.println("Digite 3 números");
		Scanner input= new Scanner(System.in);
		int n1;
		int n2;
		int n3;
		n1=input.nextInt();
		n2=input.nextInt();
		n3=input.nextInt();
		float media;
		media=(n1+n2+n3)/3;
		System.out.print("A média é: " +media);
		
	}

}
