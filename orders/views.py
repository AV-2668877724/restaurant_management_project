from rest_framework.view import APIView
from rest_framework.response import response
from rest_framework import status
from django.utils import timezone

from rest_framework.generics import ListAPIView
from rest_framework,permissions import IsAuthenticated
from rest_framework.authentication import tokenAuthentication, SessionAuthentication

from .models import Coupon, Order
from .serializers import OrderSerializer


class CouponValidationView(APIView):
    def post(self,request):
        code = request.data.get('code')

        if not code:
            return Response(
                {"error": "Coupon code is rewuired"},
                status= status.HTTP_400_BAD_REQUEST
            )

            today=timezone.now().date()

            try:
                coupon = Coupon.objects.get(
                    code=code,
                    is_active=True,
                    valid_from_lte=today,
                    valid_until_gte=today
                )
            except Coupon.DoesNotExist:
                return Response(
                    {"error": "Invalid or expired coupon"},
                    status= status.HTTP_400_BAD_REQUEST

                )


            return Response(
                {
                    "success":True,
                    "discount_percentage": coupon.discount_percentage
                },
                status=status.HTTP_200_OK
            )

class OrderHistoryView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes =[IsAuthenticated]
    authentication_classes =[tokenAuthentication, SessionAuthentication]

    def get_queryset(slef):
        return Order.objects.filter(user=self.request.user)
            


