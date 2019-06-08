public abstract class PizzaStore {
	
	public Pizza orderPizza(String type) {
		Pizza pizza = createPizza(type);

		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		
		return pizza;
	}
	
	abstract Pizza createPizza(String type);
}

/* Primeira implementação
public class PizzaStore {

	SimplePizzaFactory factory;
	
	public PizzaStore(SimplePizzaFactory factory) {
		this.factory = factory;
	}
	
	public Pizza orderPizza(String type) {
		Pizza pizza = factory.createPizza(type);
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		
		return pizza;
	}
	
}
*/