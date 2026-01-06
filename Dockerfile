# Base Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port (Cloud Run expects 8080 usually)
EXPOSE 8080

# Run commands
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
