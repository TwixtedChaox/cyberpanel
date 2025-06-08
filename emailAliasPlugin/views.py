from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mailServer.models import Forwardings


def alias_manager(request):
    return render(request, 'emailAliasPlugin/email_aliases.html')


@csrf_exempt
def fetch_aliases(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    data = [{'source': f.source, 'destination': f.destination} for f in Forwardings.objects.all()]
    return HttpResponse(json.dumps({'aliases': data}), content_type='application/json')


@csrf_exempt
def add_alias(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    payload = json.loads(request.body or '{}')
    src = payload.get('source', '').strip()
    dst = payload.get('destination', '').strip()
    if not src or not dst:
        return HttpResponse(json.dumps({'status': False, 'error': 'Invalid input'}),
                            content_type='application/json')
    if Forwardings.objects.filter(source=src, destination=dst).exists():
        return HttpResponse(json.dumps({'status': False, 'error': 'Alias already exists'}),
                            content_type='application/json')
    Forwardings.objects.create(source=src, destination=dst)
    return HttpResponse(json.dumps({'status': True, 'message': 'Alias created'}),
                        content_type='application/json')


@csrf_exempt
def delete_alias(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    payload = json.loads(request.body or '{}')
    src = payload.get('source', '').strip()
    dst = payload.get('destination', '').strip()
    Forwardings.objects.filter(source=src, destination=dst).delete()
    return HttpResponse(json.dumps({'status': True}), content_type='application/json')
