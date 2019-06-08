
public class Duck implements Comparable {

	String name;
	int weight;
	
	public Duck(String name, int weight) {
		this.name = name;
		this.weight = weight;
	}
	
	public String toString() {
		return name + " weights " + weight;
	}
	
	@Override
	public int compareTo(Object obj) {
		Duck otherDuck = (Duck)obj;
		if (weight < otherDuck.weight)
			return -1;
		else if (this.weight == otherDuck.weight)
			return 0;
		
		return 1;
	}

}
