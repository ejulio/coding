
public abstract class CaffeineBeverage {

	public final void prepareRecipe() {
		boilWater();
		brew();
		pourInCup();
		addCondiments();
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
