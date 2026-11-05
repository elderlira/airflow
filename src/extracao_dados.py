from datetime import datetime, date, timedelta
import requests

timestamp_format = "%Y-%m-%dT%H:%M:%S.00Z"

today = date.today()
start_time = today - timedelta(days=1)
end_time = today

query="data science"

tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id, in_reply_to_user_id,public_metrics,lang,source, text"
user_fields = "expansions=author_id&user.fields=id,name, username, created_at"

url_raw = f"https://labdados.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&start_time={start_time.strftime(timestamp_format)}&end_time={end_time.strftime(timestamp_format)}"
print(url_raw)

response = requests.get(url_raw)

if response.status_code == 200:
    print(response.json())