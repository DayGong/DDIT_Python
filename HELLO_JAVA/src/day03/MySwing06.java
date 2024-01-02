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

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	private JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 294, 460);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lbl_first = new JLabel("첫별수:");
		lbl_first.setBounds(37, 31, 57, 15);
		contentPane.add(lbl_first);
		
		JLabel lbl_last = new JLabel("끝별수:");
		lbl_last.setBounds(37, 81, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(114, 28, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(114, 78, 116, 21);
		contentPane.add(tf_last);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclickTeacher();
			}
		});
		btn.setBounds(37, 124, 193, 28);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(37, 179, 193, 207);
		contentPane.add(ta);
	}

	void myclick() {
		int first = Integer.valueOf(tf_first.getText());
		int last = Integer.valueOf(tf_last.getText());
		
		String result = "";
		int sub = last - first;
		
		for (int i = 0; i <= sub; i++) {
			for (int j = 1; j <= first+i; j++) {
				result += "*";
			}
			result += "\n";
		}
		
		ta.setText(result);
		
	}
	
	String getStar(int cnt) {
		String ret = "";
		for (int i=0; i<cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	void myclickTeacher() {
		String f = tf_first.getText();
		String l = tf_last.getText();
		
		int ff = Integer.parseInt(f);
		int ll = Integer.parseInt(l);
		
		String txt="";
		
		for(int i=ff; i<=ll; i++) {
			txt += getStar(i);
		}
		
		ta.setText(txt);
	}
	
}
