import numpy as np
from scipy import interpolate

x = np.linspace(-20.139558, -20.115769, 1000)
y = np.linspace(-44.141856, -44.099738, 1000)
z = np.array([100.0, 50.0, 50.0, 25, 100.0])
dam = [-20.119026, -44.119985]
X, Y = np.meshgrid(x, y)
npts = 5
px, py = np.random.choice(x, npts), np.random.choice(y, npts)

x_points = np.array([-20.115769, -20.115769, -20.129558, -20.129558])
y_points = np.array([-44.141856, -44.119738, -44.141856, -44.119738])

z1 = np.array([np.random.random() * 100 for x, y in zip(x_points,
                                                        y_points)])
z2 = interpolate.griddata((x_points, y_points), z1, (X, Y),
                          method='nearest')
# print(z2)

mapa = [(x, y, z) for x, y, z in zip(X, Y, z2)]


class Position:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def calc_vector(self):
        v_pos_x, v_pos_y = (self.lat - dam[0], self.lng - dam[1])
        xf = float('%.6f' % (self.lat + v_pos_x))
        yf = float('%.6f' % (self.lng + v_pos_y))
        return {'lat': xf, 'lng': yf}
