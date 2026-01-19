# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything from your project folder into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI using uvicorn and your actual file name
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]