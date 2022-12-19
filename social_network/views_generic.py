from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ModelGetPostView(APIView):
    model = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

