FROM python:3.7-slim
LABEL maintainer="James Turk <james@openstates.org>"

ENV PYTHONIOENCODING 'utf-8'
ENV LANG 'C.UTF-8'
ENV LC_ALL 'C.UTF-8'

RUN apt update && apt install -y libgdal-dev poppler-utils antiword tesseract-ocr
RUN pip install poetry

ADD . /opt/text-extraction
WORKDIR /opt/text-extraction
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "./text_extract.py"]
