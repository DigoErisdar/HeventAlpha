from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import User, Profile, Private
from helper.serializers import DynamicSerializerMixin


class PrivateSerializer(serializers.ModelSerializer):
    display_view = serializers.SerializerMethodField('get_value_display')

    class Meta:
        model = Private
        exclude = ('user',)

    def get_value_display(self, obj):
        return obj.get_value_display()


class ProfileSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    profile = serializers.SerializerMethodField('private_profile')

    class Meta:
        model = User
        exclude = ('password', 'last_login', 'email',)

    def private_profile(self, obj):
        fields = self.context.get('fields', {})
        allowed_fields = ['id', 'avatar', 'avatar_cropping', 'wallpaper', 'wallpaper_cropping']
        for field, users in fields.items():
            if obj.id in users:
                allowed_fields.append(field)
        serializer = ProfileSerializer(obj.profile, fields=allowed_fields)
        return serializer.data


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email', 'username',)

    def create(self, validated_data):
        user = super(UserRegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'sex', 'date_birthday',)


class UserUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUserUpdateSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'profile',)

    def update(self, instance, validated_data):
        profile = dict(validated_data.pop('profile', {}))
        print(profile)
        Profile.objects.update_or_create(user=instance, defaults=profile)
        return super(UserUpdateSerializer, self).update(instance, validated_data)


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password',)

    def validate(self, attrs):
        if not self.instance.check_password(attrs.get('old_password')):
            raise ValidationError({'old_password': "Старый пароль не верный"}, code='invalid')
        return attrs

    def update(self, instance, validated_data):
        password = validated_data.get('new_password')
        self.instance.set_password(password)
        return super(UserUpdatePasswordSerializer, self).update(instance, validated_data)
