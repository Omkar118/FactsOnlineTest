import sys
from django.http import JsonResponse
import subprocess

def language_version(request):
    language = request.GET.get('language')
    # version = str(subprocess.check_output('{} -V'.format(language),shell=True))
    version= sys.version

    response = {
        'language': language,
        'version': version
    }

    return JsonResponse(response)
