import java.util.Scanner;

/*****************************************************************************
 * 
 * PROBLEM:
 * 
 * Addition program that inputs two numbers then displays their sum.
 * 
 * Given sum = number 1 + number2, where number1 = 3 and number2 = 4, 
 * print out sum = 7.
 * 
 * @author Henrique
 *
 *****************************************************************************/
public class Addition {

	public static void main(String[] args) {
		// create a Scanner to obtain input from the console
        Scanner input = new Scanner(System.in);
		
        // variable declarations
		int number1; // first number to add
		int number2; // second number to add
		int sum; // sum of number1 and number2 -> number1 + number2
		
		// the inputs
		System.out.println("Enter firt integer number: "); //prompt
		number1 = input.nextInt(); // read first number from user		
	    System.out.println("Enter second integer number: "); //prompt
	    number2 = input.nextInt(); // read second number from user
				
	    // the sum
		sum = number1 + number2; // add numbers, the store total in sum
		
		// the output
		System.out.println("Sum is = "+sum); // display sum
	}

}
