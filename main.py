from fastapi import FastAPI

app = FastAPI()

knowledge_base = {
    "select": "SELECT используется для выборки данных из таблицы.",
    "where": "WHERE используется для фильтрации строк по условию.",
    "join": "JOIN используется для объединения данных из нескольких таблиц.",
    "group by": "GROUP BY используется для группировки строк по указанным полям.",
    "order by": "ORDER BY используется для сортировки результата запроса."
}

@app.get("/")
def root():
    return {"message": "SQL Knowledge API is running"}

@app.get("/get_topic")
def get_topic(name: str):
    key = name.lower().strip()
    if key in knowledge_base:
        return {"topic": name, "answer": knowledge_base[key]}
    return {"topic": name, "answer": "В подключённой базе знаний нет данных по этому вопросу."}
