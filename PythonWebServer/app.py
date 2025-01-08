import uvicorn

async def app(scope, receive, send):
    assert scope['type'] == 'http' # Only HTTP connections are supported
    await send({ # Send the response headers
        'type': 'http.response.start', # Indicate that the response headers are being sent
        'status': 200, # HTTP status code
        'headers': [ # Response headers
            [b'content-type', b'text-plain'], # Content-Type: text/plain
        ],
    })
    await send({ # Send the response body
        'type': 'http.response.body', # Indicate that the response body is being sent
        'body': b'Hello, world! Ihan', # Response body
    })
    
def userName(firstname:str, lastname:str):
    return firstname

print(userName("matti", "meikäläinen"))   