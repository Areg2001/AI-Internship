"""
    Client module.
"""

import socket
import threading

HOST = '127.0.0.1' 
PORT = 12345       

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages() -> None:

    """
        Receives and displays messages from the chat server.
    """

    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Clients disonnected...")
            break

def send_message() -> None:
    """
        Sends messages to the chat server.
    """

    while True:
        message = input("Enter your message: ")
        client_socket.send(message.encode())

        if message.lower() == 'exit':
            break

    client_socket.close()

if __name__ == "__main__":
    print("Connected to the chat server.")
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_message()

