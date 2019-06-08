
public class GumballMachine {

	State soldOutState;
	State noQuarterState;
	State hasQuarterState;
	State soldState;
	State winnerState;
	
	State state;
	
	int count = 0;
	
	public GumballMachine(int count) {
		this.count = count;
		soldOutState = new SoldOutState(this);
		noQuarterState = new NoQuarterState(this);
		hasQuarterState = new HasQuarterState(this);
		soldState = new SoldState(this);
		winnerState = new WinnerState(this);
		
		if (count > 0) {
			state = noQuarterState;
		} else {
			state = soldOutState;
		}
	}
	
	public void insertQuarter() {
		state.insertQuarter();
	}
	
	public void ejectQuarter() {
		state.ejectQuarter();
	}
	
	public void turnCrank() {
		state.turnCrank();
		state.dispense();
	}
	
	public void releaseBall() {
		System.out.println("A gumball comes rolling out the slot...");
		if (count > 0) {
			count--;
		}
	}
	
	public void refill(int count) {
		this.count = count;
		state = noQuarterState;
	}
	
	public void setState(State state) {
		this.state = state;
	}
	
	public State getSoldOutState() {
		return soldOutState;
	}
	
	public State getNoQuarterState() {
		return noQuarterState;
	}
	
	public State getHasQuarterState() {
		return hasQuarterState;
	}
	
	public State getSoldState() {
		return soldState;
	}
	
	public State getWinnerState() {
		return winnerState;
	}
	
	public int getCount() {
		return count;
	}
	
	public String toString() {
		return String.valueOf(state);
	}
}
