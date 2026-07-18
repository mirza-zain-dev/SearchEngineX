"""Minimal inverted index for SearchEngineX."""
from __future__ import annotations

import re
from collections import defaultdict


class InvertedIndex:
    def __init__(self) -> None:
        self.index: dict[str, set[str]] = defaultdict(set)
        self.docs: dict[str, str] = {}

    def _tokenize(self, text: str) -> list[str]:
        return re.findall(r"[a-z0-9]+", text.lower())

    def add_document(self, doc_id: str, content: str) -> None:
        self.docs[doc_id] = content
        for token in set(self._tokenize(content)):
            self.index[token].add(doc_id)

    def search(self, query: str) -> list[dict]:
        tokens = self._tokenize(query)
        if not tokens:
            return []
        scores: dict[str, int] = defaultdict(int)
        for t in tokens:
            for doc_id in self.index.get(t, set()):
                scores[doc_id] += 1
        ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [
            {"id": doc_id, "score": score, "snippet": self.docs[doc_id][:160]}
            for doc_id, score in ranked
        ]
