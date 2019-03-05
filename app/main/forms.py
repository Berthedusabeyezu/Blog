from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):

    title = StringField('Post title',validators=[Required()])
    post = TextAreaField('post', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment ', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required()])
    name =  TextAreaField('Add your username', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
    blog = TextAreaField('Post It !!', validators=[Required()])
    submit = SubmitField('Update')
