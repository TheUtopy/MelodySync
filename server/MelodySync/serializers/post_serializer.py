from rest_framework.serializers import ModelSerializer, ValidationError

from MelodySync.models.post_model import Post

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'message',
        )
