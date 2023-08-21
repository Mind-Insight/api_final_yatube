from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
)
from django.urls import include, path
from rest_framework import routers

router_v1 = routers.DefaultRouter()
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
router_v1.register("posts", PostViewSet, basename="post")
router_v1.register("groups", GroupViewSet, basename="group")
router_v1.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/auth/", include("djoser.urls")),
    path("v1/auth/", include("djoser.urls.jwt")),
]
