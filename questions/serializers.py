from rest_framework import serializers

from questions.models import Question, Answer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    answers = serializers.HyperlinkedRelatedField(many=True,
                                                                                  read_only=True,
                                                                                  view_name='answer-detail')

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'author', 'timestamp', 'answers',
                        'total_votes',)


class AnswerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'url', 'title', 'votes',)
