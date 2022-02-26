FROM python:3.8.3-alpine

RUN adduser -D test_flask
USER test_flask
WORKDIR /home/test_flask

ENV PATH="/home/app/.local/bin:${PATH}"
RUN /usr/local/bin/python -m pip install --upgrade pip

ENV PATH="/usr/local/bin/python:${PATH}"
RUN pip install --user --no-cache-dir selenium


COPY --chown=test_flask:test_flask e2e.py /home/test_flask/

CMD [ "python", "/home/test_flask/e2e.py" ]