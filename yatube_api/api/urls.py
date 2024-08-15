from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()

router.register('groups', GroupViewSet, 'groups')
router.register('posts', PostViewSet, 'posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, 'comments')
router.register('follow', FollowViewSet, 'follows')


urlpatterns = [
    path('', include(router.urls)),
]
