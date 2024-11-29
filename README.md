# bookstore-app
cloud computing assignment 

Introduction

The Bookstore Application is designed to demonstrate microservices architecture principles using Kubernetes. It consists of:
	•	Book Service: Manages book data.
	•	Order Service: Manages order data.
	•	Streamlit UI: Provides a web interface for users.
	•	Database: A shared SQLite database for persistent storage.
 Features

	•	Add New Books: Users can add books with a title and author.
	•	View Books: Users can view a list of all available books.
	•	Place Orders: Users can place orders for books by specifying the book ID and quantity.
	•	View Orders: Users can view all orders placed.
 Architecture Overview

The application follows a microservices architecture with the following components:

Book Service

	•	Technology: Flask, SQLite
	•	Functionality:
	•	POST /books: Add a new book.
	•	GET /books: Retrieve all books.
	•	Port: 5001

Order Service

	•	Technology: Flask, SQLite
	•	Functionality:
	•	POST /orders: Place a new order.
	•	GET /orders: Retrieve all orders.
	•	Port: 5002

Streamlit UI

	•	Technology: Streamlit
	•	Functionality:
	•	User interface to interact with Book and Order services.
	•	Port: 8501

Database

	•	Technology: SQLite
	•	Storage: Persistent Volume in Kubernetes

 Prerequisites

	•	Docker: For building and running container images.
	•	Kubernetes: For deploying the application.
	•	Minikube is recommended for local testing.
	•	kubectl: Command-line tool to interact with Kubernetes.
	•	Git: To clone the repository.

 Working screenshots of the project: 
 <img width="866" alt="image" src="https://github.com/user-attachments/assets/5d0f80d4-ca0b-4877-b331-48e5bd14d7d0">
 

