class MCPClient:

    def __init__(
            self,
            server
    ):
        self.server = server

    async def get_tools(self):
        return await self.server.list_tools()

    async def tool_run(
            self,
            name,
            arguments
    ):
        return await self.server.call_tool(

            name,

            arguments

        )
