import java.util.ArrayList;


public class MenuTestDrive {

	public static void main(String[] args) {
		MenuComponent pancakeHouseMenu = new Menu("PANCAKE HOUSE MENU", "Breakfast");
		MenuComponent dinerMenu = new Menu("DINER MENU", "Lunch");
		MenuComponent cafeMenu = new Menu("CAFE MENU", "Dinner");
		MenuComponent dessertMenu = new Menu("DESSERT MENU", "Dessert of course");
		MenuComponent allMenus = new Menu("ALL MENUS", "All menus combined");
		
		allMenus.add(pancakeHouseMenu);
		allMenus.add(dinerMenu);
		allMenus.add(cafeMenu);
		
		addItemToMenu(dinerMenu, "Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", true, 2.99);
		addItemToMenu(dinerMenu, "BLT", "Bacon with lettuce & tomato on whole wheat", false, 2.99);
		addItemToMenu(dinerMenu, "Soup of the day", "Suop of the day, with a side of potato salad", false, 3.29);
		addItemToMenu(dinerMenu, "HotDog", "A hot dog, with saurkraut, relish, onions, topped with cheese", false, 3.05);
		
		addItemToMenu(cafeMenu, "Veggie Burger and Air Fries", "Veggie Burger on a whole wheat bun, lettuce, tomato, and fries", true, 3.99);
		addItemToMenu(cafeMenu, "Soup of the day", "A cup of soup of the day, with a side salad", false, 3.69);
		addItemToMenu(cafeMenu, "Burrito", "A large burrito, with whole pinto beans, salsa, guacamole", true, 4.29);
		
		addItemToMenu(pancakeHouseMenu, "K&B's Pancake Breakfast", "Pancake with scrambled eggs, and toast", true, 2.99);
		addItemToMenu(pancakeHouseMenu, "Regular Pancake Breakfast", "Pancake with fried eggs, sausage", false, 2.99);
		addItemToMenu(pancakeHouseMenu, "Blueberry Pancakes", "Pancakes made with fresh blueberries", true, 3.49);
		addItemToMenu(pancakeHouseMenu, "Waffles", "Waffles with your choice of blueberries or strawberries", true, 3.59);
		
		addItemToMenu(dessertMenu, "Apple pie", "Apple pie with a flakey crust,  topped with vanilla ice cream",  true, 1.59);
		
		dinerMenu.add(dessertMenu);
		
		Waitress waitress = new Waitress(allMenus);
		
		waitress.printMenu();
		waitress.printVegetarianMenu();
	}
	
	private static void addItemToMenu(MenuComponent menu, String name, String description, boolean vegetarian, double price) {
		MenuComponent menuItem = new MenuItem(name, description, vegetarian, price);
		menu.add(menuItem);
	}
}
