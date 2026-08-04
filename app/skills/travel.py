class TravelSkill:
    name = "travel_plan"

    description = "根据城市生成旅游计划"

    def parameters(self):
        return {

            "type": "object",

            "properties": {

                "city": {

                    "type": "string",

                    "description": "城市完整名称，例如：武汉市、北京市，建议带上「市」字，不要简写"

                }

            },

            "required": [
                "city"
            ]

        }

    def __init__(self, mcp):
        self.mcp = mcp

    async def execute(
            self,
            city
    ):
        weather = await self.mcp.tool_run(
            "weather",
            city
        )

        search = await self.mcp.tool_run(
            "search",
            {"city":f'{city}景点'}
        )

        return {

            "weather": weather,

            "spots": search

        }
