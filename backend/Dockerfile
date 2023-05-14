<<<<<<< HEAD
FROM python:3.10.8

COPY . /backend
WORKDIR /backend

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t backend .
=======
FROM python:3.10.8

COPY . /backend
WORKDIR /backend

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t backend .
>>>>>>> 1731ba29a6fa2ceffc05c4c20ec8dccf5f0a8539
# docker run -p 8000:8000 backend