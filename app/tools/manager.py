from tenacity import retry_unless_exception_type
from app.tools.weather import WeatherTool


class ToolManager:
    def __init__(self, registry):
        self.registry = registry

    def get_schemas(self):

        schemas = []

        for tool in self.registry.all_tools():
            schemas.append(
                tool.schema()
            )

        return schemas

    async def execute(self, name, message):
        tool = self.registry.get(name)

        if not tool:
            return {"error": "tool not found"}
        result = await tool.execute(**message)

        return result

