from app.mcp.server import MCPServer

from app.tools.weather import WeatherTool

server = MCPServer()

server.register_tool(
    WeatherTool()
)
