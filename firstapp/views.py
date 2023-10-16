from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from firstapp.models import Contact
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


# Create your views here.
#function based
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def firstAPI(request):
    if request.method=="POST":
        id=request.data['id']
        name=request.data['name']
        messenger=request.data['messenger']
        #sender=request.data['sender']
        print(id,name,messenger)
        return Response({"id":id,"name":name,"messenger":messenger})
    context={
        'name':"shuvo",
        'department':"engineering"
    }
    return Response()

from .serializers import *
#@api_view(['POST',])
#class based
class ContactAPIView(APIView):
    permission_classes=[AllowAny,]
    def post(self,request,format=None):
  
        serializer= ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def get(self,request,format=None):
         
         queryset= Contact.objects.all()
         serializer = ContactSerializer(queryset,many=True)

         return Response(serializer.data)

from rest_framework.generics import CreateAPIView
from .models import BlogPost

class PostCreateAPIView(CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=BlogPost.objects.all()
    serializer_class=PostSerializer
    