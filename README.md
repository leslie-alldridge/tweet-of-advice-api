# Tweet Of Advice API

API Endpoint: https://eda-tweets.herokuapp.com

Note: Using free server so first request may take 20 seconds to respond / fail. Following that it should be instant.

Please use this API responsibly. It's designed to help students at EDA post JSON objects to an API endpoint.

# Get tweets

GET: /tweet

# Get tweet by id

GET: /tweet/:id

# Save a tweet

POST: /tweet

Must contain the following JSON key value pairs (ID automatically appends and you can select your own values to append):

```
{
  "tweet": "Nine weeks goes really really fast!",
  "author": "Luke"
}
```
# Reset DB 
```
$ python
>> from app import db
>> db.create_all()
>> exit()
```
