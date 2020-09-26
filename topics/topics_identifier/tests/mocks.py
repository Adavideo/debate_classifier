from topics_identifier.models import ClusterTopic
from common.testing.mock_documents import *
from common.testing.mock_web_client import *
from common.testing.mock_threads import *
from common.testing.mock_topics import mock_topic
from .mock_clusters import mock_clusters_list


def mock_topic_with_clusters(topic_name="test", with_documents=True):
    topic = mock_topic(topic_name)
    clusters_list = mock_clusters_list(with_documents=with_documents)
    for cluster in clusters_list:
        ct = ClusterTopic(topic=topic, cluster=cluster)
        ct.save()
    return topic, clusters_list

def mock_threads_and_clusters_with_topic():
    topic, clusters_list = mock_topic_with_clusters()
    threads = mock_threads_with_topic(topic)
    news = Document.objects.filter(is_news=True)
    clusters_list[0].add_document(news[0].content)
    clusters_list[1].add_document(news[1].content)
    return topic
