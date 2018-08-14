FROM python:3.6.5-slim
RUN apt-get update
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y zstd
RUN apt-get install -y libsm6
RUN apt-get install -y libxext6

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pytesseract
RUN pip install python-docx
RUN pip install textblob
RUN pip install nltk
RUN pip install PyPDF2
RUN pip install opencv-python
RUN pip install pillow
RUN pip install image
RUN pip install scikit-learn
RUN pip install Flask

RUN python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger');"
