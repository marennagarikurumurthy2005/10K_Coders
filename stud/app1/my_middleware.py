

class MyMiddleware:
    def __init__(self,get_request):
        self.get_request=get_request

    def __call__(self,request):
        res = self.get_request(request)
        return res
    