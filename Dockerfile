FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install requests

# Run the script
CMD ["python", "main.py"]
