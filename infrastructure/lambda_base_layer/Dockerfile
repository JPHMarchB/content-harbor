FROM amazonlinux:latest

# Install Python
RUN dnf install -y python3 && \
    dnf install -y python3-pip && \
    dnf install -y zip && \
    dnf clean all

# Set up PIP and Venv
RUN python3 -m pip install --ignore-installed --upgrade pip && \
    python3 -m pip install virtualenv
RUN python3 -m venv base
RUN source base/bin/activate

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt -t ./python

# Zip it up for deployment.
RUN zip -r layer.zip ./python/
ENTRYPOINT ["/bin/bash", "-l"]