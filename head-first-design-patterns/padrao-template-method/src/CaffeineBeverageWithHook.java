
public abstract class CaffeineBeverageWithHook {

	public final void prepareRecipe() {
		boilWater();
		brew();
		pourInCup();
		if (customerWantsCondiments())
			addCondiments();
	}
	
	boolean customerWantsCondiments() {
		return true;
	}

	abstract void addCondiments();

	abstract void brew();

	public void boilWater() {
		System.out.println("Boiling water");
	}
	
	public void pourInCup() {
		System.out.println("Pouring into cup");
	}
}
