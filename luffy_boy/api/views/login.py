from django.contrib import auth
from api.models import Token, UserInfo
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from api.utils.serializer import UserInfoSerializer
from rest_framework.viewsets import generics
from rest_framework.views import APIView
import binascii
import os
import hashlib
from api.utils.response import BaseResponse
from api.utils.captcha_verify import verify


# 注册
class RegView(APIView):
    def post(self, request):
        response = BaseResponse()
        # 获取用户名和密码
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        re_password = request.data.get('re_password')
        hl = hashlib.md5()
        hl.update(username.encode(encoding='utf-8'))
        request.data['uid']= hl.hexdigest()
        print(request.data)

        if re_password!=password:
            response.msg = "2次密码不一致"
            response.code = 1002
            return Response(response.dict)

        # 拿序列化器做验证
        ser_obj = UserInfoSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(response.dict)
        else:
            response.msg="注册失败"
            response.code = 1003
            response.data = ser_obj.errors
            print(ser_obj.errors)
        return Response(response.dict)


class LoginView(APIView):
    def generate_key(self):
        # 生成随机字符
        return binascii.hexlify(os.urandom(20)).decode()

    def post(self, request):
        response = BaseResponse()

        receive = request.data
        if request.method == 'POST':
            print(receive)
            # 检验验证码
            is_valid = verify(receive)
            print("is_valid", is_valid)
            if is_valid:

                username = receive.get("username")
                password = receive.get("password")
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    # update the token
                    key = self.generate_key()
                    from django.utils.timezone import utc
                    import datetime
                    now = datetime.datetime.now()
                    Token.objects.update_or_create(user=user, defaults={"key": key, "created": now})
                    user_info = UserInfo.objects.get(pk=user.pk)
                    serializer = UserInfoSerializer(user_info)
                    data = serializer.data

                    response.msg = "验证成功!"
                    response.userinfo = data
                    response.token = key

                else:
                    try:
                        UserInfo.objects.get(username=username)
                        response.msg = "密码错误!"
                        response.code = 1002
                    except UserInfo.DoesNotExist:
                        response.msg = "用户不存在!"
                        response.code = 1003
            else:

                response.code = 1001
                response.msg = "请完成滑动验证!"

            return Response(response.dict)
