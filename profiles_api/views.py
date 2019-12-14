from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
   """Test API View"""
   serializer_class=serializers.HelloSerializer

   def get(self,request,format=None):
       """Returns random text and message"""

       msg=[
       'Hello',
       'World',
       'i am Abel',
       ]

       return Response({'message':'Hello','an_apiview':msg})

   def post(self,request):

        """Create a new hello message"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

   def put(self,request,pk=None):
       return Response({'message':'PUT'})

   def patch(self,request,pk=None):
       return Response({'message':'Patch'})

   def delete(self,request,pk=None):
       return Response({'message':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test the ViewSet"""
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """Returns a hello message"""
        msg=['Hello World!!!!']
        return Response({'message':msg})

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        """Handles getting an object by its id """
        return Response({'http_method':'get'})

    def update(self,request,pk=None):
        """Updates the object by its id"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Updates the object partially by its id"""
        return Response({'http_method':'Patch'})

    def destroy(self,request,pk=None):
        """Deletes an object"""
        return Response({'http_method':'DELETE'})
