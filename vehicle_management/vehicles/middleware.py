from django.http import HttpResponseForbidden


class IPFilterMiddleware:
    """
    Simple IP filtering using custom middleware.
    """

    ALLOWED_IPS = [
        '127.0.0.1',
        '::1',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.headers.get("X-Forwarded-For", request.META.get('REMOTE_ADDR'))
        if ip not in self.ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: Your IP is not allowed.")
        return self.get_response(request)
