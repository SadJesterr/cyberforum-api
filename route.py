import uvicorn
import schemas
import crud

from fastapi import FastAPI, HTTPException

app = FastAPI()

Theme = schemas.Theme
Comment = schemas.Comment
crud = crud.CRUD()

# import models
# models.create_db()

# Создание темы
@app.post('/theme/')
def create_theme(theme: Theme):
    return crud.create_theme(theme=dict(theme))

# Создание комментария
@app.post('/comment/{theme_id}')
def create_comment(comment: Comment):
    if comment.theme_id <= 0:
        raise HTTPException(status_code=404, detail="Theme not found")
    return crud.create_comment(comment=dict(comment))

# Получение списка тем
@app.get('/theme/')
def get_themes():
    return crud.get_themes()

# Получение темы
@app.get('/theme/{theme_id}')
def get_theme(theme_id: int):
    if theme_id > len(crud.get_themes()) or theme_id <= 0:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    return crud.get_theme(theme_id=theme_id)

# Получение списка комментариев для темы
@app.get('/comment/{theme_id}')
def get_comments(theme_id: int):
    if theme_id > len(crud.get_themes()) or theme_id <= 0:
        raise HTTPException(status_code=404, detail="Theme not found")

    return crud.get_comments(theme_id=theme_id)

# Получение комментария
@app.get('/comment/{theme_id}/{comment_id}')
def get_comment(theme_id: int, comment_id: int):
    if theme_id > len(crud.get_themes()) or theme_id <= 0:
        raise HTTPException(status_code=404, detail="Theme not found")
    
    if comment_id <= 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    return crud.get_comment(theme_id=theme_id,
                            comment_id=comment_id)

# Изменение комментария
@app.put('/comment/{theme_id}/{comment_id}')
def update_comment(theme_id:int, comment_id: int, comment: dict):
    if comment_id <= 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    return crud.update_comment(theme_id=theme_id,
                               comment_id=comment_id,
                               comment=comment)

# Удаление темы
@app.delete('/theme/{theme_id}')
def delete_theme(theme_id: int):
    if theme_id > len(crud.get_themes()) or theme_id <= 0:
        raise HTTPException(status_code=404, detail="Theme not found")

    return crud.delete_theme(theme_id=theme_id)

if __name__ == 'main':
    uvicorn.run(app, host="127.0.0.1", port=8000)