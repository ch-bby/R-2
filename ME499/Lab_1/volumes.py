#!\usr\bin\env python3
"""ME 499 Lab 1 Part 1-3
    Samuel J. Stumbo
    This script "builds" on last week's volume calculator by placing it within the context of a function"""

from math import pi

# This function calculates the volumes of a cylinder
def cylinder_volume(r, h):
    if type(r) == int and type(h) == int:
        float(r)
        float(h)

        if r < 0 or h < 0:
            return None
            # print('you may have entered a negative number')
        else:
            volume = pi * r ** 2 * h
            return volume
    elif type(r) == float and type(h) == float:
        if r < 0 or h < 0:
            return None
        else:
            volume = pi * r ** 2 * h
            return volume
    else:
        # print("You must have entered a string!")
        return None


# This function calculates the volume of a torus
def volume_tor(inner_radius, outer_radius):
    if type(inner_radius) == int and type(outer_radius) == int:
        float(inner_radius)
        float(outer_radius)
        if inner_radius < 0 or outer_radius < 0:
            return None
        else:
            if inner_radius > outer_radius:
                return None
            elif inner_radius == outer_radius:
                return None
            else:
                r_mid = (inner_radius + outer_radius) / 2  # Average radius of torus
                r_circle = (outer_radius - inner_radius) / 2  # Radius of donut cross-section
                volume = (pi * r_circle ** 2) * (2 * pi * r_mid)
                return volume
    elif type(inner_radius) == float and type(outer_radius) == float:
        if r < 0 and h < 0:
            return None
        else:
            if inner_radius > outer_radius:
                return None
            elif inner_radius == outer_radius:
                return None
            else:
                r_mid = (inner_radius + outer_radius) / 2  # Average radius of torus
                r_circle = (outer_radius - inner_radius) / 2  # Radius of donut cross-section
                volume = (pi * r_circle ** 2) * (2 * pi * r_mid)
                return volume
    else:
        return None


if __name__ == '__main__':
    print(cylinder_volume(3, 1))
    print(volume_tor(-2, 7))

