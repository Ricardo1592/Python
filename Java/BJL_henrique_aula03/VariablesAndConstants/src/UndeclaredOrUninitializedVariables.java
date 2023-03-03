
public class UndeclaredOrUninitializedVariables {

	public static void main(String[] args) { 
		int cansPerPack = 6;
		final double CAN_VOLUME = 0.355; // liters in a 12-ounce can
		double totalVolume = cansPerPack * CAN_VOLUME;
		System.out.println("total volume = "+totalVolume);
	}	
}
