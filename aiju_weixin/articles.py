import time
import xml.etree.ElementTree as ET

import articleinfo
import wechatconst

def return_news_xml(article_type, app_id, usr_open_id):
    aiju_articles = get_recent_articles(article_type)
    return create_news_xml(aiju_articles, app_id, usr_open_id)

def get_recent_articles(article_type):
    return caches.articles[article_type][:10]

def create_news_xml(articles):
    article_items = []
    article_length = len(articles)
    for a in articles:
        item = wechatconst.NEWS_ITEM_TEMPLATE.format(
            title=a[0],
            description=a[1],
            picurl=a[2],
            url=a[3]
        )
        article_items.append(item)
    wechatconst.NEWS_TEMPLATE.format(
        to_user=app_id,
        from_usr=usr_open_id,
        timestamp=int(time.time()),
        length=article_length,
        news=''.join(article_items)
    )