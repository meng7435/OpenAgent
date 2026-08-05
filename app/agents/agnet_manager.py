from app.agents.base import BaseAgent


class AgentManager:

    def __init__(self):
        self.agents={}

    def register_agent(self,agent):
        self.agents[agent.name]=agent

    def get(self,name):
        return self.agents.get(name)

    def descriptions(self):
        result = []

        for agent in self.agents.values():
            result.append(

                {
                    "name":
                        agent.name,

                    "description":
                        agent.description

                }

            )

        return result