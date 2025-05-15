import streamlit as st
import requests

st.title("🍽️ Free Recipe Finder with TheMealDB")

search_term = st.text_input("Enter dish name to search:", "")

def get_meal_data(query):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("meals")
    else:
        return None

def format_ingredients(meal):
    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            ingredients.append(f"{measure.strip()} {ingredient.strip()}")
    return "\n".join(ingredients)

if search_term:
    meals = get_meal_data(search_term)
    if meals:
        for meal in meals:
            st.subheader(meal["strMeal"])
            st.image(meal["strMealThumb"], width=300)
            st.markdown("**Category:** " + (meal.get("strCategory") or "N/A"))
            st.markdown("**Area:** " + (meal.get("strArea") or "N/A"))
            
            st.markdown("### Ingredients:")
            st.text(format_ingredients(meal))
            
            st.markdown("### Instructions:")
            st.write(meal["strInstructions"])
            
            st.markdown("---")
    else:
        st.warning("No meals found. Try another search term.")
