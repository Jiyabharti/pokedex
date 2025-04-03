from re import match
import streamlit as st
import requests
import re


API_URL = "https://pokeapi-proxy.freecodecamp.rocks/api/pokemon/"

# Function to fetch data from API for a given Pokemon name or ID
def fetch_pokemon(identifier):
    response = requests.get(API_URL + str(identifier).lower())
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to fetch full list of pokemon
def fetch_all_pokemon():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()['results']  # List of dictionaries with 'name' and 'url'
    else:
        return []

# regex check
def is_valid_input(user_input):
    return re.fullmatch(r"[a-zA-Z0-9-]+", user_input.strip()) is not None


def main():
    st.title("Pokedex")

    #  for searching a specific Pokemon
    pokemon_id_or_name = st.text_input("Enter Pokemon Name or ID:", "")

    # If user clicks the Search button
    if st.button("Search"):
        if pokemon_id_or_name:
            if is_valid_input(pokemon_id_or_name):
                data = fetch_pokemon(pokemon_id_or_name)

                if data:
                    # display Pokemon name and image
                    st.subheader(f"Name: {data['name'].capitalize()}")
                    st.image(data['sprites']['front_default'], caption=data['name'].capitalize(), width=200)

                    st.write("Stats")
                    for stat in data['stats']:
                        st.write(f"**{stat['stat']['name'].capitalize()}:** {stat['base_stat']}")

                    # Display Types
                    st.write("Types")
                    for types in data['types']:
                        st.write(f"**Type:** {types['type']['name'].capitalize()}")
                else:
                    st.error("Pokemon not found! Try another name or ID.")
            else:
                # If input is invalid (symbols or special characters)
                st.error("Only letters and numbers please")
        else:
            st.warning("Please enter a Pokemon name or ID.")

    # list frst 10 pokemon
    st.markdown("---")
    st.subheader("First 10 Pokemon")

    if st.checkbox("Show First 10 Pokemon"):
        pokemon_list = fetch_all_pokemon()
        if pokemon_list:
            for pokemon in pokemon_list[0:10]:
                if st.button(pokemon['name'].capitalize()):
                    data_list = fetch_pokemon(pokemon['name'])
                    if data_list:
                        st.subheader(f"Name: {data_list['name'].capitalize()}")
                        st.image(data_list['sprites']['front_default'], caption=data_list['name'].capitalize(), width=200)
                        (st.write
                         ("Stats"))
                        for stat in data_list['stats']:
                            st.write(f"**{stat['stat']['name'].capitalize()}:** {stat['base_stat']}")

                        st.write("Types")
                        for types in data_list['types']:
                            st.write(f"**Type:** {types['type']['name'].capitalize()}")



# TURN THE IF'S into IF NOT to reduce the number of if statements
# ELIF



if __name__ == "__main__":
    main()



