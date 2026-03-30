import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables (API Key)
load_dotenv(override=True)

DB_PATH = "vector_db"

# RAG System Prompt
RAG_SYSTEM_PROMPT = """You are an expert Manufacturing Quality Engineer specialized in Root-Cause Analysis (RCA). 
Your goal is to investigate defects in discrete manufacturing processes (CNC milling, Injection Molding, Casting, etc.) 
and provide precise root causes based on process parameter deviations.

CONTEXT:
{context}

INSTRUCTIONS:
1.  Answer using ONLY the information provided in the context above.
2.  If the context does not contain enough information, state that you don't know—do not invent details.
3.  Format your response clearly, highlighting the 'Defect', 'Probable Root Causes', and 'Parameters to Adjust'.
4.  Maintain a professional, diagnostic tone.

QUESTION: {question}
"""

PROMPT = ChatPromptTemplate.from_template(RAG_SYSTEM_PROMPT)

app = FastAPI(title="Manufacturing Root-Cause Investigator API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Engine on Startup
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20, "lambda_mult": 0.5},
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": PROMPT},
)

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    result: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        result = qa_chain.invoke({"query": req.query})
        return ChatResponse(result=result["result"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
async def health():
    return {"status": "up", "db_initialized": os.path.exists(DB_PATH)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
