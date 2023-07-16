import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("CSV Data Display")
    
    # Load the CSV data
    data = pd.read_csv('a.csv')
    
    # Get the column names
    column_names = data.columns.tolist()
    
    # Define the specific columns for the dropdowns
    specific_column = 'Type'
    specific_column_2 = 'Magnitude Type'
    
    # Let the user select the specific column for the first dropdown
    specific_column = st.selectbox("Select a column", column_names, index=column_names.index(specific_column))
    
    # Get unique values from the specific column
    dropdown_options = data[specific_column].unique()
    
    # Create the first dropdown with the specific column values
    dropdown_value = st.selectbox("Select an option", dropdown_options)
    
    # Filter the data based on the selected option
    filtered_data = data[data[specific_column] == dropdown_value]
    
    # Let the user select the specific column for the second dropdown
    specific_column_2 = st.selectbox("Select a column", column_names, index=column_names.index(specific_column_2))
    
    # Get unique values from the second specific column
    dropdown_options_2 = filtered_data[specific_column_2].unique()
    
    # Create the second dropdown with the specific column values
    dropdown_value_2 = st.selectbox("Select an option", dropdown_options_2)
    
    # Filter the data further based on the second dropdown selection
    filtered_data = filtered_data[filtered_data[specific_column_2] == dropdown_value_2]
    
    # Display the filtered data
    st.write(filtered_data)
    
    # Plot 1
    st.header("Plot 1")
    fig1 = px.scatter(filtered_data, x='Latitude', y='Longitude')
    st.plotly_chart(fig1, use_container_width=True)
    
    # Plot 2
    st.header("Plot 2")
    fig2 = px.scatter(filtered_data, x='Magnitude', y='Depth')
    st.plotly_chart(fig2, use_container_width=True)
    
    # Plot 3
    st.header("Plot 3")
    fig3 = px.scatter(filtered_data, x='Depth', y='Magnitude')
    st.plotly_chart(fig3, use_container_width=True)

if __name__ == '__main__':
    main()
