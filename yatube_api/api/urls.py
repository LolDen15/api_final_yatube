from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewset


router_ver1 = SimpleRouter()
router_ver1.register(r'groups', GroupViewSet, 'groups')
router_ver1.register(r'posts', PostViewSet, 'posts')
router_ver1.register('follow', FollowViewset, 'follows')
router_ver1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('v1/', include(router_ver1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
