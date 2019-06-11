import os
import pytest
import requests
import augur.server

def teardown_module(module):
    os.system('make dev-stop')

@pytest.fixture(scope="session")
def githubapi_routes():
    os.system('make dev-stop')
    os.system('make server &')

def test_issues_closed_route(githubapi_routes):
    response = requests.get('http://localhost:5000/api/unstable/rails/rails/timeseries/githubapi/issues/closed')
    assert response.status_code == 200

# def test_commits_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/timeseries/githubapi/commits')
#     assert response.status_code == 200

# def test_lines_changed_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/lines_changed')
#     assert response.status_code == 200

# def test_issues_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/timeseries/githubapi/issues')
#     assert response.status_code == 200

# def test_pull_request_closed_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/githubapi/pull_requests_closed')
#     assert response.status_code == 200

# def test_pull_requests_merged_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/githubapi/pull_requests_merged')
#     assert response.status_code == 200

# def test_pull_requests_open_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/githubapi/githubapi/pull_requests_open')
#     assert response.status_code == 200

# def test_repository_size_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/githubapi/repository_size')
#     assert response.status_code == 200

# def test_bus_factor_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/bus_factor')
#     assert response.status_code == 200

# def test_major_tags_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/timeseries/tags/major')
#     assert response.status_code == 200

# def test_tags_route(githubapi_routes):
#     response = requests.get('http://localhost:5000/api/unstable/rails/rails/timeseries/tags/tags')
#     assert response.status_code == 200
