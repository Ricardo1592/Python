/*****************************************************************************
 * 
 * PROBLEM:
 * 
 * A program to compute the volume (in liters) of a six-pack of soda 
 * cans and the total volume of a six-pack and two-liter bottle.
 * 
 * @author Henrique
 *
 *****************************************************************************/
public class Volume {

	public static void main(String[] args) {
		int cansPerPack = 6;
		final double CAN_VOLUME = 0.355; // liters in a 12-ounce can
		double totalVolume = cansPerPack * CAN_VOLUME;
		
		System.out.print("A six-pack o 12-ounce cans contains = ");
		System.out.print(totalVolume);
		System.out.println(" liters.");
		
		final double BOTTLE_VOLUME = 2; // Two-Liter bottle
		totalVolume = totalVolume + BOTTLE_VOLUME;
		
		System.out.print("A six-pack and a two-liter bottle contains = ");
		System.out.print(totalVolume);
		System.out.println(" liters.");
	}

}
