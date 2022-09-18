from blog.models import User,Post
from blog import db
db.create_all()


#------------write data base---------------------
# u = User(username='sina majidi', email='sin.majidi@gmail.com',password='sm1818')
# p=Post(title='me',content='its about me',author=u)
# db.session.add(p)
# db.session.commit()

#---------------read data base--------------------
print(User.query.all())
# print(User.query.first().posts)
# print(Post.query.all())
# print(Post.query.first().user_id)
# print(Post.query.first().author)
# print(Post.query.filter_by(user_id='admin').first())
# print(article.query.get(#primary key#))
#------------------delete data-----------------------
# db.session.delete(me)
# db.session.commit()