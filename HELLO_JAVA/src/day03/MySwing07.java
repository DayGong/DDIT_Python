package day03;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.SwingConstants;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	private String call="";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 256, 298);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(12, 48, 201, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("1");
			}
		});
		btn1.setBounds(12, 97, 59, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("2");
			}
		});
		btn2.setBounds(83, 97, 59, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("3");
			}
		});
		btn3.setBounds(154, 97, 59, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("4");
			}
		});
		btn4.setBounds(12, 130, 59, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("5");
			}
		});
		btn5.setBounds(83, 130, 59, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("6");
			}
		});
		btn6.setBounds(154, 130, 59, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("7");
			}
		});
		btn7.setBounds(12, 163, 59, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("8");
			}
		});
		btn8.setBounds(83, 163, 59, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("9");
			}
		});
		btn9.setBounds(154, 163, 59, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// mycall("0");
			}
		});
		btn0.setBounds(12, 196, 59, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("CALL");
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				// 마우스 클릭하면 최종 번호가 alert 나오도록
				// callAlert();
			}
		});
		btn_call.setBounds(83, 196, 130, 23);
		contentPane.add(btn_call);
		
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e);	} });
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { myclickTeacher(e); } });
		
		btn_call.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e) { mycallTeacher(); } });
	}
	
	void myclickTeacher(MouseEvent e) {
		JButton o = (JButton) e.getSource();
		String str_new = o.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old + str_new);
	}
	
	void mycallTeacher() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(this, "calling\n" + str_tel);
	}
	
	void mycall(String num) {
		call += num;
		
		tf.setText(call);
	}
	
	void callAlert() {
		JOptionPane.showMessageDialog(null, call);
	}

}
