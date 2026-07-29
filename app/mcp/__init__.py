from app.mcp.server import MCPServer

from app.tools.weather import WeatherTool
from app.tools.search import SearchTool

server = MCPServer()

server.register_tool(
    WeatherTool()
)
server.register_tool(
    SearchTool()
)
