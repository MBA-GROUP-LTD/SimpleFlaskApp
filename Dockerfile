FROM python:3
# Set application working directory
WORKDIR /usr/src/app
# Install requirments
COPY requirments.txt ./
RUN pip install --no-cache-dir -r requirments.txt
# Install the application
COPY app.py ./
# Run the application
CMD ["python", "./app.py"]