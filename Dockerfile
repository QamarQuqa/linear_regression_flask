# start from the base image Python
FROM python:3.6-slim

# set a directory for the app
WORKDIR /linear_model_flask

# copy all the files to the container
COPY . /linear_model_flask

# install dependencies
RUN python3 -m pip install -r requirements.txt

# define the port number the container should expose
EXPOSE 8000/tcp
EXPOSE 8000/udp

# run the command to start the app
CMD [ "python3", "./src_code/src_app.py","-path","/linear_model_flask/src_code/linear_regression_model.sav"]





