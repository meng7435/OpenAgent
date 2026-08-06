class WorkflowGraph:



    def __init__(self):

        self.nodes={}


        self.edges={}



    def add_node(
        self,
        node
    ):

        self.nodes[node.name]=node



    def add_edge(
        self,
        start,
        end
    ):

        self.edges[start]=end



    async def run(
        self,
        state
    ):


        current="research"


        while current:


            node=self.nodes[current]


            print(
                "执行节点:",
                current
            )


            state=await node.run(
                state
            )


            current=self.edges.get(
                current
            )


        return state