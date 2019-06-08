
public class RemoteControlTest {

	public static void main(String[] args) {
		/*SimpleRemoteControl remote = new SimpleRemoteControl();
		Light light = new Light();
		LightOnCommand lightOn = new LightOnCommand(light);
		GarageDoor garageDoor = new GarageDoor();
		GarageDoorOpenCommand garageOpen = new GarageDoorOpenCommand(garageDoor);
		
		remote.setCommand(lightOn);
		remote.buttonWasPressed();
		remote.setCommand(garageOpen);
		remote.buttonWasPressed();*/
		
		RemoteControl remoteControl  = new RemoteControl();
		
		Light livingRoomLight = new Light("Living room");
		Light kitchenLight = new Light("Kitchen");
		GarageDoor garageDoor = new GarageDoor();
		Stereo stereo = new Stereo("Living room");
		CeillingFan ceillingFan = new CeillingFan("Living room");
		
		LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
		LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
		LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
		LightOffCommand kitchenLightOff = new LightOffCommand(kitchenLight);
		GarageDoorUpCommand garageDoorUp = new GarageDoorUpCommand(garageDoor);
		GarageDoorDownCommand garageDoorDown = new GarageDoorDownCommand(garageDoor);
		CeillingFanHighCommand ceillingFanHigh = new CeillingFanHighCommand(ceillingFan);
		CeillingFanOffCommand ceillingFanOff = new CeillingFanOffCommand(ceillingFan);
		
		
		StereoOnWithCdCommand stereoOnWithCd = new StereoOnWithCdCommand(stereo);
		StereoOffCommand stereoOff = new StereoOffCommand(stereo);
		
		remoteControl.setCommand(0, livingRoomLightOn, livingRoomLightOff);
		remoteControl.setCommand(1, kitchenLightOn, kitchenLightOff);
		remoteControl.setCommand(2, garageDoorUp, garageDoorDown);
		remoteControl.setCommand(3, stereoOnWithCd, stereoOff);
		remoteControl.setCommand(4, ceillingFanHigh, ceillingFanOff);
		
		remoteControl.onButtonWasPushed(0);
		remoteControl.offButtonWasPushed(0);
		remoteControl.onButtonWasPushed(1);
		remoteControl.offButtonWasPushed(1);
		remoteControl.onButtonWasPushed(2);
		remoteControl.offButtonWasPushed(2);
		remoteControl.onButtonWasPushed(3);
		remoteControl.offButtonWasPushed(3);
		remoteControl.onButtonWasPushed(4);
		remoteControl.undoButtonWasPushed();
		remoteControl.offButtonWasPushed(4);
		remoteControl.undoButtonWasPushed();
		
		System.out.println("PARTY TIME");
		
		Command[] partyOn = { garageDoorUp, ceillingFanHigh, livingRoomLightOn };
		Command[] partyOff = { garageDoorDown, ceillingFanOff, livingRoomLightOff };
	
		MacroCommand partyOnMacro = new MacroCommand(partyOn);
		MacroCommand partyOffMacro = new MacroCommand(partyOff);
		
		remoteControl.setCommand(5, partyOnMacro, partyOffMacro);
		System.out.println("PARTY STARTING");
		remoteControl.onButtonWasPushed(5);
		System.out.println("PARTY ENDING");
		remoteControl.offButtonWasPushed(5);
		
		System.out.println(remoteControl.toString());
	}
	
}
