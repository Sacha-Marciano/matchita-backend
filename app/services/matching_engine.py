# services/matching_engine.py
from google.cloud import aiplatform
from google.cloud.aiplatform.matching_engine.matching_engine_index_endpoint import MatchingEngineIndexEndpoint
from google.cloud.aiplatform.matching_engine.matching_engine_index import MatchingEngineIndex
import numpy as np

aiplatform.init(project="571768511871", location="us-central1")

# These values come from Vertex UI
INDEX_ENDPOINT_NAME = "projects/571768511871/locations/us-central1/indexEndpoints/7654784559413723136"
DEPLOYED_INDEX_ID = "matchita_index_deployed_1748258697224"
INDEX_RESOURCE_NAME = "projects/571768511871/locations/us-central1/indexes/1265971091151519744"

index_endpoint = MatchingEngineIndexEndpoint(index_endpoint_name=INDEX_ENDPOINT_NAME)

def find_nearest_neighbors(vector, k=1):
    response = index_endpoint.find_neighbors(
        deployed_index_id=DEPLOYED_INDEX_ID,
        queries=[vector],
        num_neighbors=k
    )

    if not response:
        return []

    return response[0]


def upsert_vector_to_index(vector_id: str, vector: list[float]):
    index = MatchingEngineIndex(index_name=INDEX_RESOURCE_NAME)

    index.upsert_datapoints(datapoints=[
        {
            "datapoint_id": vector_id,
            "feature_vector": vector,
        }
    ])



def normalize_vector(v: list[float]) -> list[float]:
    v_np = np.array(v)
    norm = np.linalg.norm(v_np)
    return (v_np / norm).tolist() if norm > 0 else v
