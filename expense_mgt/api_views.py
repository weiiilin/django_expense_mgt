from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .models import ExpenseRecord
from .serializers import ExpenseRecordSerializer


class ExpenseRecordListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpenseRecordSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ExpenseRecord.objects.filter(user=self.request.user).order_by('-date', '-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseRecordDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseRecordSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ExpenseRecord.objects.filter(user=self.request.user)