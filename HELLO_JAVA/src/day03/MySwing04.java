package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private JButton btn;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 319, 441);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl = new JLabel("출력단수");
		lbl.setBounds(47, 41, 88, 20);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setBounds(149, 41, 116, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(38, 81, 227, 29);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(38, 144, 227, 227);
		contentPane.add(ta);
	}
	
	void myclick() {
		int dan = Integer.valueOf(tf.getText());
		
		String result = "";
		for(int i = 1; i <= 9; i++) {
			result += dan + " * " + i + " = " + (dan * i) + "\n";
		}
		ta.setText(result);
	}
}
