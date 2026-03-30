# Defect-to-Process-Parameter Root-Cause Investigator

A RAG-powered diagnostic tool for discrete manufacturing to help quality engineers identify the root causes of defects based on process parameters.

## User Review Required

> [!IMPORTANT]
> - **OpenAI API Key**: The application requires an `OPENAI_API_KEY`. I will use the one found in the local `.env` if available, or ask you to provide one.
> - **Sample Data**: Since I don't have your actual manufacturing logs, I will create a synthetic "Knowledge Base" (Markdown files) covering common discrete manufacturing defects (e.g., CNC milling, Injection Molding).

## Proposed Changes

### Backend (Python)
Build a FastAPI server with a LangChain RAG pipeline.

#### [NEW] [ingest.py](file:///e:/TCS/ingest.py)
Script to process and embed manufacturing knowledge base files into a ChromaDB vector store.

#### [NEW] [app.py](file:///e:/TCS/app.py)
The core FastAPI application serving:
- `/chat`: POST endpoint for the RAG chatbot.
- `/`: GET endpoint to serve the premium dashboard UI.

#### [NEW] [requirements.txt](file:///e:/TCS/requirements.txt)
Python dependencies: `fastapi`, `uvicorn`, `langchain`, `langchain-chroma`, `langchain-openai`, `python-dotenv`.

### Data (Knowledge Base)
#### [NEW] [defects_catalog.md](file:///e:/TCS/data/defects_catalog.md) 
#### [NEW] [process_parameters.md](file:///e:/TCS/data/process_parameters.md)
Markdown files containing structured information about defects and their correlations with parameters like speed, pressure, and temperature.

### Frontend (HTML/CSS/JS)
#### [NEW] [index.html](file:///e:/TCS/index.html)
A premium Single-Page Application (SPA) designed with a "Manufacturing Command Center" aesthetic.
- **Visuals**: Dark mode, data-visualization-inspired borders, glassmorphic chat interface.
- **Interactions**: Real-time message streaming, diagnostic status indicators, and hover effects.

## Open Questions

- Does the synthetic data focus (CNC Milling vs. Injection Molding) align with your manufacturing context, or would you like to provide specific documentation?
- Are there specific vector databases or LLMs you prefer (currently proposing ChromaDB and GPT-4o-mini)?

## Verification Plan

### Automated Tests
- Run `ingest.py` and verify `vector_db` folder creation.
- Execute `pytest` (if added) or manual API testing via `curl` vs `/chat`.

### Manual Verification
- Launch the application using `uvicorn app:app`.
- Test specific queries like: "What process parameters cause surface burns in injection molding?" or "How do I fix chatter marks on a CNC lathe?"
- Inspect the UI for responsiveness and premium design.
