import os

import googlemaps
import pytest

from .distance_test_data import TEST_DATA

API_KEY = os.environ.get('GOOGLE_API_KEY')


@pytest.fixture(scope="module")
def google_maps_api_client():
    return googlemaps.Client(API_KEY)


@pytest.mark.parametrize("test_coordinates,expected_distance", TEST_DATA)
def test_distance_by_coordinates(google_maps_api_client, test_coordinates, expected_distance):
    matrix_data = google_maps_api_client.distance_matrix(*test_coordinates)
    distance = matrix_data['rows'][0]['elements'][0]['distance']['value']
    assert distance == expected_distance
