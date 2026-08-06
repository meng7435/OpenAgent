from pydantic import BaseModel



class WorkflowState(BaseModel):


    query:str


    research:str=""


    analysis:str=""


    report:str=""


    current_node:str=""
