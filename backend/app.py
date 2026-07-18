from flask import Flask, jsonify, request
from flask_cors import CORS
from search_engine import InvertedIndex

app = Flask(__name__)
CORS(app)
engine = InvertedIndex()

for doc_id, text in {
    "doc1": "The quick brown fox jumps over the lazy dog.",
    "doc2": "Fast foxes leap over lazy dogs in summer.",
    "doc3": "The dog is not lazy; it is simply energy-efficient.",
}.items():
    engine.add_document(doc_id, text)


@app.get("/search")
def search():
    q = request.args.get("q")
    if not q:
        return jsonify({"error": "Missing query"}), 400
    return jsonify(engine.search(q))


@app.post("/add")
def add_document():
    data = request.get_json(silent=True) or {}
    doc_id, content = data.get("id"), data.get("content")
    if not doc_id or not content:
        return jsonify({"error": "Missing id or content"}), 400
    engine.add_document(doc_id, content)
    return jsonify({"message": "Document added", "id": doc_id})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
