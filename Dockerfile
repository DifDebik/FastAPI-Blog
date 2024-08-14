FROM python:3.11

# Set the working directory in the container
WORKDIR /FastAPI_blog

# Copy the requirements file into the working directory
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port of FastAPI application will listen on
EXPOSE 8000

# cd to app directory
WORKDIR /FastAPI_blog/app

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
