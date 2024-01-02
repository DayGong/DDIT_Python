
public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("iq: " + hum.iq);
		System.out.println("cnt_lang: " + hum.cnt_lang);
		hum.training(5);
		hum.momstouch(10);
		System.out.println("iq: " + hum.iq);
		System.out.println("cnt_lang: " + hum.cnt_lang);
	}
}
