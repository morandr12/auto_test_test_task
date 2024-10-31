FROM python:alpine

# Update apk repo
RUN echo "https://dl-4.alpinelinux.org/alpine/latest-stable/main/" >> /etc/apk/repositories && \
    echo "https://dl-4.alpinelinux.org/alpine/latest-stable/community/" >> /etc/apk/repositories
RUN apk update

# Install chromedriver
RUN apk add --no-cache chromium chromium-chromedriver tzdata

# Copy project files to the working directory
WORKDIR /usr/workspace
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Run tests
CMD ["pytest", "-rfx", "-sv"]
