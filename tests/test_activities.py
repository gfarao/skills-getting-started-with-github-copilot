def test_get_activities_returns_activity_map(client):
    # Arrange

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "Chess Club" in body


def test_get_activities_returns_expected_structure(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    for activity_details in body.values():
        assert required_keys.issubset(activity_details.keys())
        assert isinstance(activity_details["participants"], list)
