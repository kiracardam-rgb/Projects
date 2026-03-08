# Heat Pump Heat Loss Calculator

def calculate_heat_loss(u_value, area, temp_difference):
    return u_value * area * temp_difference


def main():
    print("Heat Loss Calculator")

    inside_temp = float(input("Enter inside temperature (°C): "))
    outside_temp = float(input("Enter outside temperature (°C): "))
    temp_difference = inside_temp - outside_temp

    total_heat_loss = 0

    number_of_surfaces = int(input("Enter number of surfaces: "))

    for i in range(number_of_surfaces):
        print("\nSurface", i + 1)
        name = input("Enter surface name: ")
        u_value = float(input("Enter U-value: "))
        area = float(input("Enter area in m^2: "))

        heat_loss = calculate_heat_loss(u_value, area, temp_difference)
        total_heat_loss += heat_loss

        print(name, "heat loss =", heat_loss, "W")

    print("\nTotal heat loss =", total_heat_loss, "W")


main()
