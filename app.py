from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(250))
    author = db.Column(db.String(50))

    def __init__(self, tweet, author):
        self.tweet = tweet
        self.author = author


class TweetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tweet', 'author')


tweet_schema = TweetSchema(strict=True)
tweets_schema = TweetSchema(many=True, strict=True)


@app.route('/tweet', methods=['POST'])
def add_tweet():
    tweet = request.json['tweet']
    author = request.json['author']

    new_tweet = Tweet(tweet, author)

    db.session.add(new_tweet)
    db.session.commit()

    return tweet_schema.jsonify(new_tweet)


@app.route('/tweet', methods=['GET'])
def get_tweets():
    all_tweets = Tweet.query.all()
    print(all_tweets)

    result = tweets_schema.dump(all_tweets)
    print(result)
    return jsonify(result.data)


@app.route('/tweet/<id>', methods=['GET'])
def get_tweet(id):
    tweet = Tweet.query.get(id)
    return tweet_schema.jsonify(tweet)


if __name__ == '__main__':
    app.run(debug=True)
