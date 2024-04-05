# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py, vision.py, and .env files into the container
COPY app.py .
COPY vision.py .
COPY .env .

# Upgrade the google-generativeai and google-auth libraries to the latest version
RUN pip install --no-cache-dir --upgrade google-generativeai google-auth

# Expose the port that the Streamlit app runs on
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]