from django.utils.timezone import now

class UserVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            visit_history = request.session.get('visit_history', [])
            current_page = request.path
            visit_history.append({
                'page': current_page,
                'timestamp': now().strftime('%Y-%m-%d %H:%M:%S')
            })
            request.session['visit_history'] = visit_history[-8:]  # Keep only the last 10 visits
        return self.get_response(request)