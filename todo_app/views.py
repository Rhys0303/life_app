# 範例檢查
from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet): # <--- 確保名稱一模一樣
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer