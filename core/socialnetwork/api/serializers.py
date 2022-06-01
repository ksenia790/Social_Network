from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from socialnetwork.models import Post, Comment


# Comment Serializers
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentChildSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
        'id',
        'body',
        'created',
        'parent',
        'replies',
        ]
    def get_replies(self, obj):
        if obj.children:
            return CommentChildSerializer(obj.children(), many=True).data
        return None


class CommentDetailSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    replies = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'name',
            'body',
            'replies',
            'reply_count',
            ]
    
    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()


class CommentListSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
        'id',
        'post',
        'name',
        'body',
        'email',
        'parent',
        'reply_count',
        'replies',
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()


# Post Serializers
class PostCreateSerializer(ModelSerializer):
    """
        Displays next fields for creating post. 
    """
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    """
        Displays info(fields) about some particular post. 
    """
    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(ModelSerializer):
    """
        Displays info(fields) about all posts. 
    """
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
            'likes',
            'dislikes'
        ]