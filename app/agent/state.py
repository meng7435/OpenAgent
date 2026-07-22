from dataclasses import dataclass,field
from typing import Annotated
@dataclass
class AgentState:
    # 保存整个对话过程
    messages: list = field(
        default_factory=list
    )

    # 当前执行步骤
    current_step: str = ""

    # 是否结束
    finished: bool = False

    # 执行动作次数
    iteration: int = 0
