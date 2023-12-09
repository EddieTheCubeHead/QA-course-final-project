import os

import pytest

from conftest import FETCHABLE_TYPES
from utils.api_client import TypedPokeApiClient
from utils.link_walker import LinkWalker


# noinspection PyMethodMayBeStatic
@pytest.mark.parametrize("typed_client", FETCHABLE_TYPES, indirect=True)
class ObjectFetchingFeatures:

    def should_get_list_of_available_resources_if_no_identifier_given(self, typed_client: TypedPokeApiClient):
        results = typed_client.get_all()
        assert results is not None, f"Could not get a list of resources for route {typed_client.route_name}"

    def should_get_ability_data_in_the_correct_model(self, typed_client: TypedPokeApiClient):
        resource_id = typed_client.get_random_id()
        typed_client.get_typed(resource_id)

    def should_return_same_data_for_name_and_number_fetch(self, typed_client: TypedPokeApiClient):
        object_from_id = typed_client.get_typed(typed_client.get_random_name())
        object_from_name = typed_client.get_typed(object_from_id.name)
        assert object_from_name == object_from_id

    @pytest.mark.skipif(os.getenv("SKIP_LONG", default=None) is not None, reason="Skipped long test")
    def should_have_functioning_links_to_other_resources(self, typed_client: TypedPokeApiClient,
                                                         link_walker: LinkWalker):
        fetchable_object = typed_client.get_typed(typed_client.get_random_name())
        link_walker.assert_links_exist(fetchable_object.model_dump())
