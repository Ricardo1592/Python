/*******************************************************
 *                                                     * 
 * PROBLEM:                                            *
 *                                                     *
 * Complete the design of the function called product  *
 * that consumes two double numbers and produces the   *
 * product of those numbers.                           *
 *                                                     *
 * see examples wrapped in check-expect.               *
 *  -with the form: @check_expect (({in}) -> (out))    *
 *                                                     *
 * @author Henrique Rebelo                             *
 *******************************************************/
public class ProductTwoNumbers {
	
  /**
   * Examples:
   * @check_expect (({2.0, 2.0})   -> (4.0))
   * @check_expect (({2.0, 0.0})   -> (0.0))
   * @check_expect (({2.0, 1.0})   -> (2.0))
   * @check_expect (({2.0, -1.0})  -> (-2.0))
   * @check_expect (({-2.0, -1.0}) -> (2.0))
   */  
  public static double product(double x, double y) {
   return x*y;
  }
}
