from newsapi import NewsApiClient
from datetime import date, timedelta

newsapi = NewsApiClient(api_key='b7497764d45b4802b202606e175eefc3')

results = newsapi.get_everything(
    q='software',
    sources='bbc-news,the-verge',
    language='en',
    sort_by='publishedAt',
    from_param=(date.today() - timedelta(days=7)).isoformat(),
)

print(results)