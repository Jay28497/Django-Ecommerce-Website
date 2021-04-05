from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        # print(request.session.get('customer_id'))
        returnUrl = request.META['PATH_INFO']
        # print(returnUrl)
        if not request.session.get('customer_id'):
            return redirect(f'login?return_url={returnUrl}')

        response = get_response(request)
        return response

    return middleware
