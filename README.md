# AsyncLiteServer

**AsyncLiteServer** is a lightweight, asynchronous HTTP server built from scratch in Python. It can handle multiple connections simultaneously and serves an `index.html` file as its default page. This project is a great starting point for understanding how HTTP servers work at a low level using Python's asyncio and socket libraries.

## Features

- **Asynchronous Connection Handling**: Utilizes Python's `asyncio` to manage multiple client connections concurrently.
- **Simple Request Parsing**: Parses incoming HTTP requests and extracts method, path, and headers.
- **Static File Serving**: Serves an `index.html` file as the default response for incoming HTTP requests.
- **Customizable**: Easy to extend with additional request handling and response generation features.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Basic understanding of HTTP protocols and Python's asyncio library

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AsyncLiteServer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AsyncLiteServer
   ```
3. Ensure your environment is set up correctly with Python 3.8+.

### Usage

1. Start the server by running the following command:
   ```bash
   python main.py
   ```
2. The server will start listening on \`localhost:3030\`. Open your browser and navigate to:
   ```bash
   http://localhost:3030
   ```
3. You should see the content of the \`index.html\` file displayed in your browser.

## Project Structure

```bash
AsyncLiteServer/
├── request_handler.py       # Handles the parsing of incoming HTTP requests
├── response.py              # Contains predefined HTTP responses
├── server.py                # Main server code that handles connections and serves files
└── index.html               # The default HTML file served by the server
```


## Customization

- **Serving Different Files**: Modify the \`Response\` class in \`response.py\` to serve different types of files or add routing logic to handle various paths.
- **Request Processing**: Extend the \`Request\` class in \`request_handler.py\` to support more complex request handling, such as POST data or query parameters.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Special thanks to the Python community for their excellent documentation and support. This project also leverages concepts from various sources on HTTP server development and asynchronous programming.

---

Enjoy building and learning with **AsyncLiteServer**!