class AgentState:
    def __init__(self,message):
        self.message = message

        self.step = []

        self.finished = False

        self.answer = None