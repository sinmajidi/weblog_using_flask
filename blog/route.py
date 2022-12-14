from blog import app,db,bcrypt
from blog.forms import registrationForms,loginform,profileform,postform
from flask import render_template,redirect,url_for,flash,abort
from blog.models import User,Post
from flask_login import login_user,current_user,logout_user

@app.route('/')
def home():
	posts=Post.query.all()
	return render_template('home.html',posts=posts)
@app.route('/about')
def about():
	return render_template('home.html')
@app.route('/register',methods=['GET','POST'])
def register():

	r_form = registrationForms()
	if r_form.validate_on_submit():
		hashed_pass=bcrypt.generate_password_hash(r_form.password.data).decode('utf-8')
		u=User(username=r_form.username.data,email=r_form.email.data,password=hashed_pass)
		db.session.add(u)
		db.session.commit()
		flash("you're registered succesfuly!","success")
		return redirect(url_for('home'))
	return render_template('register.html',form=r_form)
@app.route('/login',methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		  return redirect(url_for('home'))

	l_form = loginform()
	if l_form.validate_on_submit():
		user=User.query.filter_by(email=l_form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,l_form.password.data):
			login_user(user,remember=l_form.remember.data)
			flash("you are login succesfully","success")
			return redirect(url_for('home'))
		else:
			flash("email or password invalid","danger")
	return render_template('login.html',form=l_form)
@app.route('/logout')
def logout():
	if current_user.is_authenticated:
		logout_user()
		flash("you are loged out","danger")
		return redirect(url_for('home'))
	else:
		return redirect(url_for('login'))
@app.route('/profile',methods=['GET','POST'])
def profile():
	if current_user.is_authenticated:
		p_form=profileform()
		if p_form.validate_on_submit():

			print(p_form.new_username.data)
			print(p_form.new_email.data)

			# u = User.query.filter_by(email=current_user.email).first()
			# u.username=p_form.new_username.data
			# u.email=p_form.new_email.data
			#----------or------------------
			current_user.username=p_form.new_username.data
			current_user.email=p_form.new_email.data

			db.session.commit()
			flash("your profile changed succesfully", "success")
			return redirect(url_for('profile'))
		else:
			p_form.new_username.data = current_user.username
			p_form.new_email.data = current_user.email
			return render_template('profile.html',form=p_form)
	else:
		flash("you should login first", "danger")
		return redirect(url_for('login'))

@app.route('/new_post',methods=['GET','POST'])
def new_post():
	if current_user.is_authenticated:
		form=postform()
		if form.validate_on_submit():
				p =Post(title=form.title.data,content=form.content.data,author=current_user)
				db.session.add(p)
				db.session.commit()
				flash("your post create succesfully", "info")
				return redirect(url_for('home'))
		else:

				return render_template('post.html',form=form)
	else:
		flash("you should login first", "danger")
		return redirect(url_for('login'))
@app.route('/show/<int:post_id>')
def show_articles(post_id):
	post=Post.query.get(post_id)
	return render_template('show.html', post=post)
@app.route('/delete/<int:post_id>')
def delete_articles(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author!=current_user:
		abort(403)
	else:
		db.session.delete(post)
		db.session.commit()
		flash("post deleted","info")
	return redirect(url_for('home'))
@app.route('/update/<int:post_id>',methods=['GET','POST'])
def update_articles(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	else:
		if current_user.is_authenticated:
			form = postform()
			if form.validate_on_submit():
				post.title=form.title.data
				post.content=form.content.data
				db.session.commit()
				flash("your post update succesfully", "info")
				return redirect(url_for('show_articles',post_id=post.id))
			else:
				form.title.data=post.title
				form.content.data=post.content
				return render_template('update_articles.html', form=form)
		else:
			flash("you should login first", "danger")
			return redirect(url_for('login'))




