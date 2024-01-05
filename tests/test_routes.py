"""
This file contains the functional tests for the routes.
These tests use GETs and POSTs to different URLs to check for the proper behavior.
Resources:
    https://flask.palletsprojects.com/en/1.1.x/testing/ 
    https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/ 
"""
import os
import pytest
from app import create_app, db
from app.Model.models import Member, Review
from config import Config

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = 'bad-bad-key'
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True


# To run tests:
# python3 -m pytest -v tests/test_routes.py

@pytest.fixture(scope='module')
def test_client():
    # create the flask application ; configure the app for tests
    flask_app = create_app(config_class=TestConfig)

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield  testing_client 
    # this is where the testing happens!
 
    ctx.pop()

def new_member(uname, uemail,passwd):
    member = Member(username=uname, email=uemail)
    member.set_password(passwd)
    return member

@pytest.fixture
def init_database():
    # Create the database and the database table
    db.create_all()
    #add a user    
    member1 = new_member(uname='sakire', uemail='sakire@wsu.edu',passwd='1234')
    # Insert user data
    db.session.add(member1)
    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

def test_register_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_register(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' form is submitted (POST)
    THEN check that the response is valid and the database is updated correctly
    """
    # Create a test client using the Flask application configured for testing
    response = test_client.post('/register', 
                          data=dict(username='john', email='john@wsu.edu',password="bad-bad-password",password2="bad-bad-password"),
                          follow_redirects = True)
    assert response.status_code == 200

    s = db.session.query(Member).filter(Member.username=='john')
    assert s.first().email == 'john@wsu.edu'
    assert s.count() == 1
    assert b"Sign In" in response.data   
    assert b"Please log in to access this page." in response.data

def test_invalidlogin(test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with wrong credentials
    THEN check that the response is valid and login is refused 
    """

    response = test_client.post('/login', 
                          data=dict(username='sakire', password='12345',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data  #You may update the assertion condition according to the content of your login page. 

def test_login_logout(request,test_client,init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' form is submitted (POST) with correct credentials
    THEN check that the response is valid and login is succesfull 
    """
    response = test_client.post('/login', 
                          data=dict(username='sakire', password='1234',remember_me=False),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Welcome to Smile Portal!" in response.data  #You may update the assertion condition according to the content of your index page. 

    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"Please log in to access this page." in response.data     #You may update the assertion condition according to the content of your  page. 

def test_postReview(test_client,init_database):
    """
    GIVEN a Flask application configured for testing , after user logs in,
    WHEN the '/postReview' page is requested (GET)  AND /ReviewForm' form is submitted (POST)
    THEN check that response is valid and the class is successfully created in the database
    """
    #login
    response = test_client.movie('/login', 
                        data=dict(username='sakire', password='1234',remember_me=False),
                        follow_redirects = True)
    assert response.status_code == 200
    assert b"Movie Ratings" in response.data  #You may update the assertion condition according to the content of your  page.
    
    #test the "PostReview" form 
    response = test_client.get('/postReview')
    assert response.status_code == 200
    assert b"Post New Review" in response.data #You may update the assertion condition according to the content of your  page.
    
    #test posting a review story
    response = test_client.post('/postReview', 
                          data=dict(title='My test review', review='This is my first test review.',rating=2),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Movie Ratings" in response.data   #You may update the assertion condition according to the content of your  page.
    assert b"My test review" in response.data 
    assert b"This is my first test review." in response.data 

    c = db.session.query(Review).filter(Review.title =='My test review')
    assert c.count() >= 1 #There should be at least one post with review "Here is another review."


    response = test_client.review('/postReview', 
                          data=dict(title='Second review', review='Here is another review.',rating=1),
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Movie Ratings" in response.data  #You may update the assertion condition according to the content of your  page.
    assert b"Second review" in response.data 
    assert b"Here is another review." in response.data 

    c = db.session.query(Review).filter(Review.body =='Here is another review.')
    assert c.count() >= 1 #There should be at least one post with review "Here is another review."

    assert db.session.query(Review).count() == 2

    #finally logout
    response = test_client.get('/logout',                       
                          follow_redirects = True)
    assert response.status_code == 200
    assert b"Sign In" in response.data
    assert b"Please log in to access this page." in response.data   #You may update the assertion condition according to the content of your  page.