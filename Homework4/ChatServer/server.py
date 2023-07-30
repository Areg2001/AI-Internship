"""
    Server module, which bulid a server where we can chat with each other...
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clients = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

def remove_client(client: socket.socket) -> None:

    """
         Removes a client's socket from the list of connected clients.
    """

    if client in clients:
        client.close()
        clients.remove(client)

def broadcast_message(message: str, sender: socket.socket) -> None:

    """
         Broadcasts a message to all connected clients except the sender.
    """

    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                print("Client disconnected...")
                remove_client(client)


def handle_client(client: socket.socket, address: tuple) -> None:

    """
        Handles communication with a client.
    """

    print(f"{address} connect...")

    try:
        client.send("Hello dear!".encode())

        while True:
            message = client.recv(1024).decode()
            if message.lower() == "exit":
                break
            broadcast_message(f"{address}: {message}", client)

    except:
        print("Client disconnected...")

    finally:
        remove_client(client)


def start_server() -> None:

    """
         Starts the chat server and listens for incoming connections.

    """

    server_socket.listen(5)
    print(f"Chat started {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()