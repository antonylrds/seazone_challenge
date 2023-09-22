from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ads
from .serializers import AdsSerializers

class AdsListView(APIView):
    def get(self, request):
        ads_instance = Ads.objects.all()
        serializer = AdsSerializers(ads_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AdsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdsDetailView(APIView):
    def get(self, request, ad_id):
        ad_instance = Ads.objects.get(id=ad_id)
        if not ad_instance:
            return Response({"res": "Ad not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdsSerializers(ad_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, ad_id):
        ad_instance = Ads.objects.get(id=ad_id)
        if not ad_instance:
            return Response(
                {"res": "Ad not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        request_data = request.data
        new_data = {
            "platform_origin": request_data.get("platform_origin", ad_instance.platform_origin),
            "platform_fee": request_data.get('platform_fee', ad_instance.platform_fee)
        }
        
        serializer = AdsSerializers(instance=ad_instance, data=new_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
