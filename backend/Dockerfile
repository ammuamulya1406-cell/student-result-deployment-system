# 1. Use an official lightweight Python image as a base
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install Flask directly inside the container environment
RUN pip install flask

# 4. Copy all your backend files from your computer into the container
COPY . .

# 5. Tell the container to expose port 5000
EXPOSE 5000

# 6. The command to run your app when the container starts
CMD ["python", "app.py"]
