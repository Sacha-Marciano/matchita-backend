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

with Diagram("Document AI Platform Architecture", show=False, direction="TB"):
    user = Users("User")

    # Frontend
    with Cluster("Frontend (Next.js)"):
        frontendNext = Typescript("Next.js frontend")
        login = Typescript("login")
        homepage = Typescript("home")
        addRoom = Typescript("Add room")
        getRoom = Typescript("Room click")
        roompage = Typescript("roompage")
        addDoc = Typescript("Add doc")

    # Backend
    with Cluster("Backend (Next.js)"):
        backendNext = Nextjs("Next.js backend")
        loginRoute = Routes("next auth")
        saveUserRoute = Routes("Save user")
        addRoomRoute = Routes("Add Room")
        getRoomsRoute = Routes("Get Rooms")
        getRoomRoute = Routes("Get Room")
        getDocsRoute = Routes("Get Docs")
        addDocsRoute = Routes("Add Doc")

    # External Services
    with Cluster("External Services"):
        mongo = Mongodb("MongoDB Atlas")

    # Google Cloud
    with Cluster("Google Cloud Platform"):
        backend = Run("FastAPI")
        embedRoute = Router("Vectorize")
        classifyRoute = Router("Classify")
        embedding = AIPlatform("Gemini Embedding 001")
        reasoning = AIPlatform("Gemini 2 Flash Lite")
        gdrive = Recombee("Google Drive")
        oauth = Oauth2Proxy("Google OAuth")

    # === Login Flow ===
    user >> red >> login >> red >> loginRoute >> red >> oauth >> red >> saveUserRoute >> red >> mongo
    saveUserRoute >> red >> getRoomsRoute >> red >> homepage

    # === Add Room Flow ===
    user >> purple >> addRoom >> purple >> addRoomRoute >> purple << mongo
    addRoomRoute >> purple >> homepage

    # === Get Room Flow ===
    user >> indigo >> getRoom >> indigo >> getRoomRoute >> indigo << mongo
    getRoomRoute >> indigo >> getDocsRoute >> indigo >> roompage

    # === Add Document Flow ===
    user >> blue >> addDoc >> blue >> addDocsRoute >> blue << embedRoute >> blue << embedding
    addDocsRoute >> blue << classifyRoute >> blue << reasoning
    addDoc >> blue << gdrive
