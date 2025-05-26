# main.py
from fastapi import FastAPI
from app.routes import duplicate_check, classify, save_vector
import vertexai
from dotenv import load_dotenv
from google.oauth2 import service_account
import os
import json

load_dotenv()

# Load credentials from a JSON file (ensure it's in your Render environment)
SERVICE_ACCOUNT_INFO = {"type": "service_account","project_id": "drive-viewer-app-460607","private_key_id": "cf8dc1b9a8e049ad41592386978d37f41f497e4d","private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCoSnSagp1B/FR7\nYEEw10nP5UQIlPooZSSFP5BNvyGrZfTU8y/UjKe1QLGdZbsoxLChJ98Bqmk13Uk9\nhksK5e6gZ2SqmJxE6iBEx+sN5x84j2ICO5ob5lLH74j9MryI4AYbBZZEFMrPvaAx\nTupwNTzOKzsAI/aG+2pwlRCZd9W88KoHaFXVCXCOl6MXxgtBqb3mmrraviNwZSm4\nQxv/Ey5h24B8xcBoUFlsSWkYjyeEC4L4BQ7K1uhk3kxYqQ6ivyuP4j/mhIBXmG8a\nLH6QODscJAhKNk2TOdKvCjs/36TlhNndr1Xb3OrHLikcG2WeCmA6TqVbigUVEHRu\nuzqwQjTTAgMBAAECggEATNSxJ1k6MkXgy/LF0GZ5bFBfHwvkqUyDv9GlL9lypa2G\neTINRBxy9Gz0qccoCxTBDtIFHd2O6uh753rIB9Gxf8m0S64gqdW5pa0fwtkhh9Du\nDdboJJSidmUFRZNEP7kHEI8caziS3wTTfa9pmJC1kepqpUXF5xohHgTv7yCmk/sO\nBzTVbOcvkq6BhpVuWQyB+87qaalJyfWkh1ob524pvXyZUThFO9gFNi4zubuYhKLN\n3/8OEfZSZtXl4gXpHukN2DYNTOULH5WT4pmLLlF7QJAUeZXnjUMtmkvhLqvfZS8T\ndxvyyMthfkf8beHuQbh8+OX1LIt48aGb4EFbfTF/AQKBgQDWMYe6MWpBSJwI3jAQ\nfSBqxAhzBrWzw1tPB5+KsSLLOmBK0XvOPoVuUxpIG2WUgTJdx5emPoEnPBKJu1P/\nVNnCpTj62C+HrxK2GVkKn5Qb6YBaA55satCg1//86Xu60jyC6pEKPGbEC/aT4y0m\nQimCWJxUdARvk1H0aoamk+2+zwKBgQDJI1ZekU5x28QfYi9mhQ9A/kkfpMV2oUUk\n6iXd9FJCeQS7/C6l4Cowy4iTXjqq1FfBOriVCA21aREyHnakNV9qAEIATsp/mbs4\nYrr3kamEEw5IER01dc241+rLqclfY2GXg0cBqD0dENWb4VRoH5XbiuC9t5oSYgfD\nFKgoP0PKvQKBgGVTmwy28bgefEopqf0y5FH9mK2pn+2BXkGdrpiywW34mLLsNLBV\nnVOalpVD+KLvF3+Luy7W5MxFu9NSPiNM5ZMSDEmGWb3LUYO5rAi9gxhNNv3eNmS9\nhyJ/7EadwX2YlS2tf52jA059BlHhp2sw42gZOSMumyaZP6zrc/V7h327AoGALcsu\n2d8JViDr+R04n4XB4FFEwsCX+JdlD6+DqZH7vIijDE2xLTDpSiy8zpiQkN5BkIvX\nBI9N17SxJpEK//3q2E5wuHM35W9R0degq8btKlXQVZYX6VkF2oTGP1JLt7z/tig8\nXWM5bsmraI8X0ZEHZHGtE2Se3nqVO9QTKP6mZ50CgYBT8JoG+VRtpqFGZjC6gfnQ\nxRBxgxYprLtQFCtWz3l8VtsfRK0XYPp94LJ9EmOKepjbbhF2MKmLzyrPfTag7Iza\nJAwlpaUHc4JkKGSaJbyqh8c457gd63TIzuQYRu8XZcZZ+1OfMBss6sYsjHZPe6BF\nJhJ/Pl/3tAvqm4VYWlV9oQ==\n-----END PRIVATE KEY-----\n","client_email": "matchita-rag-backend@drive-viewer-app-460607.iam.gserviceaccount.com","client_id": "107602557035275006322","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://oauth2.googleapis.com/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/matchita-rag-backend%40drive-viewer-app-460607.iam.gserviceaccount.com","universe_domain": "googleapis.com"}

credentials = service_account.Credentials.from_service_account_info(SERVICE_ACCOUNT_INFO)

# Init VertexAI
vertexai.init(project="571768511871", location="us-central1",credentials=credentials)


app = FastAPI()

app.include_router(duplicate_check.router)
app.include_router(classify.router)
app.include_router(save_vector.router)