FROM python:3.10.8

WORKDIR /app

COPY requirments.txt /app

RUN pip install -r requirments.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "frontend.py", "--server.port=8501"]

# docker build -t spacecraft-app .
# docker run -p 8501:8501 spacecraft-app
