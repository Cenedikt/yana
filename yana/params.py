import os

#################### Variables ####################
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
USER_AGENT = os.environ.get('USER_AGENT')
GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
GCP_REGION = os.environ.get("GCP_REGION")
DATASET_ID_POSTS= os.environ.get('DATASET_ID_POSTS')
DATASET_ID_COMMENTS = os.environ.get('DATASET_ID_COMMENTS')
BQ_REGION = os.environ.get("BQ_REGION")

#################### Constant ####################
SUBREDDITS = ['askatherapist']
