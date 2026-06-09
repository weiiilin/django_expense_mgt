from rest_framework import serializers

from .models import ExpenseRecord


class ExpenseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseRecord
        fields = ['id', 'date', 'category', 'amount', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError('金額必須大於 0。')
        return value