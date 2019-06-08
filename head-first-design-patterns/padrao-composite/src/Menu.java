import java.util.ArrayList;
import java.util.Iterator;

public class Menu extends MenuComponent {
	
	ArrayList menuComponents = new ArrayList();
	String name;
	String description;
	
	public Menu(String name, String description) {
		this.name = name;
		this.description = description;
	}
	
	public void add(MenuComponent menuComponent) {
		menuComponents.add(menuComponent);
	}
	
	public void remove(MenuComponent menuComponent) {
		menuComponents.remove(menuComponent);
	}
	
	public MenuComponent getChild(int i) {
		return (MenuComponent)menuComponents.get(i);
	}
	
	public String getName() {
		return name;
	}
	
	public String getDescription() {
		return description;
	}
	
	public void print() {
		System.out.println();
		System.out.print(getName());
		System.out.println(", " + getDescription());
		System.out.println("---------------------");
		for (Object obj : menuComponents) {
			MenuComponent menuComponent = (MenuComponent)obj;
			menuComponent.print();
		}
	}
	
	public Iterator createIterator() {
		return new CompositeIterator(menuComponents.iterator());
	}
}
