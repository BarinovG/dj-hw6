FROM python:3

WORKDIR /usr/src/testapp

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/testapp/entrypoint.sh"]