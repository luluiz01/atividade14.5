from django.http import JsonResponse

def usuarios(request):
    if request.method == 'GET':
        usuario = {'id': 1, 'nome': 'Luiz'}
        return JsonResponse(usuario)

# Create your views here.
