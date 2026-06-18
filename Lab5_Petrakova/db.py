import json
from typing import Any, List, Dict


class DocumentDB:
    def __init__(self):
        self.data = []

    def add(self, doc: dict):
        if "id" not in doc:
            raise ValueError("Документ повинен містити id")

        if self.find_by_id(doc["id"]):
            raise ValueError("ID вже існує")

        self.data.append(doc)

    def delete_by_id(self, doc_id):
        self.data = [d for d in self.data if d["id"] != doc_id]

    def delete_by_condition(self, field, value):
        self.data = [d for d in self.data if not self._get(d, field) == value]

    def update(self, doc_id, field, value):
        doc = self.find_by_id(doc_id)
        if not doc:
            raise ValueError("Документ не знайдено")

        self._set(doc, field, value)

    def find(self, field, op, value):

        result = []

        for doc in self.data:

            val = self._get(doc, field)

            if val is None:
                continue

            if self._compare(val, op, value):
                result.append(doc)

        return result

    def aggregate(self, operation, field):

        values = []

        for doc in self.data:
            val = self._get(doc, field)

            if isinstance(val, (int, float)):
                values.append(val)

        if not values:
            raise ValueError("Нема числових даних")

        if operation == "count":
            return len(values)

        if operation == "sum":
            return sum(values)

        if operation == "avg":
            return sum(values) / len(values)

        if operation == "min":
            return min(values)

        if operation == "max":
            return max(values)

        raise ValueError("Невідома операція")

    def groupby(self, field):

        groups = {}

        for doc in self.data:

            key = self._get(doc, field)

            groups.setdefault(key, []).append(doc)

        return groups

    def save(self, filename):

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def load(self, filename):

        with open(filename, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def find_by_id(self, doc_id):
        for d in self.data:
            if d["id"] == doc_id:
                return d
        return None

    def _get(self, doc, field):

        parts = field.split(".")

        for p in parts:
            if isinstance(doc, dict):
                doc = doc.get(p)
            else:
                return None

        return doc

    def _set(self, doc, field, value):

        parts = field.split(".")
        for p in parts[:-1]:
            doc = doc.setdefault(p, {})

        doc[parts[-1]] = value

    def _compare(self, a, op, b):

        if op == "=":
            return a == b
        if op == ">":
            return a > b
        if op == "<":
            return a < b
        if op == ">=":
            return a >= b
        if op == "<=":
            return a <= b
        if op == "in":
            return b in a if isinstance(a, list) else False

        return False