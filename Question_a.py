

def calculate_real_size(microscope_size, magnification_factor=100):
    
    return microscope_size / magnification_factor


microscope_size = float(input("Enter microscope size (in mm): "))
real_size = calculate_real_size(microscope_size)
print(f"Real-life size: {real_size:.2f} mm")
