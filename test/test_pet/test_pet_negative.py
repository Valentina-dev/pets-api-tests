import pytest

from api.pet import PostPet, DeletePet, UpdatePet
from fixtures.pet_fixtures import pet_name_invalid, pet_edit_status_invalid
import allure


@pytest.mark.usefixtures("delete_created_pets")
class TestCreate:
    pets_for_delete = []

    @allure.story("Invalid pet nicknames check")
    @pytest.mark.xfail
    @pytest.mark.parametrize("invalid_name", pet_name_invalid)
    def test_create_invalid_name(self, invalid_name):
        resp = PostPet().create_pet(invalid_name)
        assert resp.status_code == 500


class TestDelete:
    @allure.story("Check for delete already deleted pet")
    def test_delete_already_deleted_pet(self):
        pet = PostPet().create_pet(name="Bubenchik")
        DeletePet().delete_pet(pet.json()["id"])
        second_time_delete = DeletePet().delete_pet(pet.json()["id"])
        assert second_time_delete.status_code == 404


@pytest.mark.usefixtures("delete_created_pets")
class TestEdit:
    pets_for_delete = []

    @allure.story("Update pet nickname's invalid status checking")
    @pytest.mark.xfail
    @pytest.mark.parametrize("status", pet_edit_status_invalid)
    def test_edit_pet_status(self, status):
        pet = PostPet().create_pet(name="Bubenchik")
        self.pets_for_delete.append(pet.json()["id"])
        edit = UpdatePet().edit_status(id=pet.json()["id"], status=status)
        assert edit.status_code == 500
