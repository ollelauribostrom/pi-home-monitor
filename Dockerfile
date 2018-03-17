FROM frolvlad/alpine-python3
LABEL authors="ollelauribostrom"
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
ENV FLASK_APP=src/app.py
CMD flask run --host=0.0.0.0 --port=80
