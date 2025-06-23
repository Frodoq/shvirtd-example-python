from fastapi import Request

async def add_real_ip_header(request: Request, call_next):
    real_ip = (
        request.headers.get('X-Forwarded-For', '').split(',')[0].strip() or
        request.headers.get('X-Real-IP') or
        str(request.client.host)
    
    request.headers.__dict__['_list'] = [
        (k, v) for k, v in request.headers.items() if k.lower() != 'x-real-ip'
    ] + [('x-real-ip', real_ip.encode())]
    
    return await call_next(request)
