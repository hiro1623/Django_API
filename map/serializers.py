from rest_framework import serializers
from .models import PostData,Account

class PostDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostData
        fields = (
            'purpose',
            'message',
            'lat',
            'lng',
            'pic',
            #'post_time',
            #'last_modify',
            'user',
            #'post_flag',
        )
        

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)