import streamlit as st

st.title("Budget Allocator")

# Set total budget and number of categories
total_budget = st.number_input("Total Budget ($)", min_value=1000, value=5000, step=500)
num_categories = st.number_input("Number of Categories", min_value=1, value=2)

# Generate sliders for each category
allocations = [
    st.slider(f"Category {i+1} Allocation", min_value=0, max_value=total_budget, value=total_budget // num_categories)
    for i in range(num_categories)
]

# Calculate allocated and remaining budget
total_allocated = sum(allocations)
remaining_budget = total_budget - total_allocated

# Display budget summary
st.write("### Allocation Summary")
st.write(f"Total Allocated: ${total_allocated}")
st.write(f"Remaining Budget: ${remaining_budget}")

# Provide feedback based on budget status
if total_allocated > total_budget:
    st.error("You have exceeded the total budget!")
elif remaining_budget < total_budget * 0.1:
    st.warning("Warning: You are nearing your total budget.")
else:
    st.success("You are within the budget.")
