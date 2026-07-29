class SearchTool:
    name = "search"
    description = "网页搜索城市景点信息，传入完整城市名称查询当地游玩地点"

    @staticmethod
    def input_schema():
        return {
            "type": "object",
            "required": ["city"],  # 必须声明必填
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市完整名称，例如：武汉市、北京市，建议带上「市」字，不要简写"
                }
            },
        }

    async def execute(self, city: str):
        if city == "上海市":
            return ["东方明珠", "外滩"]
        return []