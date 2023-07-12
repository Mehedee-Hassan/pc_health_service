FROM python:3.9-bookworm

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP="./src/app.py"

EXPOSE 5000
CMD ["flask" , "run" ]
