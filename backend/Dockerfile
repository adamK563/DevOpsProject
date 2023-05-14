FROM python:3.10.8

COPY . /backend
WORKDIR /backend

RUN pip install -r requirments.txt

EXPOSE 8000

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t backend .
# docker run -p 8000:8000 backend