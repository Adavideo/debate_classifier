from config import default_documents_limit
from timeline.models import Document


def short_document_types(document_types):
    if document_types == "both":
        news = True
        comments = True
    elif document_types == "news":
        news = True
        comments = False
    else:
        news = False
        comments = True
    return news, comments

def get_documents_content(documents_list):
    documents_content = []
    for doc in documents_list:
        documents_content.append(doc.content)
    return documents_content

# Cutting to the maximum number of documents, to not overload the aviable memory.
def ensure_documents_limit(documents, limit):
    if not limit: limit = default_documents_limit
    num_documents = len(documents)
    print("Documents selected: "+str(num_documents))
    if num_documents > limit:
        print("Adjusting to limit of "+str(limit)+" documents")
        documents = documents[:limit]
    return documents

def select_documents_from_database(document_types):
    with_news, with_comments = short_document_types(document_types)
    if with_news and with_comments:
        documents_list = Document.objects.all()
    else:
        documents_list = Document.objects.filter(is_news=with_news)
    return documents_list

def select_documents(document_types, max_num_documents):
    documents_list = select_documents_from_database(document_types)
    documents_list = ensure_documents_limit(documents_list, max_num_documents)
    documents_content = get_documents_content(documents_list)
    return documents_content
