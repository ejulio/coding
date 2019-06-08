from sys import exit

class Scene(object):

	def enter(self):
		pass
		
	def next_scene(self):
		pass
		
class Engine(object):

	def __init__(self, scene):
		self.scene = scene
		
	def play(self):
		while True:
			self.scene.enter()
			self.scene = self.scene.next_scene()
		
class Death(Scene):
	
	def enter(self):
		print "The aliens caught you."
		print "They are taking you to the torment room."
		print "You died."
		exit()
		
class CentralCorridor(Scene):

	def enter(self):
		print "You're in the central corridor."
		print "You should run to get the escape pod and leave the planet."
		print "There are aliens coming from the left."
		print "To which direction should you run?"
		
	def next_scene(self):
		direction = raw_input('>> ')
		if direction == '>':
			return LaserWeaponArmory()
		
		return TheBridge()
		
class LaserWeaponArmory(Scene):
	
	def enter(self):
		print "You entered the Leaser Weapon Armory."
		print "You must be quick here or the lasers will kill you."
		print "What's your next step?"
		
	def next_scene(self):
		direction = raw_input('>> ')
		if direction == '<':
			return Death()
		
		return TheBridge()
		
class TheBridge(Scene):
	
	def enter(self):
		print "Now I'm at the bridge."
		print "There are aliens everywhere."
		print "Should I jump or should I go ahead?"
		
	def next_scene(self):
		direction = raw_input('>> ')
		if direction == '<':
			return Death()
		
		return EscapePod()
	
class EscapePod(Scene):

	def enter(self):
		print "Here you are, The Escape Pod is right over here."
		print "Entering the pod."
		print "Starting the engine."
		print "Starting the engine."
		print "Starting the engine."
		print "OOOHHHHH, NOO. It's not starting."
		print "Trying one last time. The aliens are coming..."
		print "The engine started, let's go..."
		exit()
		
first_scene = CentralCorridor()
a_game = Engine(first_scene)
a_game.play()