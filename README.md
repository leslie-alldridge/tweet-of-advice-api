# Tweet Of Advice API

API Endpoint: https://eda-tweets.herokuapp.com

Note: Using free server so first request may take 20 seconds to respond / fail. Following that it should be instant.

# Get tweets

GET: /tweet

# Get tweet by id

GET: /tweet/:id

# Save a tweet

POST: /tweet

Must contain the following JSON (ID automatically appends):

```
{
  "tweet": "Nine weeks goes really really fast!",
  "author": "Luke"
}
```
