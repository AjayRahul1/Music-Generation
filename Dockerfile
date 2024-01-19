FROM python:3.10
WORKDIR /app
COPY req.txt /app/
RUN pip install -r req.txt
COPY . /app/
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]