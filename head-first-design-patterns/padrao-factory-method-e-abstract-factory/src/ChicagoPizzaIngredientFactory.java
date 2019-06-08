
public class ChicagoPizzaIngredientFactory implements PizzaIngredientFactory {

	@Override
	public Dough createDough() {
		return new ThickCrustDough();
	}

	@Override
	public Sauce createSauce() {
		return new PlumTomatoSauce();
	}

	@Override
	public Cheese createCheese() {
		return new Mozzarela();
	}

	@Override
	public Veggies[] createVeggies() {
		return new Veggies[] {
			new BlackOlives(),
			new Spinach(),
			new Eggplant()
		};
	}

	@Override
	public Pepperoni createPepperoni() {
		return new SlicedPepperoni();
	}

	@Override
	public Clam createClam() {
		return new FrozenClam();
	}

}
