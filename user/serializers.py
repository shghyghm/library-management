from rest_framework import serializers
from .models import User

# class UserLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
#
#         def create(self, validated_data):
#             """
#             Create and return a new `Token` instance, given the validated data.
#             """
#             user = User.objects.get(
#                 # Q(username=validated_data.get('identity')) |
#                 Q(phone_number=validated_data.get("identity"), phone_number_confirmed=True)
#                 | Q(email=validated_data.get("identity")), is_finbeet=settings.IS_FINBEET
#             )
#             return get_jwt_tokens_for_user(user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def login_validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username:
            raise serializers.ValidationError("نام کاربری وارد نشده است")

        if not password:
            raise serializers.ValidationError("پسورد وارد نشده است")
            # check identity
        try:
            user = User.objects.get(
                username=username,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError("نام کاربری نامعتبر است")

        if not user.check_password(password):
            raise serializers.ValidationError("پسورد نامعتبر است")
        return user

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()