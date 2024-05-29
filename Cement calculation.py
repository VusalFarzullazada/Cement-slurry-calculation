import math


def calculate_annular_volume(height, hole_diameter, casing_od, excess_percentage=0):
    """
    Calculate the volume of the annular space between the casing and the wellbore.

    Parameters:
    height (float): Height (or depth) of the well in feet.
    hole_diameter (float): Diameter of the open hole (wellbore) in inches.
    casing_od (float): Outside diameter (OD) of the casing in inches.
    excess_percentage (float): Excess cement percentage (default is 0).

    Returns:
    float: Total volume of cement slurry needed in barrels (bbl).
    """
    # Convert inches to feet for volume calculation
    hole_diameter = float(hole_diameter) / 12  # convert inches to feet
    casing_od = float(casing_od) / 12  # convert inches to feet

    # Calculate the cross-sectional areas in square feet
    hole_area = math.pi * (hole_diameter / 2) ** 2
    casing_area = math.pi * (casing_od / 2) ** 2

    # Calculate the annular area in square feet
    annular_area = hole_area - casing_area

    # Calculate the annular volume in cubic feet
    annular_volume = annular_area * float(height)

    # Add excess cement volume
    excess_volume = annular_volume * (float(excess_percentage) / 100)
    total_cement_volume_cubic_feet = annular_volume + excess_volume

    # Convert cubic feet to barrels (bbl)
    total_cement_volume_bbl = total_cement_volume_cubic_feet / 5.615

    return total_cement_volume_bbl


def main():
    print("Cement Slurry Volume Calculator")

    # Prompt the user for input values
    height = input("Enter the height (depth) of the well (in feet): ")
    hole_diameter = input("Enter the diameter of the open hole (wellbore) (in inches): ")
    casing_od = input("Enter the outside diameter (OD) of the casing (in inches): ")
    excess_percentage = input("Enter the excess cement percentage (optional, default is 0): ")

    # Handle optional input for excess percentage
    if not excess_percentage:
        excess_percentage = 0
    else:
        excess_percentage = float(excess_percentage)

    # Calculate the required amount of cement slurry in barrels
    cement_volume = calculate_annular_volume(height, hole_diameter, casing_od, excess_percentage)
    print(f"\nThe required amount of cement slurry is {cement_volume:.2f} barrels (bbl).")


if __name__ == "__main__":
    main()
