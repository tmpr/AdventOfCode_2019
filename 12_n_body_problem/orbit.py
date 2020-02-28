import numpy as np
from itertools import product

from moon import Moon
from utils_nbp import lowest_common_multiple

class Orbit:
    """
    Model of an Orbit with moons used for simulating their motion.
    
    `starting_positions` should be an iterable containing 3D-coordinates,
    representing the initial moon positions.
    """
    def __init__(self, starting_positions):

        self.moons = [Moon(starting_position)
                      for starting_position in starting_positions]
        self.starting_positions = starting_positions
        self.combinations_of_moons = [combination for combination in
                                      product(self.moons, self.moons)
                                      if len(set(combination)) > 1]

    def simulate_motion(self, timesteps=1):
        """Simulates orbit motion for given timesteps."""
        for _ in range(timesteps):
            self.apply_gravity_all()
            self.apply_velocity_all()

    def apply_gravity_all(self):
        """
        Calls apply_gravity for all possible pairs of
        moons in the orbit instance.
        """
        for combination in self.combinations_of_moons:
            combination[0].apply_gravity(combination[1])

    def apply_velocity_all(self):
        """Updates position of every moon according to its velocity."""
        for moon in self.moons:
            moon.apply_velocity()

    def return_orbit_energy(self, after_n_timesteps=0):
        """Returns sum of every moon's energy."""
        self.simulate_motion(timesteps=after_n_timesteps)
        orbit_energy = sum([moon.return_total_energy() for moon in self.moons])
        self.reset_orbit()
        return orbit_energy

    def return_axis_stats(self, axis: int):
        """
        Returns positions and velocities of all moons of orbit for given
        axis.
        """
        return np.array([moon.return_axis(axis) for moon in self.moons])

    def find_axis_cycle_length(self, axis: int):
        """
        Finds needed steps to simulate orbit motion until given
        axis has same stats again.
        """
        initial_axis_stats = self.return_axis_stats(axis)
        self.simulate_motion()
        steps = 1
        current_axis_stats = self.return_axis_stats(axis)
        while not (initial_axis_stats == current_axis_stats).all():
            self.simulate_motion()
            steps += 1
            current_axis_stats = self.return_axis_stats(axis)
        return steps

    def find_axis_cycles(self):
        """Returns cycle length of all axes."""
        self.reset_orbit()
        cycle_x = self.find_axis_cycle_length(0)
        self.reset_orbit()
        cycle_y = self.find_axis_cycle_length(1)
        self.reset_orbit()
        cycle_z = self.find_axis_cycle_length(2)
        self.reset_orbit()
        return cycle_x, cycle_y, cycle_z

    def full_cycle_length(self):
        try:
            return lowest_common_multiple(self.axis_cycles)
        except AttributeError:
            self.axis_cycles = self.find_axis_cycles()
            return lowest_common_multiple(self.axis_cycles)
        

    def reset_orbit(self):
        """Resets the orbit to its inital state."""
        self.moons = [Moon(starting_position)
                      for starting_position in self.starting_positions]
        self.combinations_of_moons = [combination for combination in
                                      product(self.moons, self.moons)
                                      if len(set(combination)) > 1]
