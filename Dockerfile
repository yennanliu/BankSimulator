FROM continuumio/miniconda3
ENV PYTHONPATH="$PYTHONPATH:/REST/my_app"
COPY . /my_app
WORKDIR /my_app
RUN pip install -r requirements.txt
