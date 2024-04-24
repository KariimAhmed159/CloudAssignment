FROM python
WORKDIR /app
COPY paragraphs.txt /app/
COPY Python1.py /app/ 
COPY . . 
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt
CMD [ "python","./app/Python1.py" ]