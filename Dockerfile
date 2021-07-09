#Base Image to use
FROM python:3.9-slim

#Expose port 8080
EXPOSE 8080

#Copy Requirements.txt file into app directory
COPY requirements.txt rps_app/requirements.txt

#install all requirements in requirements.txt
RUN pip install -r rps_app/requirements.txt

#Copy all files in current directory into app directory
COPY . /rps_app

#Change Working Directory to app directory
WORKDIR /rps_app

#Run the application on port 8080
ENTRYPOINT ["streamlit", "run", "rps_app.py", "--server.port=8080", "--server.address=0.0.0.0"]