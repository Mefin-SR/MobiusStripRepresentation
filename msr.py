import numpy as np
import matplotlib.pyplot as plt

class MobiusStrip:

  def __init__(self, radius, width, num_points=100):

    self.radius = radius
    self.width = width
    self.num_points = num_points

    self.u = np.linspace(0, 2 * np.pi, num_points)
    self.v = np.linspace(-self.width/2, self.width/2, num_points)

    self.x, self.y, self.z = self._compute_surface()


  def _compute_surface(self):
    """
    Using parametric equations, compute the coordinates of the mobius strip.
    """

    u, v = np.meshgrid(self.u, self.v)

    x = (self.radius + v * np.cos(u/2)) * np.cos(u)
    y = (self.radius + v * np.cos(u/2)) * np.sin(u)
    z = v * np.sin(u / 2)

    return x, y, z

  def compute_surface_area(self):
    """
    Computes the surface area of the mobius strip using approximation
    formula : edge of circle mutiplied by width.
    """

    return 2 * np.pi * self.radius * self.width

  def compute_edge_length(self):
    """
    Computes the edge length of the mobius strip using approximation
    formula : two times the edge length of the circle.
    """

    return 4 * np.pi * self.radius


  def plot(self):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(self.x, self.y, self.z, cmap='viridis')
    ax.set_title("Mobius Strip")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()


if __name__ == "__main__":

    mobius = MobiusStrip(radius=2, width=1, num_points=100)

    area = mobius.compute_surface_area()
    edge_length = mobius.compute_edge_length()

    print(f"Surface Area ≈ {area:.4f}")
    print(f"Edge Length ≈ {edge_length:.4f}")

    mobius.plot()
