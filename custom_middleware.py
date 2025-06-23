from fastapi import Request

async def add_real_ip_header(request: Request, call_next):
    if not request.headers.get('x-real-ip'):
        request.headers.__dict__['_list'].append(
            (b'x-real-ip', b'127.0.0.1')
        )
    return await call_next(request)
