from fastapi import FastAPI
import re

app = FastAPI()

knowledge_base = {
    "select": "SELECT используется для выборки данных из таблицы.",
    "where": "WHERE используется для фильтрации строк по условию.",
    "join": "JOIN используется для объединения данных из нескольких таблиц.",
    "group by": "GROUP BY используется для группировки строк по указанным полям.",
    "order by": "ORDER BY используется для сортировки результата запроса."
}

aliases = {
    "select": "select",
    "what is select": "select",
    "что такое select": "select",

    "where": "where",
    "для чего нужен where": "where",
    "что такое where": "where",

    "join": "join",
    "что делает join": "join",
    "что такое join": "join",

    "group by": "group by",
    "объясни group by": "group by",
    "что такое group by": "group by",

    "order by": "order by",
    "что такое order by": "order by",
    "объясни order by": "order by",
}

def normalize_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[?.,!]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text

@app.get("/")
def root():
    return {"message": "SQL Knowledge API is running"}

@app.get("/get_topic")
def get_topic(name: str):
    key = normalize_text(name)

    if key in knowledge_base:
        return {"topic": key, "answer": knowledge_base[key]}

    if key in aliases:
        normalized_key = aliases[key]
        return {"topic": normalized_key, "answer": knowledge_base[normalized_key]}

    return {
        "topic": name,
        "answer": "В подключённой базе знаний нет данных по этому вопросу."
    }
