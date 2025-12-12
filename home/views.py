from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwner

class NoteViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for Note - allows create, list, retrieve, update, destroy.
    Only authenticated users. Users only see their own notes.
    """
    serializer_class = NoteSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]  # Session kept for browsable API
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Ensure users only list/access their own notes
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Assign the logged in user as owner
        serializer.save(owner=self.request.user)
