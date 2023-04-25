import pytest
from api.pet import PostPet, DeletePet, UpdatePet, ReadPet
import re

from conftest import PetsDeleteID
from fixtures.pet_fixtures import pet_name_valid, pet_edit_status
import allure


class TestRead:
    @pytest.mark.fast
    def test_get_pet(self):
        resp = ReadPet().get_one_pet(pet_id=1)
        assert resp.status_code == 200


@pytest.mark.usefixtures("delete_created_pets")
class TestCreate:
    pets_for_delete = []

    @allure.story("Проверка валидных имен питомца")
    @pytest.mark.smoke
    @pytest.mark.parametrize("name", pet_name_valid)
    def test_create_pet(self, name):
        resp = PostPet().create_pet(name)
        self.pets_for_delete.append(resp.json()["id"])
        assert resp.status_code == 200
        assert (resp.json()["name"]) == "".join(
            re.split("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$", name)
        )

    @allure.story("Проверка добавления изображения питомцу")
    def test_add_img_to_pet(self):
        resp = PostPet().create_pet(name="Bubenchik")
        PetsDeleteID().pets_for_delete.append(resp.json()["id"])
        add_file_resp = PostPet().add_image_to_pet(
            pet_id=resp.json()["id"], file="img/test_img.png"
        )
        assert add_file_resp.status_code == 200
        assert "test_img.png" in add_file_resp.json()["message"]


class TestDelete:
    @allure.story("Проверка удаления питомца")
    def test_delete_pet(self):
        pet = PostPet().create_pet(name="Bubenchik")
        delete = DeletePet().delete_pet(pet.json()["id"])
        assert delete.status_code == 200


@pytest.mark.usefixtures("delete_created_pets")
class TestEdit:
    pets_for_delete = []

    @allure.story("Проверка обновления статуса питомца на валидный")
    @pytest.mark.parametrize("status", pet_edit_status)
    def test_edit_pet_status(self, status):
        pet = PostPet().create_pet(name="Bubenchik")
        self.pets_for_delete.append(pet.json()["id"])
        edit = UpdatePet().edit_status(id=pet.json()["id"], status=status)
        assert edit.json()["status"] == status
