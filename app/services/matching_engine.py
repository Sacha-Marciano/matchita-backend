# services/matching_engine.py
from google.cloud import aiplatform
from google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint import MatchingEngineIndexEndpoint

aiplatform.init(project="571768511871", location="us-central1")

# These values come from Vertex UI
INDEX_ENDPOINT_NAME = "projects/571768511871/locations/us-central1/indexEndpoints/4626113810007064576"
DEPLOYED_INDEX_ID = "matchita-index-deployed"

index_endpoint = MatchingEngineIndexEndpoint(index_endpoint_name=INDEX_ENDPOINT_NAME)

def find_nearest_neighbors(vector, k=1):
    response = index_endpoint.find_neighbors(
        deployed_index_id=DEPLOYED_INDEX_ID,
        queries=[vector],
        num_neighbors=k
    )
    return response[0].neighbors
