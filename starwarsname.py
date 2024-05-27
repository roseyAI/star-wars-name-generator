import streamlit as st

st.write("""
# 🌌 Star Wars Name Generator 🛰️
Find out your Star Wars name today in just a few clicks!
""")
# gif
st.markdown("![Alt Text](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXUyajk4NHk0YXc0Zzl6cHFqcXQ1b2lraW42ZjlmM3JjZTZmbWlhdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohuPdEqZR8tDeuN3O/giphy.gif)")

# Use Streamlit's text input to get user inputs
firstName = st.text_input("Enter your first name:").title()
lastName = st.text_input("Enter your last name:").lower()
maidenName = st.text_input("Enter your mother's maiden name:").title()
cityName = st.text_input("Enter the city you were born:").lower()

# Add a button to generate the Star Wars name
if st.button('Generate'):
    # Ensure all inputs are provided before generating the name
    if firstName and lastName and maidenName and cityName:
        first = firstName[:3]
        last = lastName[:3]
        maiden = maidenName[:2]
        city = cityName[:3]

        # Display the Star Wars name using Streamlit
        st.title(f"Your Star Wars name is: 🌠 {first}{last} {maiden}{city} 🌠")
    else:
        st.write("Please fill in all the fields.")
