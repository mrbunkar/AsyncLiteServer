import typing
import socket
import os
import mimetypes
import asyncio
from response import Response

SERVER_PATH = "mrbunkar"

async def iter_lines(loop: asyncio.AbstractEventLoop, client: socket.socket, bufsize: int = 16_384) -> typing.AsyncGenerator[bytes,None]:
    """
    Given a socket, read until EOF hits, returns the remainder until empty lines
    """

    buf = b""
    while True:
        data = await loop.sock_recv(client, bufsize)
        if not data:
            return 
        
        buf += data
        while b"\r\n" in buf:
            i = buf.index(b"\r\n")
            line, buf = buf[:i], buf[i+2:]
            if not line:
                return
            yield line

async def serve_file(loop: asyncio.AbstractEventLoop, client: socket.socket, path: str) -> None:
    """
    Given the path to the file, send the file to the socket. If file dosen't exist
    send 404 not found error
    """

    if path == "/":
        path = "/index.html"
    
    abs_path = os.path.normpath(os.path.join(SERVER_PATH, path.lstrip('/')))
    print(abs_path)
    if not abs_path.startswith(SERVER_PATH):
        client.sendall(Response.NOT_FOUND_RESPONSE)
        return
    
    try:
        with open(abs_path, 'rb') as f:
            file_stat = os.fstat(f.fileno())
            content_type, encoding = mimetypes.guess_type(abs_path)

            if content_type is None:
                content_type = "application/octet-stream"
            
            if encoding is not None:
                content_type += f"; charset = {encoding}"
            
            response_header = Response.FILE_RESPONSE_TEMPLATE.format(
                content_type = content_type,
                content_length = file_stat.st_size
            ).encode('ascii')

            await loop.sock_sendall(client, response_header)
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break

                await loop.sock_sendall(client, chunk)
    except FileNotFoundError:
        await loop.sock_sendall(Response.NOT_FOUND_RESPONSE)


class Request(typing.NamedTuple):

    method: str
    path: str
    headers: str
    
    @classmethod
    async def from_socket(cls,loop: asyncio.AbstractEventLoop,client: socket.socket):
        """
        Read and parse the objects from the request.
        Raise ValueError if the request cannot be parser
        """

        iter = iter_lines(loop,client)
        
        try:
            request_line = (await anext(iter)).decode('ascii')
        except StopAsyncIteration:
            raise ValueError("Request line missing")
        
        try:
            method, path, _ = request_line.split(" ")
        except ValueError:
            raise ValueError(f"Malformed request line: {request_line}")
        
        headers = {}

        async for line in iter:
            try:
                name , _, value = line.decode("ascii").partition(":")
                headers[name.lower()] = value.lstrip()
            except ValueError:
                raise ValueError(f"Malformed header line: {line}")
        
        return cls(method = method, path = path , headers = headers)
