import java.util.ArrayList;


public class MenuTestDrive {

	public static void main(String[] args) {
		ArrayList menus = new ArrayList();
		menus.add(new PancakeHouseMenu());
		menus.add(new DinerMenu());
		menus.add(new CafeMenu());
		
		Waitress waitress = new Waitress(menus);
		
		waitress.printMenu();
	}
	
}
