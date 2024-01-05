from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
from config import Config

from app import db
from app.Model.models import Review, Member, Movie
from app.Controller.forms import MovieForm, ReviewForm, SortForm, GetFriendForm, AddRatingOrReviewForm, EditForm
from flask_login import login_user, current_user, logout_user, login_required

from sqlalchemy import or_
 
bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/premium_index', methods=['POST', 'GET'])
def premium_index():
    if request.method == 'POST':
        sort_selection = request.form['sort_by']
        sort_genre_selection = request.form['sort_genre']
        search_query = request.form.get('search_query', '')
        
        movies = Movie.query.order_by(Movie.timestamp.desc())
        
        if sort_selection == '1':
            movies = Movie.query.order_by(Movie.timestamp.desc())
        elif sort_selection == '2':
            movies = Movie.query.order_by(Movie.title.desc())
        elif sort_selection == '3':
            movies = Movie.query.order_by(Movie.average_rating.desc())
            
        if sort_genre_selection != 'None':  # Check if a genre is selected
            movies = Movie.query.filter_by(genre=sort_genre_selection).order_by(Movie.timestamp.desc())
            
        if search_query:
            movies = movies.filter(or_(Movie.title.ilike(f'%{search_query}%')))

        sort_form = SortForm()
        return render_template('premium_index.html', title="Movie Ratings", movies=movies.all(),  form=sort_form)

    if request.method == 'GET':
        movies = Movie.query.order_by(Movie.timestamp.desc())
        sort_form = SortForm()
        return render_template('premium_index.html', title="Movie Ratings", movies=movies.all(), form=sort_form)
    
@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/normal_index', methods=['POST', 'GET'])
def normal_index():
    if request.method == 'POST':
        sort_selection = request.form['sort_by']
        sort_genre_selection = request.form['sort_genre']
        search_query = request.form.get('search_query', '')
        
        movies = Movie.query.order_by(Movie.timestamp.desc())
          
        if sort_selection == '1':
            movies = Movie.query.order_by(Movie.timestamp.desc())
        elif sort_selection == '2':
            movies = Movie.query.order_by(Movie.title.desc())
        elif sort_selection == '3':
            movies = Movie.query.order_by(Movie.average_rating.desc())
            
        if sort_genre_selection != 'None':  # Check if a genre is selected
            movies = Movie.query.filter_by(genre=sort_genre_selection).order_by(Movie.timestamp.desc())
        if search_query:
            movies = movies.filter(or_(Movie.title.ilike(f'%{search_query}%')))
            
        sort_form = SortForm()
        return render_template('normal_index.html', title="Movie Ratings", movies=movies.all(),  form=sort_form)

    if request.method == 'GET':
        movies = Movie.query.order_by(Movie.timestamp.desc())
        sort_form = SortForm()

        return render_template('normal_index.html', title="Movie Ratings", movies=movies.all(), form=sort_form)



@bp_routes.route('/postMovie', methods=['GET', 'POST'])
@login_required
def postMovie():
    movieForm = MovieForm()
    title = "(No Movie)"
    genre = "(No Genre)"
    if movieForm.validate_on_submit():
        title = movieForm.title.data
        genre = movieForm.genre.data
        if Movie.query.filter_by(title=title).first() != None:
            flash("Movie " + movieForm.title.data + " already exists")
            return render_template('add_movie.html', title=movieForm.title.data, genre = movieForm.genre.data, movieForm=movieForm)
        average_rating = 0

        if title:
            newMovie = Movie(title=title, average_rating=average_rating, member_id=current_user.id, genre = genre)
            db.session.add(newMovie)
            db.session.commit()
            flash("Movie " + movieForm.title.data + " created")
            if current_user.user_type == "Normal":
                return render_template('n_intermediate.html', title=title)
            else:
                return render_template('p_intermediate.html', title=title)
    return render_template('add_movie.html', title=movieForm.title.data, movieForm=movieForm)
        
        
@bp_routes.route('/postReview/<title>', methods=['GET', 'POST'])
@login_required
def postReview(title):
    movie = Movie.query.filter_by(title=title).first()
    reviews = movie.reviews
    for review in reviews:
        if review.member_id == current_user.id:
            flash(f"Already added rating or review for {movie.title}")
            return redirect(url_for('routes.movieRating', title=title))
    
    reviewForm = ReviewForm()
    if reviewForm.validate_on_submit() and movie:
        review_text = ""
        if reviewForm.review.data:
            review_text = reviewForm.review.data
        if reviewForm.rating.data:
            rating = reviewForm.rating.data
            newReview = Review(movie_title=movie.title, review=review_text, rating=rating, member_id=current_user.id)
            movie.reviews.append(newReview)
            db.session.add(newReview)
            db.session.commit()
            flash("Review created")
            
            # Calculate and commit the average rating score
            total = 0 
            for review in list(movie.reviews):
                total += review.rating
            if len(list(reviews)) != 0:
                avg = round(total/len(list(reviews)))
            else:
                avg = round(0)
            movie.average_rating = avg
            db.session.commit()
            
            if current_user.user_type == "Normal":
                return redirect(url_for('routes.normal_index'))
            else:
                return redirect(url_for('routes.premium_index'))
    elif not movie:
        flash("Invalid movie name privided")
            
    return render_template('create.html', title=title, reviewForm=reviewForm)



@bp_routes.route('/normal_profile', methods=['GET', 'POST'])
@login_required
def normal_profile():
    user_reviews = current_user.reviews.all()  
    return render_template('normal_profile.html', user_reviews=user_reviews)


@bp_routes.route('/premium_profile', methods=['GET', 'POST'])
@login_required
def premium_profile():
    user_reviews = current_user.reviews.all()  
    return render_template('premium_profile.html', user_reviews=user_reviews)


@bp_routes.route('/friends', methods=['GET', 'POST'])
@login_required
def friends():
    getFriendForm = GetFriendForm()

    if getFriendForm.validate_on_submit():
        friend_username = getFriendForm.friend_username.data
        friend = Member.query.filter_by(username=friend_username).first()
        if friend:
            if friend.id == current_user.id:
                flash("Cannot add yourself as a friend")
            elif friend in current_user.friends:
                flash("Friendship already exists")
            else:
                current_user.friends.append(friend)
                db.session.commit()
                flash("\"" + friend_username + "\" has been added to your friends list!")
        else:
            flash("User \"" + friend_username + "\" does not exist.")
            return redirect(url_for('routes.friends'))
    friends = current_user.friends
    return render_template('friends.html', getFriendForm=getFriendForm, friends=friends)


@bp_routes.route('/rating/<title>', methods=['GET', 'POST'])
def movieRating(title):
    getFriendForm = GetFriendForm()
    movie = Movie.query.filter_by(title=title).first()
    
    if getFriendForm.validate_on_submit():
        friend_username = getFriendForm.friend_username.data
        friend = Member.query.filter_by(username=friend_username).first()
        if friend:
            if friend.id == current_user.id:
                flash("Cannot recommend to yourself")
            else:
                premium_user = Member.query.filter_by(username = friend_username).first()
                premium_user.recommended_movies.append(movie)
                db.session.commit()
                flash("Movie recommendation sent! ")
        else:
            flash("User \"" + friend_username + "\" does not exist.")
    
    reviews = list(movie.reviews)
    total = 0
    for review in movie.reviews:
        total += review.rating
    
    if len(reviews) != 0:
        avg = round(total/len(reviews))
    else:
        avg = 0
        
    movie.average_rating = avg
    db.session.commit()

    if current_user.user_type == "Normal":
        return render_template('normal_rating.html', title=title, reviews=reviews, average = avg)
    else:

        return render_template('premium_rating.html', title=title, reviews=reviews, average = avg, getFriendForm=getFriendForm)
    
    
@bp_routes.route('/recommend', methods=['GET', 'POST'])
def seeRecommended():
    movies = current_user.recommended_movies
    return render_template('recommended.html', movies=movies)


@bp_routes.route('/watch_later', methods=['GET', 'POST'])
def watchLater():
    movies = current_user.watch_later_movies
    return render_template('watch_later.html', movies=movies)


@bp_routes.route('/watched', methods=['GET', 'POST'])
def watched():
    movies = current_user.watched_movies
    return render_template('watched.html', movies=movies)


@bp_routes.route('/addToWatched/<title>', methods=['GET', 'POST'])
def addToWatched(title):
    themovie = Movie.query.filter_by(title=title).first()
    username = current_user.username
    premium_user = Member.query.filter_by(username = username).first()
    if themovie:
        premium_user.watched_movies.append(themovie)
        db.session.commit()
    flash("Movie added to watched list ")
    movies = premium_user.watch_later_movies
    return render_template('watched.html', movies=movies)


@bp_routes.route('/addToToWatch/<title>', methods=['GET', 'POST'])
def addToToWatch(title):
    themovie = Movie.query.filter_by(title=title).first()
    username = current_user.username
    premium_user = Member.query.filter_by(username = username).first()
    if themovie:
        premium_user.watch_later_movies.append(themovie)
        db.session.commit()
    flash("Movie added to watch later ")
    movies = premium_user.watch_later_movies
    return render_template('watch_later.html', movies=movies)


@bp_routes.route('/edit_review/<review_id>', methods=['GET', 'POST'])
@login_required
def edit_review(review_id):
    review = Review.query.get(review_id)
    if current_user.id != review.member_id:
        flash("Cannot edit review")
        return redirect(url_for('routes.movieRating', title=review.movie_title))

    editForm = EditForm(obj=review)

    if editForm.validate_on_submit():
        review.rating = editForm.rating.data
        review.review = editForm.review.data
        db.session.commit()
        flash("Review updated successfully")
        return redirect(url_for('routes.movieRating', title=review.movie_title))

    return render_template('edit_review.html', review=review, editForm=editForm)


@bp_routes.route('/like/<post_id>/<title>', methods = ['POST']) 
def like(post_id, title): # the title is needed because I want to redirect the user to the correct .html at the end
    post = Review.query.get(post_id) # changed post_id to post_id.idd


    if post != None: # none to
        stuck = str(current_user)
        stuck = stuck.split(",")
        #['<Member 1', 'Calvin', 'Calvin@calvin.com', 'pbkdf2:sha256:600000$uu2S9qPXaiSeEZT6$8efdfa17476f9321fa6c38ceb47d2b1373c5acb1d6ddba3c03c3d83625bfe3f1 >']
        # the above comment is what current_user looks like before I process it
        userstr = ""
        reddog = 0
        for i in stuck: #this splits the current_user into just the name to make parsing the whovoted string easier
            if(reddog== 1):
                userstr = i
            reddog +=1
        votedocket = post.whovoted # this variable is just here to be shorter to type
        if(votedocket == None): # no one has voted
            post.likecount +=1  # adds one like 
            votedocket = userstr + "," # vote docket is equal to the name of the first person to vote plus a comma
            post.whovoted = votedocket # I could set this equal to the above but it works
        else: # we have to find if this user has voted before and add or subtract from likes based on result
        #flash(votedocket)  
            substrings = votedocket.split(',') # this splits vote docket into individual names
            listify = [substring.strip() for substring in substrings] # removes spaces
            canvote = 1 # 1 mean you can like 0 means you will unlike
            newstring = None
            for stringy in listify:
                if(stringy == userstr): #they have voted already
                    canvote = 0
            if(canvote ==1):
                post.likecount += 1 # adds a like
                listify.append(userstr)
            else:
                post.likecount-= 1 # removes your like 
                listify.remove(userstr)
            for name in listify:
                #flash("name len:")
                #flash(len(name))
                if(len(name) != 0): # this is necessary otherwise new string fills up with commas 
                    if(newstring == None):
                        #flash("in note should show once")
                        newstring = name +","
                    else:
                        newstring = newstring + name + ","

            #flash("sring end ")
            #flash(newstring)
            post.whovoted = newstring # this updates who votes to the new string

        db.session.commit()
        #flash(type(current_user))
    else:
        flash('Error 1 Post Unfound')
        #return redirect(url_for("routes.normal_index"))

    movie = Movie.query.filter_by(title=title).first() # everything after here is for getting you back to the correct URL for the user
    reviews = list(movie.reviews) 
    total = 0
    for review in movie.reviews:
        total += review.rating

    if len(reviews) != 0:
        ingersoll = round(total/len(reviews)) # ingersoll is average
    else:
        ingersoll = round(0)

    movie.average_rating = ingersoll

    if current_user.user_type == "Normal":
        return render_template('normal_rating.html', title=title, reviews=reviews, average = ingersoll, eltitle = title)
    else:
        return render_template('premium_rating.html', title=title, reviews=reviews, average = avg, eltitle = title)
    
