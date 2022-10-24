FROM python:3.9-slim

WORKDIR /app

COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]

