from rest_framework.view import APIView
from rest_framework.response import response
from rest_framework import status
from django.utils import timezone

from .models import Coupon


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

                
            


