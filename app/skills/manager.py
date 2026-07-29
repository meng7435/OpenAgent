class SkillManager:


    def __init__(self):
        self.skills = {}


    def register(self, skill):

        self.skills[skill.name] = skill


    def get(self, name):

        return self.skills.get(name)


    def get_schemas(self):

        result=[]

        for skill in self.skills.values():

            result.append(
                {
                    "type":"function",
                    "function":{
                        "name":skill.name,
                        "description":skill.description,
                        "parameters":skill.parameters()
                    }
                }
            )

        return result