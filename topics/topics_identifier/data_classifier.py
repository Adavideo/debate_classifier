from .data_importer import load_dataset
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from .util import store_clustering_attempt

def process_data(dataset):
    # Process the documents with the vectorizer.
    vectorizer = TfidfVectorizer()
    vectorized_documents = vectorizer.fit_transform(dataset.data)
    # Get the terms extracted from the documents (to be used later to show the results)
    terms = vectorizer.get_feature_names()
    data = { "vectorized documents": vectorized_documents, "terms": terms }
    return data

def get_clusters_terms(model, terms, num_clusters):
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    clusters = []
    for i in range(num_clusters):
        cluster_terms = []
        for ind in order_centroids[i, :10]:
            cluster_terms.append(terms[ind])
        clusters.append(cluster_terms)
    return clusters

def cluster_with_kmeans(data, num_clusters):
    # Build the model
    model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
    # Train the model with the pre procesed data
    model.fit(data["vectorized documents"])
    # get the terms selected for each cluster
    clusters_terms = get_clusters_terms(model, data["terms"], num_clusters)
    # predict the categories for each document
    documents_predicted_clusters = model.predict(data["vectorized documents"])
    return clusters_terms, documents_predicted_clusters

def group_documents_by_cluster(documents, documents_predicted_clusters, cluster_terms, num_clusters):
    # For each cluster stores the terms and creates an empty list to store the documents
    clustered_documents = []
    for i in range(0, num_clusters):
        clustered_documents.append({ "terms": cluster_terms[i], "documents": []})
    # Store the documents in the list of the cluster predicted
    document_index = 0
    for predicted_cluster in documents_predicted_clusters:
        document = documents[document_index]
        clustered_documents[predicted_cluster]["documents"].append(document)
        document_index += 1
    return clustered_documents

def cluster_data():
    # Load the dataset with text documents
    dataset = load_dataset()
    processed_data = process_data(dataset)
    # Try to cluster the texts with diferent numbers of clusters
    clustering_attempts = []
    for num_clusters in range(30, 41, 5):
        clusters_terms, documents_predicted_clusters = cluster_with_kmeans(processed_data, num_clusters)
        clustered_documents = group_documents_by_cluster(dataset.data, documents_predicted_clusters, clusters_terms, num_clusters)
        clustering_attempts.append( clustered_documents )
        store_clustering_attempt( clustered_documents )
    return { "clustering_attempts": clustering_attempts }
