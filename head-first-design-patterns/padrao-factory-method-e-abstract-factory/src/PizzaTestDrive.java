
public class PizzaTestDrive {

	public static void main(String[] args) {
		
		PizzaStore nyPizzaStore = new NYStylePizzaStore();
		PizzaStore chicagoPizzaStore = new ChicagoStylePizzaStore();
		
		Pizza pizza;
		pizza = nyPizzaStore.orderPizza("cheese");
		System.out.println("Ethan ordered a " + pizza.getName());
		
		pizza = chicagoPizzaStore.orderPizza("cheese");
		System.out.println("Joel ordered a " + pizza.getName());
	}
	
}
