package point;

public class Point {
	
	private int x;
	private int y;
	
	public Point(){};  //Pode-se colocar miad de um método inicializador
	
	public Point(int x, int y) {
		
		this.x=x; // Método inicializador/construtor 
		this.y=y;
		
	}
	
	public int getX() {
		return this.x;
	}
	public int getY() {
		return this.y;
	}

	public void setX(int x) {
		this.x=x;
	}

	public void setY(int y){
		this.y=y;
	}
	
	@Override
	public String toString() {
		return "Point[x="+this.x+ ", y="+this.y+"]"; 
	}
	
	public static void main(String [] args) {
		
		Point p1 = new Point();
		p1.setX(2);
		p1.setY(4);
		System.out.println(p1.toString());
		System.out.println(p1);
		
	}

}
