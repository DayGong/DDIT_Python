
public class Car {
	int speed = 0;
	
	void excel(int strength) {
		speed += strength;
	}
	
	public static void main(String[] args) {
		Car c = new Car();
		System.out.println("speed: " + c.speed);
		c.excel(30);
		System.out.println("speed: " + c.speed);
	}
}
