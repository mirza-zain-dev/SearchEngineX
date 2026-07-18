# SearchEngineX

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-000000?logo=flask)](https://flask.palletsprojects.com/)
[![IR](https://img.shields.io/badge/IR-Inverted%20Index-informational)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Lightweight **information-retrieval** engine: build an inverted index, rank documents for a query, and expose search over a **Flask REST API** with a simple frontend.

---

## Why it exists

Modern search stacks hide the fundamentals. SearchEngineX makes the core path explicit:

**tokenize → index → query → rank → JSON results**

Ideal portfolio piece for AI / backend roles that care about retrieval, not only prompt engineering.

## Features

- In-memory **inverted index**
- Document add + search APIs
- Ranking over term overlap (extensible to TF-IDF / BM25)
- Flask backend + separate frontend
- spaCy-friendly dependency set for tokenization experiments

## Architecture

```text
Frontend ──▶ GET /search?q=... ──▶ InvertedIndex.search()
                │
Frontend ──▶ POST /add ──────────▶ InvertedIndex.add_document()
```

## Tech stack

| Area | Tools |
|------|--------|
| Core | Python, custom `InvertedIndex` |
| API | Flask, flask-cors |
| NLP deps | spaCy, NLTK (tokenization / preprocessing experiments) |
| Frontend | JS client under `frontend/` |

## Project structure

```text
SearchEngineX/
├── backend/
│   ├── app.py
│   └── search_engine.py      # inverted index + ranking
├── frontend/
├── requirements.txt
├── .github/workflows/ci.yml
├── .gitignore
├── LICENSE
└── README.md
```

> Note: never commit `venv/` — use `.gitignore` (included).

## Quick start

```bash
git clone https://github.com/mirza-zain-dev/SearchEngineX.git
cd SearchEngineX

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd backend
python app.py
```

### API

| Method | Path | Body / query | Description |
|--------|------|--------------|-------------|
| `GET` | `/search` | `?q=lazy dog` | Ranked hits |
| `POST` | `/add` | `{ "id": "doc4", "content": "..." }` | Index a document |

### Example

```bash
curl "http://127.0.0.1:5000/search?q=fox"
curl -X POST http://127.0.0.1:5000/add \
  -H 'Content-Type: application/json' \
  -d '{"id":"doc4","content":"Search engines use inverted indexes."}'
```

## Roadmap

- [ ] BM25 ranking
- [ ] Persistent index (SQLite / disk)
- [ ] Phrase queries & boolean operators
- [ ] Benchmarks on a small public corpus

## AI engineer notes

Retrieval quality compounds every LLM/RAG system. This repo shows you understand **index structure and ranking**, not only calling an embedding API.

## License

MIT — see [LICENSE](LICENSE).

## Author

**Mirza Zain** · [GitHub](https://github.com/mirza-zain-dev)
