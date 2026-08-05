from app.agents.agnet_manager import AgentManager
from app.agents.researcher import ResearchAgent
from app.agents.writer import WriterAgent
from app.llm.client import LLMClient
llm = LLMClient()
agent_manager = AgentManager()
agent_manager.register_agent(
    WriterAgent(llm)
)
agent_manager.register_agent(
    ResearchAgent(llm)
)
