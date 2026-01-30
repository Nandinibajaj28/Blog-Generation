import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")


## API's
@app.post("/blogs")
async def create_blogs(request: Request):
    data = await request.json()
    topic = data.get("topic","")
    if not topic:
        return {"error":"Topic is required"}
    
    ## get llm object
    groqllm=GroqLLM()
    llm = groqllm.get_llm()

    ##Get graph
    graph_builder=GraphBuilder(llm)
    if topic:
        graph=graph_builder.setup_graph(usecase="topic")
        response=graph.invoke({"topic":topic})
       
    return {"data":response}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)