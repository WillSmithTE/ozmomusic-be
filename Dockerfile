FROM python:3

WORKDIR /usr/src/app

ENV AWS_ACCESS_KEY_ID=AKIA22JFITDT7SQ4W3IY
ENV AWS_SECRET_ACCESS_KEY=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
ENV AWS_DEFAULT_REGION=ap-southeast-2

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./main.py" ]