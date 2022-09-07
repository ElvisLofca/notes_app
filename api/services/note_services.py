from rest_framework.response import Response
from api.models import Note
from api.serializers import NoteSerializer
from rest_framework import status


def get_notes_list(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


def get_note_detail(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)


def create_note(request):
    data = request.data
    serializer = NoteSerializer(data=data)
    if serializer.is_valid():
        note = Note.objects.create(
            body=data['body']
        )
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    else:
        return Response({"message": "A body must be provided"}, status=status.HTTP_400_BAD_REQUEST)

def update_note(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


def delete_note(request, pk):
    print('deleting')
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')