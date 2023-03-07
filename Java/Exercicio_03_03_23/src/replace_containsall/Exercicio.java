package replace_containsall;

import java.util.ArrayList;

public class Exercicio {
	
	public static String replace(String s, char target, char replacement) {
		String palavra_nova="";
		char sCharArray [] = s.toCharArray();
		for (char letra : sCharArray) {
			
			if (letra==target) {
				letra=replacement;
				palavra_nova=palavra_nova + replacement;
				
			}
			else {
			
				palavra_nova=palavra_nova+letra;
				
			}
		}
		
		return palavra_nova;
	}	
	
	public static int containsAll(ArrayList <String> a1, ArrayList <String> a2) {
		
		int qtd_indices= a1.size();
		
		return qtd_indices;
		
	}
	
	
	public static void main(String [] args) {
		ArrayList <String> a1 = new ArrayList<>();
		ArrayList <String> a2 = new ArrayList<>();
		String palavra;
		palavra=replace("Bananana", 'n', 'r');
		System.out.println(palavra);
		containsAll(a1, a2);
		
	
		
	}
	
	
	

}
