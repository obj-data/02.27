# -*- codeing = utf -*-
# @Time : 2022/3/8 14:54
# @Author : 陈迪曙
# @File : authJWT.py
# @software : PyCharm
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication, get_authorization_header, \
    jwt_decode_handler


class AuthToken(BaseJSONWebTokenAuthentication):
    def authenticate(self, request):
        # 返回请求头的Authorization字段，str格式
        jwt_value = str(get_authorization_header(request), encoding='utf-8')
        if not jwt_value:
            # 没有Authorization字段则提示
            raise AuthenticationFailed("Authorization  字段是必须的")
        try:
            # 验证token
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            # 捕捉 错误类型返回提示
            raise AuthenticationFailed('签名过期')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('非法用户')
        user = self.authenticate_credentials(payload)
        # 返回 user实例和 token
        return user, jwt_value
