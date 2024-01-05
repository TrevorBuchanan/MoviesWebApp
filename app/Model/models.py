from datetime import datetime
from app import db, login


from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# git status
# git add .  // . to add everything
# git cmmit -am "message"
# git push origin [name of branch]

@login.user_loader
def load_user(id):
    return Member.query.get(int(id))


movieReviews = db.Table('movieReviews', db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                                db.Column( 'review_id', db.Integer, db.ForeignKey('review.id')))

movieRecommends = db.Table('movieRecommends', db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
                           db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))

watchLaters = db.Table('watchLaters', db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
                           db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))

watched = db.Table('watched', db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
                           db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')))

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    genre = db.Column(db.String(150))
    average_rating = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    reviews = db.relationship('models.Review', secondary=movieReviews, primaryjoin=(movieReviews.c.movie_id == id), 
                           backref=db.backref('movieReviews', lazy='dynamic'), lazy='dynamic')
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    def get_reviews():
        return self.reviews
    

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(250))
    review = db.Column(db.String(1500))
    rating = db.Column(db.Integer, default = 0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    #
    whovoted = db.Column(db.String(1600))
    likecount = db.Column(db.Integer, default = 0) # number of lieks defaulting to 0
    #

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('member.id'))
    

class Member(UserMixin, db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64), unique= True, index= True)
    email = db.Column(db.String(120), unique= True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='writer', lazy ='dynamic')
    user_type = db.Column(db.String(50))
    friends = db.relationship('Friendship', backref='writer', lazy ='dynamic')
    friends = db.relationship('Member', secondary='friendship',
                            primaryjoin=(Friendship.member_id == id),
                            secondaryjoin=(Friendship.friend_id == id),
                            backref=db.backref('friendships', lazy='dynamic'),
                            lazy='dynamic')
    recommended_movies = db.relationship('models.Movie', secondary=movieRecommends, primaryjoin=(movieRecommends.c.member_id == id), 
                backref=db.backref('movieRecommends', lazy='dynamic'), lazy='dynamic')
    watch_later_movies = db.relationship('models.Movie', secondary=watchLaters, primaryjoin=(watchLaters.c.member_id == id), 
            backref=db.backref('watchLaters', lazy='dynamic'), lazy='dynamic')
    watched_movies = db.relationship('models.Movie', secondary=watched, primaryjoin=(watched.c.member_id == id), 
        backref=db.backref('watched', lazy='dynamic'), lazy='dynamic')
        
    __mapper_args__ = {
        'polymorphic_identity': 'Member',
        'polymorphic_on':user_type
    }
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_user_posts(self):
        return self.reviews
        
    def __repr__(self):
        return '<Member {},{},{},{} >'.format(self.id, self.username, self.email, self.password_hash)
    
class Normal(Member):
    __tablename__ = 'Normal'
    id = db.Column(db.ForeignKey("member.id"), primary_key= True)

    __mapper_args__ = {
        'polymorphic_identity':'Normal'
    }
        
class Premium(Member):
    __tablename__ = 'Premium'
    id = db.Column(db.ForeignKey("member.id"), primary_key= True)

    # can recomend movies
    # can see recomended movies from friends
    
    __mapper_args__ = {
        'polymorphic_identity':'Premium'
    }
        
