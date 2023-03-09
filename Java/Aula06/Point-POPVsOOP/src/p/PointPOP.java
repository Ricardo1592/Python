package p;

public class PointPOP {
	
	public static void setX(PointCoord pc, int x) {
		pc.x = x;
	}
	
	public static void setY(PointCoord pc, int y) {
		pc.y = y;
	}
	
	public static int getX(PointCoord pc) {
		return pc.x;
	}
	
	public static int getY(PointCoord pc) {
		return pc.y;
	}

	public static void main(String[] args) {
		PointCoord pc = new PointCoord();
		PointCoord pc2 = new PointCoord();
		PointPOP.setX(pc, 10);
		setY(pc, 20);
		System.out.println(getX(pc));
		System.out.println(getY(pc));

	}

}

// Struct
class PointCoord{
	int x;
	int y;
}
