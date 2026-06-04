# Use official lightweight Python base runtime environment image
FROM python:3.10-slim

# Establish isolated internal task space environment path 
WORKDIR /app

# Pull app codebase structural tree into build layer context
COPY . /app

# Run target pip install parameters configurations
RUN pip install --no-cache-dir -r requirements.txt

# Explicitly open interface networking gateway to external mappings
EXPOSE 5000

# Execute command to start application inside the container
CMD ["python", "app.py"]