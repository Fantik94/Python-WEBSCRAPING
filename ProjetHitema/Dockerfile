FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update --fix-missing && apt-get install -y wget gnupg2 unzip ca-certificates procps xdg-utils --fix-missing \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable --fix-missing \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget -q --continue -P /chromedriver "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/linux64/chromedriver-linux64.zip" \
    && unzip /chromedriver/chromedriver* -d /usr/local/bin/ \
    && rm -rf /chromedriver

COPY . .

COPY run_scrapers.sh .

CMD ["./run_scrapers.sh"]
