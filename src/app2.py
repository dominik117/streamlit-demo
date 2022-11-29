# standard imports
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# importing data source
data = px.data.gapminder()

# defining page title
st.title("Country cross socio-economic data analysis")

# sidebar checkbox to show dataframe
if st.sidebar.checkbox("Show data source"):
    st.header("Socio-economic data per country")
    st.dataframe(data.head())

# setting up columns
# left_column, right_column = st.columns([1, 1])

# FIGURE 1

# first figure widget
continents = ["All"]+sorted(data['continent'].unique())
for continent in continents:
    continent = st.sidebar.checkbox(continent)  #"Choose continent(s) for life expectancy distribution", continents)
#selectbox #multiselect

# first figure title
st.header("Life expectancy distribution (2007)")

# first figure flow control and plot with plotly
continents = data['continent'].unique()

fig = go.Figure()

for continent in continents:
    y = data[(data['continent'] == continent) & (data['year'] == 2007)]['lifeExp']
    fig.add_trace(go.Box(y=y, name=continent))

st.plotly_chart(fig)

# FIGURE 2

# second figure widget
continent = st.sidebar.selectbox("Choose continent(s) for GDP per capita vs Life expectancy", continents)