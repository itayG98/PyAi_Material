import uvicorn
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
SERVER_PORT = 5000

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=SERVER_PORT,
        reload=True,
    )
