import json

# 输出结果转换
def parse_action(text:str):
    try:
        data = json.loads(text)

        return data
    except Exception as e:
        return {

            "action": "finish",

            "input": text,

            'error': e

        }