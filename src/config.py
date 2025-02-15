from dotenv import load_dotenv
import os

# Lade die Variablen aus der .env-Datei
load_dotenv()

#AI Search
ai_search_api_key = os.getenv("AI_SEARCH_API_KEY")
ai_search_endpoint = os.getenv("AI_SEARCH_ENDPOINT")
index_name = "cv_content"

# Document Intelligence
di_api_key = os.getenv("DOCUMENT_INTELLIGENC_API_KEY")
di_endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")

open_ai_key = os.getenv("OPENAI_API_KEY")
open_ai_endpoint = os.getenv("OPENAI_ENDPOINT")

# Others
assets_path = "src/assets"