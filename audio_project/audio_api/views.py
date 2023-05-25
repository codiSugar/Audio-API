from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AudioElement
from .serializers import AudioElementSerializer

@api_view(['GET'])
def get_audio_elements(request, project_id):
    audio_elements = AudioElement.objects.filter(project_id=project_id)
    serializer = AudioElementSerializer(audio_elements, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_audio_element(request):
    serializer = AudioElementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_audio_element(request, audio_element_id):
    try:
        audio_element = AudioElement.objects.get(pk=audio_element_id)
    except AudioElement.DoesNotExist:
        return Response(status=404)

    serializer = AudioElementSerializer(audio_element, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_audio_element(request, audio_element_id):
    try:
        audio_element = AudioElement.objects.get(pk=audio_element_id)
    except AudioElement.DoesNotExist:
        return Response(status=404)

    audio_element.delete()
    return Response(status=204)
