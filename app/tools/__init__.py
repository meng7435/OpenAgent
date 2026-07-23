from app.tools.registry import ToolRegistry
from app.tools.weather import WeatherTool
from app.tools.manager import ToolManager


def create_tool_manager():
    tool_registry = ToolRegistry()

    tool_registry.register(WeatherTool())

    return ToolManager(tool_registry)
