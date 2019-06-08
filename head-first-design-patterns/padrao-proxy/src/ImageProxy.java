import java.awt.Component;
import java.awt.Graphics;
import java.net.URL;

import javax.swing.*;

public class ImageProxy implements Icon {
	ImageIcon imageIcon;
	URL imageUrl;
	Thread retrievalThread;
	boolean retrieving = false;
	
	public ImageProxy(URL imageUrl) {
		this.imageUrl = imageUrl;
	}
	
	@Override
	public int getIconHeight() {
		if (imageIcon == null) {
			return 600;
		} else {
			return imageIcon.getIconHeight();
		}
	}

	@Override
	public int getIconWidth() {
		if (imageIcon == null) {
			return 800;
		} else {
			return imageIcon.getIconWidth();
		}
	}

	@Override
	public void paintIcon(final Component c, Graphics g, int x, int y) {
		if (imageIcon != null) {
			imageIcon.paintIcon(c, g, x, y);
		} else {
			g.drawString("Loading image, please wait...", x + 300, y + 190);
			if (!retrieving) {
				retrieving = true;
				retrievalThread = new Thread(new Runnable() {
					
					@Override
					public void run() {
						try {
							imageIcon = new ImageIcon(imageUrl, "CD Cover");
							c.repaint();
						} catch (Exception e) {
							e.printStackTrace();
						}
					}
				});
				retrievalThread.start();
			}
		}
	}

}
