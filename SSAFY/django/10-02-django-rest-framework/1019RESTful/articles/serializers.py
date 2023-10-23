from rest_framework import serializers
from .models import Article, Comment, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class ArticleListSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'content', 'title', 'topics')



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # 조회 가능, 생성 x
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):

    # Comment 내용 포함시키기
    # 1. CommentSerializer 활용하기
    # comment_set = CommentSerializer(many=True, read_only=True)
    
    # 2. 각 필드를 재정의하기
    # 필드 명은 자유롭게 구성 가능
    # PrimaryKeyRelatedField: 참조하는 테이블의 PK
    # comment_id = serializers.PrimaryKeyRelatedField(source="comment_set", many=True, read_only=True)
    # comment_content = serializers.StringRelatedField(source="comment_set", many=True, read_only=True)

    # 3. SerializerMethodField
    comments = serializers.SerializerMethodField()
    #자동으로 get_comments 메소드 호출
    # obj: instance
    def get_comments(self, obj):
        comments = obj.comment_set.all()
        return [{
            "id": comment.id,
            "content": comment.content,
        } for comment in comments]
    class Meta:
        model = Article
        # all: 전체필드
        # -> 역참조 시 사용되는 필드명도 추가가 되어 있다. (comment_set)
        fields ='__all__'