from rest_framework import serializers

from .models import Repository, Directory

class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Directory
        fields = ('name', 'url', 'last_commit', 'parent_dir', 'total_doc_info', 'sub_dirs', 'sub_files',)
        depth = 1


class PrimeDirectorySerializer(serializers.ModelSerializer):
    sub_dirs = DirectorySerializer(many=True)

    class Meta:
        model = Directory
        fields = ('name', 'url', 'last_commit', 'parent_dir', 'total_doc_info', 'sub_dirs', 'sub_files',)
        depth = 1


class RepositorySerializer(serializers.ModelSerializer):
    root = PrimeDirectorySerializer()

    class Meta:
        model = Repository
        fields = ('name', 'url', 'last_commit', 'root', 'document_stats',)


