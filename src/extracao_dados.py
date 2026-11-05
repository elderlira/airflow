from datetime import datetime, date, timedelta
import requests
import json

timestamp_format = "%Y-%m-%dT%H:%M:%S.00Z"

today = date.today()
start_time = today - timedelta(days=1)
end_time = today

query="python"

tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id, in_reply_to_user_id,public_metrics,lang,source, text"
user_fields = "expansions=author_id&user.fields=id,name, username, created_at"

url_raw = f"https://labdados.com/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&start_time={start_time.strftime(timestamp_format)}&end_time={end_time.strftime(timestamp_format)}"
response = requests.get(url_raw)


if response.status_code == 200:

    dados = response.json()

    print(json.dumps(dados, indent=4, sort_keys=True))

    while "next_token" in dados.get("meta", {}):

        next_token = dados["meta"]["next_token"]

        url_raw = (
            f"https://labdados.com/2/tweets/search/recent?"
            f"query={query}"
            f"&{tweet_fields}"
            f"&{user_fields}"
            f"&start_time={start_time.strftime(timestamp_format)}"
            f"&end_time={end_time.strftime(timestamp_format)}"
            f"&next_token={next_token}"
        )

        response = requests.get(url_raw)

        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            break

        dados = response.json()

        print(json.dumps(dados, indent=4, sort_keys=True))