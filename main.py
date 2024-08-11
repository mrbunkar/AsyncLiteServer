import socket
import asyncio
import argparse
from request_handler import Request, serve_file
from response import Response

async def accept_and_handle(loop, client: socket.socket):
    with client:
        try:
            request = await Request.from_socket(loop, client)
            if request.method == "GET":
                await serve_file(loop, client, request.path)
            else:
                client.sendall(Response.METHOD_NOT_ALLOWED_RESPONSE)
        except Exception as err:
            print(f"Failed to parse the request, Error: {err}")
            client.sendall(Response.BAD_REQUEST_RESPONSE)


async def server(port = 3030):

    host = "localhost"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server_socket.bind((host, port))
        
        # Listen for incoming connections with a backlog of 5
        server_socket.listen(5)
        print(f"Server listening on the port {port}")
        loop = asyncio.get_event_loop()

        while True:
            client_socket, client_addr = await loop.sock_accept(server_socket)
            print("New connection from {}".format(client_addr))
            await loop.create_task(accept_and_handle(loop, client_socket))


if __name__ == "__main__":
    asyncio.run(server())
