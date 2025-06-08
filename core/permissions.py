from rest_framework import permissions  # Importa o módulo de permissões do Django REST Framework

# Define uma permissão personalizada que verifica se o usuário é dono do veículo ou do registro (objeto)
class IsOwnerOfVehicleOrRecord(permissions.BasePermission):
    # Método que checa a permissão para um objeto específico (obj)
    def has_object_permission(self, request, view, obj):
        user = request.user  # Usuário que está fazendo a requisição

        # Verifica se o objeto possui o atributo 'owner'
        if hasattr(obj, 'owner'):
            # Retorna True se o owner do objeto existir e seu usuário for o usuário da requisição
            return obj.owner and obj.owner.user == user

        # Caso o objeto não tenha 'owner', verifica se tem um atributo 'vehicle' que possui um 'owner'
        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            # Retorna True se o dono do veículo existir e seu usuário for o usuário da requisição
            return obj.vehicle.owner and obj.vehicle.owner.user == user

        # Caso nenhuma das condições acima seja satisfeita, retorna False (sem permissão)
        return False
