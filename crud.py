import models

class CRUD:
    dataBase = models.sessionLocal()

    def create_theme(self, theme: dict):
        with self.dataBase as db:
            insert = models.Theme(name=theme['name'],text=theme['text'])

            db.add(insert)
            db.commit()
            db.refresh(insert)

            answer = dict(id=insert.id,
                        name=insert.name,
                        text=insert.text)
            return answer

    def create_comment(self, comment: dict):
        with self.dataBase as db:
            insert = models.Comment(author_name=comment['author_name'],text=comment['text'],
                                    theme_id=comment['theme_id'],quote_id=comment['quote_id'])
            db.add(insert)
            db.commit()
            db.refresh(insert)

            answer = dict(id=insert.id, 
                        theme_id=insert.theme_id, 
                        author_name=insert.author_name,
                        text=insert.text,
                        quote_id=insert.quote_id)

            return answer

    def get_themes(self):
        with self.dataBase as db:
            query = db.query(models.Theme).all()
            answer = []
            for q in query:
                answer.append(dict(id=q.id, 
                                name=q.name, 
                                text=q.text))
            return answer

    def get_theme(self, theme_id: int):
        with self.dataBase as db:
            query = db.query(models.Theme).filter(models.Theme.id == theme_id)
            for q in query:
                answer=dict(id=q.id, 
                            name=q.name, 
                            text=q.text)
            return answer

    def get_comments(self, theme_id: int):
        with self.dataBase as db:
            query = db.query(models.Comment).filter(models.Comment.theme_id == theme_id).all()
            answer = []
            for q in query:
                answer.append(dict(id=q.id, 
                                theme_id=q.theme_id, 
                                author_name=q.author_name,
                                text=q.text,
                                quote_id=q.quote_id))
            return answer

    def get_comment(self, theme_id: int, comment_id: int):
        with self.dataBase as db:
            query = db.query(models.Comment).filter(
                models.Comment.theme_id == theme_id).filter(models.Comment.id == comment_id)
            for q in query:
                answer=(dict(id=q.id, 
                            theme_id=q.theme_id, 
                            author_name=q.author_name,
                            text=q.text,
                            quote_id=q.quote_id))
            return answer

    def update_comment(self, theme_id:int, comment_id: int, comment: dict):
        with self.dataBase as db:
            query = db.query(models.Comment).filter(
                models.Comment.theme_id == theme_id).filter(models.Comment.id == comment_id)
        
            # update = {'id':'', 'author_name':'', 'quote_id':'', 'theme_id':'', 'text':'', }
            for q in query:
                q.author_name = comment.get('author_name', q.author_name)
                q.text = comment.get('text', q.text)
                q.quote_id = comment.get('quote_id', q.quote_id)
                q.theme_id = comment.get('theme_id', q.theme_id)

                update = dict(id=q.id,
                            author_name=q.author_name,
                            quote_id=q.quote_id,
                            theme_id=q.theme_id,
                            text=q.text)

            db.commit()
            db.refresh(q)
            return update

    def delete_theme(self, theme_id: int):
        with self.dataBase as db:
            query = db.query(models.Theme).filter(models.Theme.id == theme_id)
            for q in query:
                answer = dict(id=q.id,
                        name=q.name,
                        text=q.text)

            db.delete(q)
            db.commit()
            return answer