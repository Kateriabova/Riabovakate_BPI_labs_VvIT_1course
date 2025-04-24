from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import wikipedia
import random

app = FastAPI()
wikipedia.set_lang("ru")


class ArticleRequest(BaseModel):
    title: str
    keyword: str


class ArticleResponse(BaseModel):
    title: str
    summary: str
    keyword: str
    url: str


class SearchRequest(BaseModel):
    query: str
    limit: int = 5


class SearchResponse(BaseModel):
    results: list[str]


@app.get("/article/{title}", response_model=ArticleResponse)
def get_article(title: str):
    try:
        article = wikipedia.summary(title, sentences=10)
        page = wikipedia.page(title)
        return {"title": page.title, "summary": article, "keyword": title, "url": page.url}
    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Статья не найдена")
    except wikipedia.exceptions.DisambiguationError:
        page = wikipedia.page(wikipedia.exceptions.DisambiguationError.options[0])
        return {
            "title": page.title,
            "summary": wikipedia.summary(wikipedia.exceptions.DisambiguationError.options[0], sentences=10),
            "keyword": title,
            "url": page.url
        }


@app.get("/search/", response_model=SearchResponse)
def search_articles(query: str, limit: int = 5):
    results = wikipedia.search(query, results=limit)
    return {"results": results}


@app.post("/key-word/", response_model=ArticleResponse)
def get_article_by_keyword(request: ArticleRequest):
    try:
        search_results = wikipedia.search(request.keyword)
        if not search_results:
            return {
                "title": "Ошибка",
                "summary": f"Нет статей по ключевому слову '{request.keyword}'",
            }
        article = random.choice(search_results)
        page = wikipedia.page(article)
        summary = wikipedia.summary(article)

        return {
            "title": page.title,
            "summary": summary,
            "keyword": request.keyword,
            'url': page.url
        }

    except wikipedia.exceptions.DisambiguationError:
        article = wikipedia.exceptions.DisambiguationError.options[0]
        summary = wikipedia.summary(article)
        return {
            "title": article,
            "summary": summary,
            "keyword": request.keyword + " in first meaning"
        }

    except wikipedia.exceptions.PageError:
        raise HTTPException(status_code=404, detail="Статья не найдена")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


