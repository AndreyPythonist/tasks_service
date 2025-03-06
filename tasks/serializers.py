from rest_framework import serializers


from tasks.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'is_completed']


    title = serializers.CharField(max_length=100, required=True)
    is_completed = serializers.BooleanField(default=False)
