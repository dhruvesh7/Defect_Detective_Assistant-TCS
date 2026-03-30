# Defect Detective Assistant - AI ROOT CAUSE INVESTIGATOR

**Defect Detective Assistant** is a high-end RAG (Retrieval-Augmented Generation) assistant designed for **Discrete Manufacturing**. It investigates the root causes of production defects (like silver streaks, chatter marks, or porosity) and correlates them with process parameter deviations.

## Features
- **Defect Detective Assistant**: A fully responsive, high-fidelity UI that works on both Desktop and Mobile.
- **RAG-Powered Diagnostics**: Utilizes LangChain, ChromaDB, and OpenAI to retrieve accurate engineering data.
- **Cross-Vertical Knowledge Base**:
    - **Injection Molding**: Surface burns, short shots, sink marks.
    - **CNC Machining**: Chatter marks, built-up edge (BUE).
    - **Welding (MIG/TIG)**: Porosity, undercut, spatter.
    - **Stamping**: Wrinkling, springback, cracking.
    - **PCB Manufacturing**: Solder bridging, delamination, over-etching, drill offset.
- **Quick-Access Chips**: One-click tags for common investigations.
- **Branding**: "Build with Sarighasri" signature.

## Project Structure
- `app.py`: FastAPI backend and RAG logic.
- `ingest.py`: Script to process and index the manufacturing knowledge base (`data/`).
- `index.html`: Premium "Defect Detective Assistant" dashboard (HTML/CSS/JS).
- `data/`: Directory containing Markdown-based manufacturing SOPs and defect catalogs.
- `vector_db/`: Persistent ChromaDB store.

## Installation & Setup

### 1. Prerequisites
- Python 3.9+
- OpenAI API Key (Stored in `.env`)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Ingest Data
Run the ingestion script to build the vector database:
```bash
python ingest.py
```

### 4. Launch the Server
```bash
python app.py
```
The application will be live at `http://localhost:8000`.

---
**Build with Sarighasri**
