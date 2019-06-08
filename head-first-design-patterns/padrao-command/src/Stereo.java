
public class Stereo {

	String description;
	
	public Stereo(String description) {
		this.description = description;
	}
	
	public void on() {
		System.out.println(description + " stereo on");
	}
	
	public void off() {
		System.out.println(description + " stereo off");
	}
	
	public void setCd() {
		System.out.println(description + " stereo set cd");
	}
	
	public void setDvd() {
		System.out.println(description + " stereo set dvd");
	}
	
	public void setRadio() {
		System.out.println(description + " stereo set radio");
	}
	
	public void setVolume(int volume) {
		System.out.println(description + " stereo set volume " + volume);
	}
}
