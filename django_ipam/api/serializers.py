import swapper
from openwisp_utils.api.serializers import ValidatedModelSerializer
from rest_framework import serializers

IpAddress = swapper.load_model('django_ipam', 'IpAddress')
Subnet = swapper.load_model('django_ipam', 'Subnet')


class IpRequestSerializer(ValidatedModelSerializer):
    class Meta:
        model = IpAddress
        fields = ('subnet', 'description')
        read_only_fields = ('created', 'modified')


class IpAddressSerializer(ValidatedModelSerializer):
    class Meta:
        model = IpAddress
        fields = '__all__'
        read_only_fields = ('created', 'modified')


class SubnetSerializer(ValidatedModelSerializer):
    class Meta:
        model = Subnet
        fields = '__all__'
        read_only_fields = ('created', 'modified')


class ImportSubnetSerializer(serializers.Serializer):
    csvfile = serializers.FileField()


class HostsResponseSerializer(serializers.Serializer):
    address = serializers.CharField()
    used = serializers.BooleanField()
