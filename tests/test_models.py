import warnings
warnings.filterwarnings("ignore")
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.Model.models import Member, Review
from config import Config

# To run tests:
# python3 -m unittest -v tests/test_models.py


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ROOT_PATH = '..//'+basedir
    
class TestModels(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        m = Member(username='john', email='john.yates@wsu.edu')
        m.set_password('covid')
        self.assertFalse(m.get_password('flu'))
        self.assertTrue(m.get_password('covid'))

    def test_review_1(self):
        m1 = Member(username='john', email='john.yates@wsu.com')
        db.session.add(m1)
        db.session.commit()
        self.assertEqual(m1.get_user_posts().all(), [])
        r1 = Review(movie_title='My review', review='This is my test review.', rating=75, member_id=m1.id)
        db.session.add(r1)
        db.session.commit()
        self.assertEqual(m1.get_user_posts().count(), 1)
        self.assertEqual(m1.get_user_posts().first().movie_title, 'My review')
        self.assertEqual(m1.get_user_posts().first().review, 'This is my test review.')
        self.assertEqual(m1.get_user_posts().first().rating, 75)

    def test_review_2(self):
        m1 = Member(username='john', email='john.yates@wsu.com')
        m2 = Member(username='amit', email='amit.khan@wsu.com')
        db.session.add(m1)
        db.session.add(m2)
        db.session.commit()
        self.assertEqual(m1.get_user_posts().all(), [])
        self.assertEqual(m2.get_user_posts().all(), [])
        r1 = Review(movie_title='My review 1', review='This is my first test review.', rating=50, member_id=m1.id)
        db.session.add(r1)
        r2 = Review(movie_title='My review 2', review='This is my second test review.', rating=60, member_id=m1.id)
        db.session.add(r2)
        db.session.commit()
        r3 = Review(movie_title='Another review', review='This is a review by somebody else.', rating=70, member_id=m2.id)
        db.session.add(r3)
        db.session.commit()
        # test the posts by the first user
        self.assertEqual(m1.get_user_posts().count(), 2)
        self.assertEqual(m1.get_user_posts().all()[1].movie_title, 'My review 2')
        self.assertEqual(m1.get_user_posts().all()[1].review, 'This is my second test review.')
        self.assertEqual(m1.get_user_posts().all()[1].rating, 60)
        # test the posts by the second user
        self.assertEqual(m2.get_user_posts().count(), 1)
        self.assertEqual(m2.get_user_posts().all()[0].movie_title, 'Another review')
        self.assertEqual(m2.get_user_posts().all()[0].review, 'This is a review by somebody else.')
        self.assertEqual(m2.get_user_posts().all()[0].rating, 70)


if __name__ == '__main__':
    unittest.main(verbosity=2)