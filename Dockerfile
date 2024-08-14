FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY python-devops-project/ ./app/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", ]