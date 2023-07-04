# brain-tumor-classifier

A website that hosts a brain tumor classifier powered by a CNN model, hosted on an API made with FastAPI.

To run on local machine:
- clone the repo
- you can train and modify the models in train.py with data in the 'data' folder
- install requirements for the API: 'pip install -r requirements api/requirements.txt'
- cd into the api folder and run 'uvicorn main:app' in the command line to start the FastAPI
- go to the site and upload images to use the model
