from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
   """Test API View"""

   def get(self,request,format=None):
       """Returns random text and message"""

       msg=[
       'Hello',
       'World',
       'i am Abel',
       ]

       return Response({'message':'Hello','an_apiview':msg})
