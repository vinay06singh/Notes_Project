from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(['POST'])
def create_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_note_by_id(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

@api_view(['GET'])
def query_notes_by_title(request):
    title_substring = request.GET.get('title', '')
    notes = Note.objects.filter(title__icontains=title_substring)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
