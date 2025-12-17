from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, FeaturedMenuItemListView, MenuCategoryListView
from django.urls import path, include

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('menu-categories/', MenuCategoryListView.as_view(),name='menu-categories'),
    path('features-menu-items/', FeaturedMenuItemListView.as_view(), name='featured-menu-items'),
]
