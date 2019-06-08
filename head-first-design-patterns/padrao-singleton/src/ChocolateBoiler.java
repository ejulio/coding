
public class ChocolateBoiler {
	private boolean empty;
	private boolean boiled;
	//private static ChocolateBoiler uniqueInstance;
	
	//public static synchronized ChocolateBoiler getInstance() {
	//	if (uniqueInstance == null)
	//		uniqueInstance = new ChocolateBoiler();
		
	//	return uniqueInstance;
	//}
	
	private volatile static ChocolateBoiler uniqueInstance;
	
	public static ChocolateBoiler getInstance() {
		if (uniqueInstance == null) {
			synchronized (ChocolateBoiler.class) {
				if (uniqueInstance == null)
					uniqueInstance = new ChocolateBoiler();
			}
		}
		return uniqueInstance;
	}
	
	private ChocolateBoiler() {
		empty = true;
		boiled = false;
	}
	
	public void fill() {
		if (isEmpty()) {
			empty = false;
			boiled = false;
		}
	}
	
	public void drain() {
		if (!isEmpty() && isBoiled()) {
			empty = true;
		}
	}
	
	public void boil() {
		if (!isEmpty() && !isBoiled()) {
			boiled = true;
		}
	}
	
	public boolean isEmpty() {
		return empty;
	}
	
	public boolean isBoiled() {
		return boiled;
	}

}
