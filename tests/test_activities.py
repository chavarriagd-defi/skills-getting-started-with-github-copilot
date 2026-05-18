def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_top_level_key = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_top_level_key in payload


def test_get_activities_entry_contains_required_fields(client):
    # Arrange
    activity_name = "Programming Class"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activity = response.json()[activity_name]

    # Assert
    assert response.status_code == 200
    assert required_fields.issubset(activity.keys())
    assert isinstance(activity["participants"], list)
