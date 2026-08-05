from pydantic import BaseModel



class AgentAction(BaseModel):


    action:str


    input:dict