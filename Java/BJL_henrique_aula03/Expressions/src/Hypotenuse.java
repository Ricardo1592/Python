
/*****************************************************************************
 * 
 * PROBLEM:
 * 
 * Assume that the two short sides of a right triangle have length 3 and 4.
 * What is the length of the long side? Recall the Pythagorean Theorem: 
 * 
 * Given a = 3 and b = 4, print out sqrt(a*a + b*b), where sqrt(3*3 + 4*4).
 * 
 * @author Henrique
 *
 *****************************************************************************/
public class Hypotenuse {

	public static void main(String[] args) {
		System.out.println(Math.hypot(3, 4));
	}
}
