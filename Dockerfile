FROM python:3.9-slim

WORKDIR /app

COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 10", "-b", "0.0.0.0:8000", "main:app"]

