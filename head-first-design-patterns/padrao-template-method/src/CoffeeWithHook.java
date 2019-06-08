import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class CoffeeWithHook extends CaffeineBeverageWithHook {
	
	void brew() {
		System.out.println("Dripping Coffee through filter");
	}
	
	void addCondiments() {
		System.out.println("Adding sugar and milk");
	}
	
	boolean customerWantsCondiments() {
		String answer = getUserInput();
		
		return answer.toLowerCase().equals("y");
	}

	private String getUserInput() {
		String answer;
		System.out.println("Yould you like milk and sugar with your coffee (y/n)");
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		try {
			answer = in.readLine();
		} catch (IOException ioe) {
			System.err.println("IO Error trying to read your answer");
			answer = "n";
		}
		
		return answer;
	}
}
