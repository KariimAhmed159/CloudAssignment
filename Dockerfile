ARG VERSION_NAME=python
FROM ${VERSION_NAME}
WORKDIR /python
COPY . /python
RUN pip install nltk
RUN python -m nltk downloader stopwords punkt
CMD [ "python", "python.py" ]