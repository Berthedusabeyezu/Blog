from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Post,User,Comment
from .forms import PostForm,CommentForm
from flask_login import login_required, current_user
from .forms import PostForm,UpdateProfile
from .. import db,photos
from ..email import mail_message
from ..request import get_quote



    

@main.route('/')
def index():
       
    posts=Post.query.all()
   
    title = 'Home - Welcome to The best Blog Post Web'
    # posts = posts.get_posts()
    quote = get_quote()

    return render_template('index.html', title = title, quote = quote, posts = posts)
    
    
@main.route('/post/<int:id>')
def post(id):
    post = Post.query.filter_by(id=id).first()
    comments=Comment.get_comments(id=id)

    
    '''
    View post page function that returns the post details page and its data
    '''
    return render_template('post.html',post = post,comments=comments)

@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        new_post = Post(title = title,description = post, user_id = current_user.id)

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index',post = post ))

    return render_template('new_post.html',post_form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None: 
        abort(404)
  
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update/',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    post=Post.query.filter_by(id=id).first()
    

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment = comment,post=post, user_id = current_user.id)

        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.index'))
    

    return render_template('new_comment.html',comment_form=form)


    