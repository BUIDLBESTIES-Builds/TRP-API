from rest_framework import serializers
from api.models import User
from rest_framework import status
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password

from api.models import User, Reimbursement


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = User
       fields = ('fullname', 'category','amounts', 'description', 'status','id')


class ReimbursementSerializer(serializers.ModelSerializer):
   class Meta:
       model = Reimbursement
       fields = ('user', 'wallets', 'crypto', 'upload', 'status')



class ReimbursementDetailSerializer(serializers.HyperlinkedModelSerializer):
    user_fullname =  serializers.ReadOnlyField(source='user.fullname')
    amount = serializers.ReadOnlyField(source='user.amounts')
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, object):
        items = self.instance.values_list('user__amounts', flat=True)
        newlist = [float(i) for i in items]
        return {
           str(sum(newlist))
        }
       
    class Meta:
        model = Reimbursement
        fields = ['user','status', 'crypto', 'user_fullname','amount','total_amount']
        lookup_field= 'user_fullname'
        extra_kwargs ={
            'url': {'view_name': 'reimbursement', 'lookup_field': 'user_fullname'},
        }



# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ["id", "username"]

# class RegisterSerializer(serializers.ModelSerializer):
# #     email = serializers.EmailField(
# #     required=True,
# #     validators=[UniqueValidator(queryset=User.objects.all())]
# # )
# #     password = serializers.CharField(
# #     write_only=True, required=True, validators=[validate_password])
# #     password2 = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = User
#         fields = '__all__'
#         # extra_kwargs = {
#         # 'first_name': {'required': True},
#         # 'last_name': {'required': True}
#         # }
#     # def validate(self, attrs):
#     #     if attrs['password'] != attrs['password2']:
#     #         raise serializers.ValidationError(
#     #             {"password": "Password fields didn't match."})
#     #         return attrs
#     def create(self, validated_data):
#         user = User.objects.create(
#         username=validated_data['username'],
#         # email=validated_data['email'],
#         # first_name=validated_data['first_name'],
#         # last_name=validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user