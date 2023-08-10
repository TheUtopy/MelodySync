from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from MelodySync.serializers.PostSerializer import PostSerializer
from MelodySync.models.PostModel import Post
from MelodySync.models.UserModel import User


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, **kwargs):
        serializer = PostSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)

            # Retrieve the session ID from the request's session cookie
            session_id = request.COOKIES.get('sessionid')

            # Fetch the session object using the session ID
            session = Session.objects.get(session_key=session_id)

            # Get the user_id from the session's decoded data
            user_id = session.get_decoded().get('_auth_user_id')

            # Fetch the user object using the user_id
            user = User.objects.get(id=user_id)

            # Update the serializer with the user_id
            serializer.validated_data['user_id'] = user_id

            serializer.save()
            return Response({'post': "created"}, status=status.HTTP_201_CREATED)

        except:
            return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)
