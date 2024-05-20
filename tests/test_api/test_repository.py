def test_search_repositories_with_keyword(github_api_worker):
    params = {"q": "aqa-python-2024"}

    response = github_api_worker.get_list_of_repos(params)
    assert response.status_code == 200

    json_response = response.json()
    assert "items" in json_response
    assert len(json_response["items"]) > 0
    assert len(json_response["items"]) == json_response["total_count"]
