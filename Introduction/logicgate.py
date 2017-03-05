class LogicGate:

	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		"""Returns the label"""
		return self.label

	def getOutput(self):
		"""Performs gate logic and returns the output"""
		self.output = self.performGateLogic()
		return self.output


class BinaryGate(LogicGate):

	def __init__(self, n):
		super().__init__(self, n)
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))

	def getPinB(self):
		return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))


class UnaryGate(LogicGate):
	
	def __init__(self, n)
		super().__init__(self, n)
		self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))		