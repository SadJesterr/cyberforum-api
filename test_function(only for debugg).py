import route
import schemas
import models

##### РАБОТАЕТ

# models.create_db()

# theme = {"name": "Anton", "text": "Help"}
# print(f'Создали тему:\n{route.create_theme(theme=theme)}\n') 

# comment = {'author_name':'Anton', 'text':'Privet', 
#            'quote_id':-1, 'theme_id':1}
# print(f'Создали комментарий:\n{route.create_comment(comment)}\n')

# print(f'Получили список всех тем:\n{route.get_themes()}\n')

# print(f'Получили тему по id:\n{route.get_theme(theme_id=1)}\n')

# print(f'Получили список комментариев для темы:\n{route.get_comments(theme_id=1)}\n')

# print(f'Получение комментария по id:\n{route.get_comment(theme_id=1, comment_id=1)}\n')

# comment = {'author_name': 'Anton', 'text': 'Poka', 'quote_id':-1}
# print(f'Изменение комменатрия по id:\n{route.update_comment(theme_id=1, comment_id=1, comment=comment)}\n')

# print(f'Удаление темы по id:\n{route.delete_theme(theme_id=1)}\n')