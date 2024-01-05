from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField , TextAreaField, PasswordField, BooleanField, IntegerField
from wtforms.validators import  ValidationError, DataRequired, Length, Email, EqualTo, NumberRange
from flask_login import current_user

from app.Model.models import Review, Member

def get_reviews():
    return Review.query.all()


class MovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    genre = SelectField('Genre', choices = [('None'),
                                            ('Action'),
                                            ('Animation'),
                                            ('Comedy'),
                                            ('Crime'),
                                            ('Drama'),
                                            ('Experimental'),
                                            ('Fantasy'),
                                            ('Historical'),
                                            ('Romance'),
                                            ('Science Fiction'),
                                            ('Thriller'),
                                            ('Western')])
    submit = SubmitField('Post Movie')
    
    
class SortForm(FlaskForm):
    sort_by = SelectField('Sort by', choices=[(1,'Date'), (2,'Title'), (3,'Rating')], validators=[DataRequired()]) 

    sort_genre =SelectField('Genre', choices = [('None'),
                                            ('Action'),
                                            ('Animation'),
                                            ('Comedy'),
                                            ('Crime'),
                                            ('Drama'),
                                            ('Experimental'),
                                            ('Fantasy'),
                                            ('Historical'),
                                            ('Romance'),
                                            ('Science Fiction'),
                                            ('Thriller'),
                                            ('Western')], validators=[DataRequired()])
    submit = SubmitField('Refresh')
    
    
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating (1-100)', validators=[DataRequired(), NumberRange(1,100) ])
    review = TextAreaField('Review', validators=[Length(min=1,max=1500,message="Length out of bounds")])
    submit = SubmitField('Post Review')


class GetFriendForm(FlaskForm):
    friend_username = StringField('Friend Username', validators=[DataRequired()])
    submit = SubmitField('Add Friend')
 
    
class AddRatingOrReviewForm(FlaskForm):
    title = ""
    rating = IntegerField('Rating (1-100)', validators=[NumberRange(1,100) ])
    review = TextAreaField('Review', validators=[Length(min=1,max=1500,message="Length out of bounds")])
    submit = SubmitField('Post')
    
class EditForm(FlaskForm):
    rating = IntegerField('Rating (1-100)', validators=[DataRequired(), NumberRange(1,100) ])
    review = TextAreaField('Review', validators=[Length(min=1,max=1500,message="Length out of bounds")])
    submit = SubmitField('Post Review')
