from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source="user.username")
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = "__all__"
        model = Follow

    def validate(self, data):
        following = data.get("following")
        request = self.context.get("request")

        if (
            Follow.objects.filter(
                user=request.user,
                following=following,
            ).exists()
            or request.user == following
        ):
            raise serializers.ValidationError(
                (
                    "Вы не можете подписаться на себя или "
                    "вы уже подписаны на этого пользователя"
                )
            )

        return data
