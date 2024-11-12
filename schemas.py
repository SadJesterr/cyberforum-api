from pydantic import BaseModel

class ThemeBase(BaseModel):
    name: str
    text: str

class Theme(ThemeBase):
    # id: int

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    author_name: str
    text: str
    quote_id: int

class Comment(CommentBase):
    # id: int
    theme_id: int
    
    class Config:
        from_attributes = True
