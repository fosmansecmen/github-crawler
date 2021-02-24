FROM python:3.7
WORKDIR /opt/red\ points
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY crawler.py items.py __init__.py example1.json example2.json ./
CMD python crawler.py example1.json
EXPOSE 5000/tcp