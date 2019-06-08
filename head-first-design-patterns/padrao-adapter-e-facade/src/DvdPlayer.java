
public class DvdPlayer {

	String movie;
	
	public void on() {
		System.out.println("Top-O-Line DVD Player on");
	}

	public void play(String movie) {
		this.movie = movie;
		System.out.println("Top-O-Line playing \"" + movie + "\"");
	}
	
	public String toString() {
		return "Top-O-Line DVD Player";
	}

	public void stop() {
		System.out.println("Top-O-Line DVD Player stopper \"" + movie + "\"");
	}

	public void eject() {
		System.out.println("Top-O-Line DVD Player eject");
	}

	public void off() {
		System.out.println("Top-O-Line DVD Player off");
	}

}
