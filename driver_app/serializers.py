from rest_framework import serializers

from driver_app.models import Answer, Question, Training, Advice, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    advice_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='advices')


class AdviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advice
        fields = '__all__'

    tags = serializers.HyperlinkedRelatedField(allow_empty=True, many=True, queryset=Tag.objects.all(),
                                               view_name='tag-detail')


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

    advice_set = serializers.HyperlinkedRelatedField(many=True, queryset=Advice.objects.all(),
                                                     view_name='advice-detail')
    question = serializers.HyperlinkedRelatedField(allow_empty=True, many=True, queryset=Question.objects.all(),
                                                   view_name='question-detail')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    answers = AnswerSerializer(many=True)
