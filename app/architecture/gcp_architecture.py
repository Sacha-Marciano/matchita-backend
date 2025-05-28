from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.programming.language import Typescript
from diagrams.onprem.auth import Oauth2Proxy
from diagrams.saas.recommendation import Recombee
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import AIPlatform
from diagrams.onprem.database import Mongodb
from diagrams.gcp.network import Routes, Router
from diagrams.programming.framework import Nextjs

# Define reusable edges
red = Edge(color="red", style="bold")
purple = Edge(color="purple", style="bold")
indigo = Edge(color="indigo", style="bold")
blue = Edge(color="blue", style="bold")
green = Edge(color="green", style="bold")

with Diagram("Document AI Platform Architecture", show=False, direction="LR"):
    user = Users("User")

    # Frontend
    with Cluster("Frontend"):
        frontendNext = Typescript("Next.js Frontend")

    # Backend
    with Cluster("Backend"):
        backendNext = Nextjs("Next.js Backend")

    # External Services
    with Cluster("Database"):
        mongo = Mongodb("MongoDB Atlas")

    # Google Cloud
    with Cluster("Google Cloud Platform"):
        with Cluster("Cloud Run"):
            backend = Run("FastAPI")
        with Cluster("Vertex AI"):
            embedding = AIPlatform(f"Gemini Ebd-001\n Vectorizing")
            reasoning = AIPlatform(f"Gemini 2.0 FLite\n Reasoning")
        with Cluster("Google SDK"):
            gdrive = Recombee("Google Drive")
            oauth = Oauth2Proxy("Google OAuth")

    

    user >> red >> frontendNext >> red << backendNext 

    backendNext >> green << mongo 
    backendNext >> purple << backend 
    backendNext >> indigo << gdrive 
    backendNext >> blue << oauth 

    backend >> purple << embedding 
    backend >> purple << reasoning 
    

