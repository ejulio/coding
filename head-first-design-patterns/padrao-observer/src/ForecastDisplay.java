import java.util.Observable;
import java.util.Observer;


public class ForecastDisplay implements Observer, DisplayElement {

	private float currentPressure = 29.92f;
	private float lastPressure;
	
	public ForecastDisplay(Observable observable) {
		observable.addObserver(this);
	}
	
	@Override
	public void display() {
		System.out.println("Forecast: last:" + lastPressure + ", current:" + currentPressure);
	}

	@Override
	public void update(Observable o, Object arg) {
		if (o instanceof WeatherData) {
			WeatherData weatherData = (WeatherData)o;
			lastPressure = currentPressure;
			currentPressure = weatherData.getPressure();
			display();
		}
	}

}
