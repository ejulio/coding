import java.net.URL;

import javax.swing.Icon;
import javax.swing.JFrame;


public class ImageProxyTestDrive {

	public static void main(String[] args) throws Exception {
		ImageProxyTestDrive testDrive = new ImageProxyTestDrive();
	}
	
	public ImageProxyTestDrive() throws Exception {
		JFrame frame = new JFrame("Image proxy");
		
		URL initialUrl = new URL("http://blog.codinghorror.com/content/images/uploads/2005/09/6a0120a85dcdae970b0128776fb8b7970c-pi.jpg");
		Icon icon = new ImageProxy(initialUrl);
		ImageComponent imageComponent = new ImageComponent(icon);
		frame.getContentPane().add(imageComponent);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(800, 600);
		frame.setVisible(true);
	}
}
