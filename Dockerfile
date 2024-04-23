FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir nltk
RUN python -m nltk.downloader punkt stopwords webtext
CMD ["python", "stop_word clearing.py"]
https://youtu.be/KUECJHlV1LE?si=HM_nqggXe7adYkbh