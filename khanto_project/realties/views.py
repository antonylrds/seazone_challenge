from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Realties
from .serializers import RealtiesSerializer
from drf_yasg.utils import swagger_auto_schema

from .utils import get_now

class RealtiesListView(APIView):
    @swagger_auto_schema(responses={200: RealtiesSerializer(many=True)})
    def get(self, request):
        realties = Realties.objects.all()
        serializer = RealtiesSerializer(realties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = RealtiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
class RealtiesDetailsView(APIView):
    def get(self, request, realty_id):
        realty = Realties.objects.get(id=realty_id)
        if not realty:
            return Response({"res": "Realty not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RealtiesSerializer(realty)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, realty_id):
        realty = Realties.objects.get(id=realty_id)
        if not realty:
            return Response(
                {"res": "Realty not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        request_data = request.data
        if realty.active != request_data.get("active"):
            new_data = {
                "active": request_data.get("active", realty.active),
                #updates activation date only if it was inactive
                'activated_at': get_now() if not realty.active else realty.activated_at
            }
            
            serializer = RealtiesSerializer(instance=realty, data=new_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"res": "Nothing to change."}, status=status.HTTP_200_OK)
    
    def delete(self, request, realty_id):
        realty = Realties.objects.get(id=realty_id)
        if not realty:
            return Response({"res": "Realty not found."}, status=status.HTTP_404_NOT_FOUND)
        realty.delete()
        return Response({"res": "Realty deleted."}, status=status.HTTP_200_OK)