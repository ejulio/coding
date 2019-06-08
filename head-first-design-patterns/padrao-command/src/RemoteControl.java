
public class RemoteControl {
	Command[] onCommands;
	Command[] offCommands;
	Command undoCommand;
	
	public RemoteControl() {
		onCommands = new Command[7];
		offCommands = new Command[7];
		
		Command noCommand = new NoCommand();
		undoCommand = noCommand;
		for (int i = 0; i < 7; i++) {
			onCommands[i] = noCommand;
			offCommands[i] = noCommand;
		}
	}
	
	public void setCommand(int slot, Command onCommand, Command offCommand) {
		onCommands[slot] = onCommand;
		offCommands[slot] = offCommand;
	}
	
	public void onButtonWasPushed(int slot) {
		onCommands[slot].execute();
		undoCommand = onCommands[slot];
	}
	
	public void offButtonWasPushed(int slot) {
		offCommands[slot].execute();
		undoCommand = offCommands[slot];
	}
	
	public void undoButtonWasPushed() {
		undoCommand.undo();
	}
	
	public String toString() {
		StringBuffer stringBuf = new StringBuffer();
		stringBuf.append("\n-- RemoteControl --\n");
		for (int i = 0; i < onCommands.length; i++) {
			stringBuf
				.append("[slot " + i + "] ")
				.append(onCommands[i].getClass().getName())
				.append(" ")
				.append(offCommands[i].getClass().getName())
				.append("\n");
		}
		
		return stringBuf.toString();
	}
}
