import os

#################### Variables ####################
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = os.environ.get('REDIRECT_URI')
USER_AGENT = os.environ.get('USER_AGENT')
GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
GCP_REGION = os.environ.get("GCP_REGION")
BQ_DATASET= os.environ.get('BQ_DATASET')
BQ_REGION = os.environ.get("BQ_REGION")

#################### Constant ####################
SUBREDDITS = ['whatsbotheringyou']
