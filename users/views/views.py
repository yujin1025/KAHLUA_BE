from functools import partial
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from users.mixins import ApiAuthMixin, ApiAllowAnyMixin
from users.models import User
from users.serializers import UserSerializer


#serializer에 partial=True를 주기위한 Mixin
class SetPartialMixin:
    def get_serializer_class(self, *args, **kwargs):
        serializer_class = super().get_serializer_class(*args, **kwargs)
        return partial(serializer_class, partial=True)


class SignUpView(SetPartialMixin, CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = [
        AllowAny,
    ]

    @swagger_auto_schema(
        operation_id='api_users_signup_post',
        operation_description='''
            전달된 필드값을 기반으로 회원가입을 진행합니다.
        ''',
        responses={
            "200": openapi.Response(
                description="OK",
                examples={
                    "application/json": {
                        "status": "success",
                        "data": {"id": 1}
                    }
                }
            ),
            "400": openapi.Response(
                description="Bad Request",
            ),
        },
    )
    def post(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({
            'status': 'Success',
        }, status=status.HTTP_200_OK)