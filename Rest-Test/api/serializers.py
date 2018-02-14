from rest_framework import serializers

from talkMethods.models import Talk

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Talk
        fields = ('ID','Name','Speaker','Duration','Venue')