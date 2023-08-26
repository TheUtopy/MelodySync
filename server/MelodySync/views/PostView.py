from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError

from MelodySync.serializers.PostSerializer import PostSerializer
from MelodySync.models.PostModel import Post
from MelodySync.models.UserModel import User


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, **kwargs):
        serializer = PostSerializer(data=request.data)
        if 'sessionid' not in request.COOKIES:
            return Response({"error": "Missing session cookie"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.is_valid(raise_exception=True)

            # Retrieve the session ID from the request's session cookie
            session_id = request.COOKIES.get('sessionid')

            # Fetch the session object using the session ID
            session = Session.objects.get(session_key=session_id)

            # Get the user_id from the session's decoded data
            user_id = session.get_decoded().get('_auth_user_id')
            # user_id = 6
            # Fetch the user object using the user_id
            user = User.objects.get(id=user_id)

            # Update the serializer with the user_id
            serializer.validated_data['user_id'] = user

            serializer.save()
            return Response({'post': "created"}, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            if 'message' in e.detail:
                error_message = e.detail['message'][0]
                return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
