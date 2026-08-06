import asyncio

from litellm import query

from app.agents import ResearchAgent, WriterAgent
from app.agents.analyst import AnalysisAgent
from app.nodes.analysis import AnalysisNode
from app.nodes.research import ResearchNode
from app.nodes.writer import WriterNode
from app.workflow.graph import WorkflowGraph
from app.workflow.state import WorkflowState

from app.llm.client import LLMClient
llm = LLMClient()
async def main():
    graph = WorkflowGraph()

    graph.add_node(
        ResearchNode(
            ResearchAgent(llm)
        )
    )

    graph.add_node(
        AnalysisNode(
            AnalysisAgent(llm)
        )
    )

    graph.add_node(
        WriterNode(
            WriterAgent(llm)
        )
    )

    graph.add_edge(

        "research",

        "analysis"

    )

    graph.add_edge(

        "analysis",

        "writer"

    )

    graph.add_edge(

        "writer",

        None

    )
    state = WorkflowState(

        query="分析苹果公司"

    )

    result = await graph.run(
        state
    )

    print(
        result.report
    )

asyncio.run(main())