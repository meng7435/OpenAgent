def react_prompt(task, history,skills):
    REACT_PROMPT = f"""
    
    你是一个AI Agent。


你的目标:

{task}


你可以使用以下技能:

{skills}


执行历史:

{history}


规则:

1. 如果任务无法直接回答，
必须调用技能。


2. 返回JSON格式。


调用技能:

{{
"action":"skill_name",

"input":{{}}
}}



完成任务:

{{
"action":"finish",

"input":"最终答案"
}}


不要提前finish。


"""

    return REACT_PROMPT
