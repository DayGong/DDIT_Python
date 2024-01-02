package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	JLabel lbl01, lbl02, lbl03, lbl04, lbl05, lbl06;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl01 = new JLabel("__");
		lbl01.setBounds(53, 96, 57, 15);
		contentPane.add(lbl01);
		
		lbl02 = new JLabel("__");
		lbl02.setBounds(105, 96, 57, 15);
		contentPane.add(lbl02);
		
		lbl03 = new JLabel("__");
		lbl03.setBounds(155, 96, 57, 15);
		contentPane.add(lbl03);
		
		lbl04 = new JLabel("__");
		lbl04.setBounds(207, 96, 57, 15);
		contentPane.add(lbl04);
		
		lbl05 = new JLabel("__");
		lbl05.setBounds(260, 96, 57, 15);
		contentPane.add(lbl05);
		
		lbl06 = new JLabel("__");
		lbl06.setBounds(311, 96, 57, 15);
		contentPane.add(lbl06);
		
		JButton btn = new JButton("로또생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(53, 149, 315, 23);
		contentPane.add(btn);
	}
	
	void myclick() {
		int[] arr = {
			1,2,3,4,5 ,6,7,8,9,10,
			11,12,13,14,15 ,16,17,18,19,20,
			21,22,23,24,25 ,26,27,28,29,30,
			31,32,33,34,35 ,36,37,38,39,40,
			41,42,43,44,45
		};
		
		for (int i = 0; i < 1000000; i++) {
			int rnd = (int)(Math.random()*45);
			int tmp = arr[0];
			arr[0] = arr[rnd];
			arr[rnd] = tmp;
		}
		
		lbl01.setText(String.valueOf(arr[0]));
		lbl02.setText(String.valueOf(arr[1]));
		lbl03.setText(String.valueOf(arr[2]));
		lbl04.setText(String.valueOf(arr[3]));
		lbl05.setText(String.valueOf(arr[4]));
		lbl06.setText(String.valueOf(arr[5]));
	}

}
