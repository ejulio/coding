
public class NYStylePizzaStore extends PizzaStore {

	@Override
	Pizza createPizza(String type) {
		Pizza pizza = null;
		PizzaIngredientFactory ingredientFactory = new NYPizzaIngredientFactory();
		if (type.equals("cheese")) {
			pizza = new CheesePizza(ingredientFactory);
			pizza.setName("Pizza de Queijo estilo Nova York");
		}
		else if (type.equals("pepperoni")) {
			pizza = new PepperoniPizza(ingredientFactory);
			pizza.setName("Pizza de calabresa no estilo Nova York");
		}
		else if (type.equals("clam")) {
			pizza = new ClamPizza(ingredientFactory);
			pizza.setName("Pizza de Mariscos no estilo Nova York");
		}
		else if (type.equals("veggie")) {
			pizza = new VeggiePizza(ingredientFactory);
			pizza.setName("Pizza vegetariana no estilo Nova York");
		}
		return pizza;
	}

}
