from rest_framework.response import Response
from rest_framework.views import APIView
from apps.api.user.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)