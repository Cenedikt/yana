# YANA

## Description
Mental Health Platform for finding people who went through similar experiences

## Data analysis
- Data Source: Reddit.com multiple subreddits
- Type of analysis: Semantic search

Please document the project the better you can.

## Setup

### Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for yana in github.com/Cenedikt. If your project is not set please add it:

Create a new project on github.com/Cenedikt/yana
Then populate it:

```bash
##   e.g. if the group is "Cenedikt" and project_name is "yana"
git remote add origin git@github.com:Cenedikt/yana.git
git push -u origin master
git push -u origin --tags
```

Functional test with a script:

```bash
cd
mkdir tmp
cd tmp
yana-run
```

### Install

Go to `https://github.com/Ceneidikt/yana` to see the project, manage issues,


Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:Cenedikt/yana.git
cd yana
pip install -r requirements.txt
make clean install test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
yana-run
```
### Setup environment variable

- Locate the sample environment variable file in the repository. It is usually named something like .env.sample or .env.example.
- Open the sample environment variable file in a text editor.
- Review each variable name and its corresponding value. Pay attention to any potential spelling mistakes in the variable names or their values.
- Compare the variable names in the sample file with the expected variable names used in your application's code. Ensure that they match exactly, including any capitalization or underscores.
- Verify that the values assigned to the variables in the sample file are correct and match the expected format or content.
- If you encounter any spelling mistakes or incorrect variable names/values, correct them in the sample file.
- Save the changes to the sample environment variable file

## to scrap Reddit

first, the subreddits that should be scrapped have to be defined in the params.py file
than run
```bash
make scraper
```

### For local tests some helpful commands

fist the some initialize has to be done
the csv and embedding.pt will be created locally
```bash
make initialize
```
to start frontend
```bash
streamlit run
```
to start api
```bash
uvicorn yana.api.api:app --reload
```

### Docker setup

Before building an image
some initialize has to be done
the csv and emmbeding.pt will be created locally
```bash
make initialize
```
#### for Development

build new docker image :
```bash
docker build -t $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:dev .
```
if needed test the docker image locally:
```bash
docker run -e PORT=8000 -p 8000:8000 --env-file .env $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:dev
```
push the image to GoogleCloud:
```bash
docker push $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:dev
```
Deploy the docker container on GoogleCloud:
```bash
gcloud run deploy --image $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:dev --memory $GCR_MEMORY --region $GCP_REGION --env-vars-file .env.yaml --project $GCP_PROJECT_ID
```

#### for Production

build new docker image :
```bash
docker build -t $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:prod .
```
if needed test the docker image locally:
```bash
docker run -e PORT=8000 -p 8000:8000 --env-file .env $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:prod
```
push the image to GoogleCloud:
```bash
docker push $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:prod
```
Deploy the docker container on GoogleCloud:
```bash
gcloud run deploy --image $GCR_REGION/$GCP_PROJECT_ID/$GCR_IMAGE:prod --memory $GCR_MEMORY --region $GCP_REGION --env-vars-file .env.yaml --project $GCP_PROJECT_ID
```
