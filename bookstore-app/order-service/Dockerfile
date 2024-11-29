FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install flask flask_cors
EXPOSE 5002
#ENV DATABASE /Users/tejaswath/Desktop/Build_something/bookstore-app/shared/bookstore.db
ENV DATABASE=/app/shared/bookstore.db
CMD ["python", "order_service.py"]