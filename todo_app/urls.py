from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet # 這裡只匯入 ViewSet

# 設定 API 的路由
router = DefaultRouter()
router.register(r'todos', TodoItemViewSet)

urlpatterns = [
    # 移除 path('', todo_list, ...)，改用 router 的自動化路由
    path('api/', include(router.urls)),
]