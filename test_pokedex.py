import pytest
from pokedex import fetch_pokemon

# UNIT TESTING THE POKEDEX SEARCH ENGINE

def describe_fetch_pokemon():
    """Tests for fetch_pokemon function."""

    def test_valid_pokemon():
        """It should return data for a valid Pokemon name."""
        data = fetch_pokemon("pikachu")
        assert data is not None
        assert data["name"] == "pikachu"

    def test_valid_pokemon_by_id():
        """It should return data when searching by a valid Pokémon ID."""
        data = fetch_pokemon(25)  # Pikachu's ID
        assert data is not None
        assert data["name"] == "pikachu"

    def test_invalid_pokemon():
        """It should return None for an invalid Pokemon."""
        data = fetch_pokemon("invadingdarkness11")
        assert data is None

    def test_case_insensitive_search():
        """It should return Pokémon data regardless of letter case."""
        data = fetch_pokemon("PikAchu")
        assert data is not None
        assert data["name"] == "pikachu"

    def test_numeric_string_id():
        """It should return data when a numeric string ID is passed."""
        data = fetch_pokemon("25")
        assert data is not None
        assert data["name"] == "pikachu"

    def test_edge_case_empty_string():
        """It should return None when an empty string is passed."""
        data = fetch_pokemon("")
        assert data is None

    def test_edge_case_special_characters():
        """It should return None when special characters are used."""
        data = fetch_pokemon("@!#$%^")
        assert data is None
