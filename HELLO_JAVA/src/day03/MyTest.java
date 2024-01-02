package day03;

public class MyTest {
	public static void showDan(int dan) {
		System.out.println(dan + " * " + 1 + " = " + (dan * 1));
		System.out.println(dan + " * " + 2 + " = " + (dan * 2));
		System.out.println(dan + " * " + 3 + " = " + (dan * 3));
		System.out.println(dan + " * " + 4 + " = " + (dan * 4));
		// System.out.println(dan + " * " + 5 + " = " + (dan * 5));
		System.out.println(dan + " * " + 6 + " = " + (dan * 6));
		System.out.println(dan + " * " + 7 + " = " + (dan * 7));
		System.out.println(dan + " * " + 8 + " = " + (dan * 8));
		System.out.println(dan + " * " + 9 + " = " + (dan * 9));
		System.out.println();
	}
	
	public static void main(String[] args) {
		showDan(9);
		showDan(7);
		showDan(4);
		showDan(2);
	}
}
