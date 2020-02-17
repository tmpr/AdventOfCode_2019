import cv2
import shutil
import numpy as np
import matplotlib.pyplot as plt
import os
from math import sin, cos, pi

from utils import *
from color_values import *

class Asteroid:
    """Model of an Asteroid."""
    def __init__(self, coordinates, parent_belt):
        self.coordinates = coordinates
        self.parent_belt = parent_belt
        self.perspective = dict()
        self.visible_asteroid_count = 0

    def generate_perspective(self):
        """
        Produces a dict, where the keys are directions (unit vectors)
        and values are asteroids which lie in that direction.
        Additionally determines and sets the amount of visible asteroids.
        """
        for other_asteroid in self.parent_belt.asteroids:
            if other_asteroid == self:
                continue
            else:
                self.assign_to_perspective(other_asteroid)

        # The number of directions is also the number of visible asteroids.
        self.visible_asteroid_count = len(self.perspective.keys())

    def assign_to_perspective(self, other,):
        """
        Given some other asteroid, finds out in which
        direction it lies, i.e. which unit vector leads to it.
        """
        between = vector_between(other.coordinates, self.coordinates)
        unit_vector = calculate_unit_vector(between, 3)
        if unit_vector in self.perspective.keys():
            self.perspective[unit_vector].append(tuple(other.coordinates))
        else:
            self.perspective[unit_vector] = [tuple(other.coordinates)]

    def simulate_destruction(self, n_asteroids: int, v_title, make_video=False):
        """
        Simulates a circling laser which can only destroy 1 asteroid
        when passing by. Returns last asteroid after destroying `n_asteroids`
        in a way of 10*x-coordinate + y-coordinate.

        If `make_video` is True, saves a video into the working 
        directory.
        """
        # Values important for longer
        self.destroyed_asteroids = []
        self.initial_perspective = self.perspective.copy()
        
        # Initial values
        phi = round(3 * pi / 2, 5)
        laser_direction = (round(cos(phi), 3), round(sin(phi), 3))

        if make_video:
            self.video_title = v_title
            self.video_folder = "temp_images"
            self.value_matrix = np.array(self.parent_belt.matrix, dtype=np.float)
            if not os.path.exists(self.video_folder):
                os.makedirs(self.video_folder)

        while len(self.destroyed_asteroids) < n_asteroids:
            if laser_direction in self.perspective.keys():
                self.process_new_laser_direction(laser_direction, make_video)
            laser_direction, phi = update_direction_and_phi(laser_direction, phi)
            
        if make_video:
            print("Images have been taken.")
            print("Rendering video.")
            self.produce_video(self.video_folder, self.video_title)

        self.perspective = self.initial_perspective

        return (self.destroyed_asteroids[n_asteroids - 1][0] * 100 +
                self.destroyed_asteroids[n_asteroids - 1][1])

    def process_new_laser_direction(self, laser_direction, make_video):
        
        # Dummy values.
        closest_id = 0
        current_smallest_magnitude = 1000000
        visible_asteroids = self.perspective[laser_direction]

        # Check and reset values
        for asteroid_id, asteroid_coords in enumerate(visible_asteroids):
            current_magnitude = get_magnitude(
                vector_between(asteroid_coords, self.coordinates))
            if current_magnitude < current_smallest_magnitude:
                closest_id = asteroid_id
                current_smallest_magnitude = current_magnitude
                closest_asteroid_coords = asteroid_coords

        try:
            killed_asteroid = self.perspective[laser_direction].pop(
                closest_id)

            if make_video:
                self.value_matrix[closest_asteroid_coords] = UNDER_ATTACK
                self.save_belt_as_image(
                    self.video_folder, laser_direction, len(self.destroyed_asteroids))
                self.value_matrix[closest_asteroid_coords] = DESTROYED
            
            self.destroyed_asteroids.append(killed_asteroid)
        except BaseException:
            pass

    def produce_video(self, folder_path, video_name: str):
        """Produces a video of all saved images."""
        image_folder = folder_path
        video_name = self.video_title + ".avi"

        images = [img for img in os.listdir(
                  image_folder) if img.endswith(".png")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, _ = frame.shape

        video = cv2.VideoWriter(video_name, 0, 5, (width, height))

        for image in sorted(images):
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()

        shutil.rmtree(self.video_folder)
        
        print(f"Video saved.")

    def save_belt_as_image(self, folder, laser_direction, current_iteration):
        """
        Saves an image of the field as a matrix and the current laser.
        For the color values, look into the corresponding file.
        """
        y, x = self.coordinates
        dy, dx = laser_direction
        plt.arrow(x, y, 1000 * dx, 1000 * dy, color="red")
        plt.imshow(self.value_matrix, animated=True, cmap="inferno")

        file_number = (4 - len(str(current_iteration))) * \
            "0" + str(current_iteration)

        plt.savefig(os.path.join(folder, f"{file_number}.png"))
        plt.close()