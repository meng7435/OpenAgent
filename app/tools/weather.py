from app.tools.base import BaseTool
from dotenv import load_dotenv
import os
import httpx

load_dotenv()


class WeatherTool(BaseTool):
    name = "weather"
    description = '''
    查询城市天气

    输入:
    城市名称
    '''
    API_KEY = os.getenv("WEATHER_API_KEY")
    BASE_URL = os.getenv("WEATHER_BASE_URL")

    async def execute(self, city: str):
        #  构造请求参数
        params = {
            "q": city,  # 城市名
            "appid": self.API_KEY,
            "units": "metric",  # 使用摄氏度
            "lang": "zh_cn"  # 中文返回
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()

                return {
                    "city": data["name"],
                    "weather": data["weather"][0]["description"],
                    "temp": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"]
                }
        except Exception as e:
            print("【请求捕获异常】", type(e), str(e))
            return {"error": str(e)}

    def schema(self):
        return {

            "type": "function",

            "function": {

                "name": "weather",

                "description":
                    "查询城市天气",

                "parameters": {

                    "type": "object",

                    "properties": {

                        "city": {

                            "type": "string",

                            "description":
                                "城市完整名称，例如：武汉市、北京市，建议带上「市」字，不要简写"

                        }

                    },

                    "required": [
                        "city"
                    ]

                }

            }

        }
