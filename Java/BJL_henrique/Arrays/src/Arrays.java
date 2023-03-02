public class Arrays {

	public static void main(String[] args) {
		final int ARRAY_LENGTH = 10;
		double [] values = new double [ARRAY_LENGTH];
		values[4] = 35; // 5th position
		System.out.println(values[4]);
		System.out.println(values[0]);
		for (int i = 0; i < values.length; i++) {
			System.out.println("values["+i+"] = "+values[i]);
		}
		System.out.println();
		double [] moreValues = {32, 54, 67.5, 29, 35, 80, 115, 44.5, 100, 65};
		for (int i = 0; i < moreValues.length; i++) {
			System.out.println("moreValues["+i+"] = "+moreValues[i]);
		}
		System.out.println();
		moreValues[4] = 350; // 5th position
		for (int i = 0; i < moreValues.length; i++) {
			System.out.println("moreValues["+i+"] = "+moreValues[i]);
		}
		System.out.println();
		for (int i = 0; i < moreValues.length; i++) {
			moreValues[i] = moreValues[i] + 1;
			System.out.printf("moreValues[%d] = %.1f%n",i, moreValues[i]);
		}
	} 

}
