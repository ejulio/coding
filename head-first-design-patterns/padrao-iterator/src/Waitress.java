import java.util.ArrayList;
import java.util.Iterator;

public class Waitress {

	ArrayList menus;
	
	public Waitress(ArrayList menus) {
		this.menus = menus;
	}
	
	public void printMenu() {
		for (Object obj : menus) {
			printMenu(((Menu)obj).createIterator());
		}
	}

	private void printMenu(Iterator iterator) {
		while (iterator.hasNext()) {
			MenuItem menuItem = (MenuItem)iterator.next();
			System.out.print(menuItem.getName() + ", ");
			System.out.print(menuItem.getPrice() + " -- ");
			System.out.println(menuItem.getDescription());
		}
	}
	
}
