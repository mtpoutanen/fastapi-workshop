async def app(scope, receive, send):
    """
    Main ASGI application entry point
    :param scope: Contains information about the incoming request, such as the type of request, the headers, query parameters, etc.
    :param receive: An async generator that can be used to receive the message body from the client.
    :param send: An async function that can be used to send messages to the client.
    :return:
    """
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, World from pure Uvicorn app!',
    })
