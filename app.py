import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(layout="wide")

st.title("Bacteria Dataset Visualization 🦠")
data = pd.read_csv("bacteria_list_200.csv")
#print (data)

# This is a test
st.write(
    "This dashboard visualizes bacteria species, their taxonomic families, common habitats, "
    "and whether they are harmful to humans. The dataset is stored in a Google Cloud bucket. "
    "The goal of this project is to demonstrate how to extract meaningful insights from a small dataset using Python."
)

st.write(
    "The following is the dataset being used:")

st.subheader("Bacteria Datasheet")
st.write(data)

#Turn data into a DataFrame to use st.dataframe. Same thing as st.write for this purpose. 
#df = pd.DataFrame(data)
#st.dataframe(df)


###---------------------------PIE CHART---------------------------
#Strip whitespaces
data.columns = data.columns.str.strip()
data["Harmful to Humans"] = data["Harmful to Humans"].str.strip()

# Count occurrences
harmful_counts = data["Harmful to Humans"].value_counts()

st.subheader("Harmful vs Non-Harmful Bacteria")

fig, ax = plt.subplots()
ax.pie(
    harmful_counts,
    labels=harmful_counts.index,
    autopct="%1.1f%%",
    colors=["crimson", "lightgreen"],
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)
ax.axis("equal")  # Equal aspect ratio to ensure pie is a circle

st.pyplot(fig)

###---------------------------BAR CHART---------------------------
#This is a bar chart

data["Family"] = data["Family"].str.strip()
family_counts = data["Family"].value_counts().sort_values(ascending=False)

# Convert to DataFrame (in order to sort by largest to smallest)
df_family = family_counts.reset_index()
df_family.columns = ["Family", "Count"]
df_family = df_family.set_index("Family")

st.subheader("Bacteria by Family")
st.bar_chart(df_family)


#-----------ONLY HARMFUL BACTERIA-------------
st.subheader("Bacteria Harmful to Humans")
st.dataframe(data[data["Harmful to Humans"] == "Yes"])

#------------SEARCH BY NAME ------------------

st.subheader("Search 🔎")
search_term = st.text_input("Type a Bacteria Name")
if search_term:
    result = data[data["Name"].str.contains(search_term, case=False)]
    st.write(result)


#-----------Trying new things

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


# Sample data
data = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Value1": [10, 20, 30],
    "Value2": [5, 15, 25]
})

# Create columns
col1, col2 = st.columns(2)
# First chart (in column 1)
with col1:
    st.subheader("Bar Chart")
    st.bar_chart(data.set_index("Category")["Value1"])

# Second chart (in column 2)
with col2:
    st.subheader("Line Chart")
    st.line_chart(data.set_index("Category")["Value2"])