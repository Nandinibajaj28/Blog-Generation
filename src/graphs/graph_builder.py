from langchain.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState

class GraphBuilder:
    def __init__(self, llm):
        self.graph = StateGraph(BlogState)
        self.llm = llm
    
    def build_topic_graph(self):
        ## nodes
        self.graph.add_node("title_creation", self.generate_blog)
        self.graph.add_node("content_creation", self.generate_blog)
        self.graph.add_node("tags_creation", self.generate_blog)

        ## edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", "tags_creation")
        self.graph.add_edge("tags_creation", END)

        return self.graph.compile()
        
    def setup_graph(self,usecase):
        if usecase=="topic":
            self.build_topic_graph()