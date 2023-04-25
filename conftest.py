import pytest
from api.pet import DeletePet


class PetsDeleteID:
    pets_for_delete = []


@pytest.fixture(scope="class")
def delete_created_pets(request):
    yield
    for pet in set(request.cls.pets_for_delete):
        DeletePet().delete_pet(pet)
