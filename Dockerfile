# Use Python 3.10 as base image
FROM python:3.10

WORKDIR /app
# copy the requirements file
COPY requirements.txt .
# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy the application code
COPY . .
# command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
