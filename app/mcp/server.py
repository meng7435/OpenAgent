class MCPServer:
    def __init__(self):
        self.tools = {}

    def register_tool(self, tool):
        self.tools[tool.name] = tool

    async def list_tools(self):
        result = []
        for tool in self.tools.values():
            result.append({
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.parameters()
                }
            })
        return result

    async def call_tool(
            self,
            name,
            arguments
    ):
        tool = self.tools.get(name)

        if not tool:
            return {
                "error":
                    "tool not found"
            }

        return await tool.execute(
            arguments
        )
