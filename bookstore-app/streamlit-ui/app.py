import streamlit as st
import requests

st.title("Bookstore App")

# Define service URLs
#BOOK_SERVICE_URL = 'http://book-service:5001'
#ORDER_SERVICE_URL = 'http://order-service:5002'
# Define service URLs with Minikube IP and NodePort
MINIKUBE_IP = '192.168.49.2'
BOOK_SERVICE_URL = f'http://{MINIKUBE_IP}:30001'  # NodePort for book-service
ORDER_SERVICE_URL = f'http://{MINIKUBE_IP}:30002'  # NodePort for order-service

# Book Management
st.header("Manage Books")

# Add Book
st.subheader("Add a New Book")
with st.form(key='add_book_form'):
    title = st.text_input("Title")
    author = st.text_input("Author")
    submit_book = st.form_submit_button("Add Book")

if submit_book:
    response = requests.post(f'{BOOK_SERVICE_URL}/books', json={'title': title, 'author': author})
    if response.status_code == 201:
        st.success("Book added successfully!")
    else:
        st.error("Failed to add book.")

# View Books
if st.button("View Books"):
    response = requests.get(f'{BOOK_SERVICE_URL}/books')
    if response.status_code == 200:
        books = response.json()['books']
        st.write(books)
    else:
        st.error("Failed to retrieve books.")

# Order Management
st.header("Manage Orders")

# Place Order
st.subheader("Place an Order")
with st.form(key='place_order_form'):
    book_id = st.number_input("Book ID", min_value=1, step=1)
    quantity = st.number_input("Quantity", min_value=1, step=1)
    submit_order = st.form_submit_button("Place Order")

if submit_order:
    response = requests.post(f'{ORDER_SERVICE_URL}/orders', json={'book_id': int(book_id), 'quantity': int(quantity)})
    if response.status_code == 201:
        st.success("Order placed successfully!")
    else:
        st.error("Failed to place order.")

# View Orders
if st.button("View Orders"):
    response = requests.get(f'{ORDER_SERVICE_URL}/orders')
    if response.status_code == 200:
        orders = response.json()['orders']
        st.write(orders)
    else:
        st.error("Failed to retrieve orders.")