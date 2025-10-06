from django.http import JsonResponse, HttpResponse

def home(request):
    return HttpResponse("""
        <h1>🎉 Azure Web App Deployment Successful!</h1>
        <p>Your Django app is running smoothly on Azure.</p>
        <p>Visit <a href='/health/'>/health</a> to check the app status.</p>
    """)

def health(request):
    return JsonResponse({"status": "OK", "app": "Azure Django Test App"})
