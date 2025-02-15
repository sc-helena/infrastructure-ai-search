from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import ResourceExistsError
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SimpleField,
    SearchFieldDataType,
    SearchableField,
    SearchIndex
)
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration,
)

from config import ai_search_api_key, ai_search_endpoint, index_name

def create_index():
    credential = AzureKeyCredential(ai_search_api_key)

    # Create a search schema
    index_client = SearchIndexClient(
        endpoint=ai_search_endpoint, credential=credential)

    fields = [
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SearchableField(name="Filename", type=SearchFieldDataType.String, sortable=True),
            SearchableField(name="Content", type=SearchFieldDataType.String, sortable=True),
            SearchField(
                name="embeddedContent",
                type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                searchable=True,
                vector_search_dimensions=1536,
                vector_search_profile_name="my-vector-config",
            ),
    ]

    vector_search = VectorSearch(
        profiles=[VectorSearchProfile(name="my-vector-config", algorithm_configuration_name="my-algorithms-config")],
        algorithms=[HnswAlgorithmConfiguration(name="my-algorithms-config")],
    )

    # Create the search index
    index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
    try: 
        result = index_client.create_or_update_index(index)
    except ResourceExistsError as e: 
        print(e.message)
        index_client.delete_index(index)
        result = index_client.create_or_update_index(index)

    print(f' {result.name} created')

    # def upload_documents():
    #     client = SearchClient(service_endpoint, index_name, credential)
    #     hotel_docs = get_hotel_documents()
    #     client.upload_documents(documents=hotel_docs)