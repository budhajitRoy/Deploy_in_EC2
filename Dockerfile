FROM python:3.10

WORKDIR /app_folder

COPY . .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "-m", "flask" , "run", "--host=0.0.0.0"]


# # command to build an image : docker build -t app_name .
#### command to create container and run : docker run -p 5000:8000 -d churn
