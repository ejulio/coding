
public class CeillingFan {

	public static final int HIGH = 3;
	public static final int MEDIUM = 2;
	public static final int LOW = 1;
	public static final int OFF = 0;
	
	String location;
	int speed;
	
	public CeillingFan(String location) {
		this.location = location;
		speed = OFF;
	}
	
	public void high() {
		System.out.println(location + " ceilling fan high");
		speed = HIGH;
	}
	
	public void medium() {
		System.out.println(location + " ceilling fan medium");
		speed = MEDIUM;
	}
	
	public void low() {
		System.out.println(location + " ceilling fan low");
		speed = LOW;
	}
	
	public void off() {
		System.out.println(location + " ceilling fan off");
		speed = OFF;
	}
	
	public int getSpeed() {
		return speed;
	}
}
