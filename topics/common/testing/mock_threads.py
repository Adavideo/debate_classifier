from timeline.models import Thread
from .mock_documents import mock_news, mock_comments


def mock_thread(thread_number, with_documents=False, news_number=None):
    if not news_number: news_number = thread_number
    if not with_documents:
        thread = Thread(number=thread_number)
        thread.save()
    else:
        news = mock_news(number=news_number)
        thread = news.thread
        # Assign comments
        start = news_number*2
        end = start+2
        comments_list = mock_comments()[start:end]
        for comment in comments_list:
            comment.thread = thread
            comment.save()
    return thread

def mock_threads_list():
    thread0 = mock_thread(thread_number=0, with_documents=True, news_number=0)
    thread1 = mock_thread(thread_number=1, with_documents=True, news_number=1)
    return [thread0, thread1]

def mock_threads_with_topic(topic):
    topic.save()
    thread_list = mock_threads_list()
    topic.assign_threads_list(thread_list)
    return thread_list
