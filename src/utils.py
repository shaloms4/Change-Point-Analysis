def print_assumptions():
    print("ASSUMPTIONS & LIMITATIONS")
    print("- Structural breaks can be identified, but exact causes must be interpreted cautiously.")
    print("- Correlation in time does not imply causation.")
    print("- Some price shifts may align with events by chance.")
    print("- Some events may not yield immediate price effects.")

def print_change_point_purpose():
    print("Change Point Models help detect time periods where the underlying data distribution shifts.")
    print("They identify points in time when the mean/variance of oil prices changes due to external shocks.")
    print("Expected Outputs: list of change points, mean/variance values before and after.")
