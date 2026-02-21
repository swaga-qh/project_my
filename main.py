from fastapi import FastAPI

# Создаем экземпляр приложения
app = FastAPI()

# Определяем обработчик для GET-запроса по главному URL ("/")
@app.get("/")
def read_root():
    # FastAPI автоматически преобразует словарь в JSON
    return {"message": "Hello, FastAPI!"}

# Еще один пример с параметром в пути
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
    https://github.com/swaga-qh/project-.git
