from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    """
    An abstract base serializer for models using UUIDs for primary keys and timestamp fields.

    This serializer adds common fields and configurations for other serializers that inherit from it.

    Fields:
    - `id` (UUID): The unique identifier for the instance, represented as a UUID. This field is read-only.
    - `created` (DateTime): The timestamp indicating when the instance was created. This field is read-only.
    - `updated` (DateTime): The timestamp indicating when the instance was last updated. This field is read-only.
    """

    id = serializers.UUIDField(
        source='public_id',
        read_only=True,
        format='hex'
    )
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
