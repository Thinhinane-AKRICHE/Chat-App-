from django.contrib.auth.models import User
#User est un modèle (classe), qui représente la structure d'un utilisateur dans la base de données. 
from rest_framework import serializers

#Les "serializers" dans le contexte de Django REST Framework (et d'autres frameworks similaires) sont des composants qui facilitent la conversion des données entre différents formats, notamment entre des objets Python (comme des instances de modèles) et des formats de données interchangeables comme JSON ou XML.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "passeword"]
        extra_kwargs={"passeword": {"write_only": True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # user, est une Instance de modèle (objet créé à partir de la classe User)
        return user