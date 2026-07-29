from app.skills.manager import SkillManager

from app.skills.travel import TravelSkill

from app.mcp.client import MCPClient
from app.mcp import server
skill_manager = SkillManager()

# 旅游Skill注册
skill_manager.register(TravelSkill(MCPClient(server)))
