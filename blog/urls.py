from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from blog.views import PostViewSet, CommentViewSet, CategoryViewSet, TagViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register("post", PostViewSet)
router.register("comnt", CommentViewSet)
router.register("cate", CategoryViewSet)
router.register("tag", TagViewSet)
router.register("like", LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
