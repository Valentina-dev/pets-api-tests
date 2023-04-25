from api_service import APIService


class PostPet(APIService):
    def create_pet(self, name):
        data = {
            "id": 0,
            "category": {"id": 0, "name": "string"},
            "name": name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        return self._request(method="post", route="/pet", body=data)

    def add_image_to_pet(self, pet_id, file):
        with open(file, "rb") as file:
            return self._request(
                method="post", route=f"/pet/{pet_id}/uploadImage", files={"file": file}
            )


class DeletePet(APIService):
    def delete_pet(self, pet_id):
        return self._request(method="delete", route=f"/pet/{pet_id}")


class UpdatePet(APIService):
    def edit_status(self, id: int, status):
        data = {
            "id": id,
            "category": {"id": 0, "name": "string"},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": status,
        }
        return self._request(method="put", route="/pet", body=data)


class ReadPet(APIService):
    def get_one_pet(self, pet_id):
        return self._request(method="get", route=f"/pet/{pet_id}")
