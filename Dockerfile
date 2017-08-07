FROM python:3.4

RUN groupadd -r appuser && useradd -r -g appuser appuser
RUN mkdir /app
COPY requirements.txt /app/
COPY app.py /app/
WORKDIR /app

RUN pip install -r requirements.txt
USER appuser

EXPOSE 8080
ENTRYPOINT ["python", "app.py"]
