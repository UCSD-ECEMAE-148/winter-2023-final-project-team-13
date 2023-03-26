from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np

# Initialize Kalman filter
kf = KalmanFilter(dim_x=5, dim_z=2)

# Define state transition matrix and measurement function
dt = 1.0  # time step
kf.F = np.array([[1, 0, dt, 0, 0],
                 [0, 1, 0, dt, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1]])
kf.H = np.array([[1, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0]])

# Define process noise and measurement noise
q = Q_discrete_white_noise(dim=2, dt=dt, var=0.01)
kf.Q = np.diag([q, q, 0, 0, 0])
kf.R = np.diag([0.1, 0.1])

# Initialize state estimate and covariance matrix
kf.x = np.array([0, 0, 0, 0, 0]).T
kf.P = np.eye(5) * 10

# Initialize map
M = np.zeros((100, 100), dtype=np.uint8)

def get_gps_data():
    return [0, 0]

def get_lidar_data():
    return [0, 0, 0, 0]

def get_vesc_data():
    return [0, 0]

# Main loop
while True:
    # Get sensor data
    gps_data = get_gps_data()
    lidar_data = get_lidar_data()
    vesc_data = get_vesc_data()
    
    # Update Kalman filter with sensor data
    if gps_data is not None:
        kf.predict()
        kf.update(np.array([gps_data[0], gps_data[1]]))
    else:
        kf.predict()
        kf.update(np.array([kf.x[0, 0] + vesc_data[0], kf.x[1, 0] + vesc_data[1]]))
    
    # Update map using lidar data and current state estimate
    for j in range(len(lidar_data)):
        d = lidar_data[j]  # lidar measurement
        alpha = kf.x[2,0] + j*np.pi/2  # angle of lidar ray in world coordinates
        x_lidar = kf.x[0,0] + d*np.cos(alpha)  # x position of obstacle in world coordinates
        y_lidar = kf.x[1,0] + d*np.sin(alpha)  # y position of obstacle in world coordinates
        
        # Convert obstacle position from world coordinates to map coordinates
        x_map = int(x_lidar * 10) + 50  # scale by 10 and shift to center of map
        y_map = int(y_lidar * 10) + 50
        
        # Update map if obstacle is within bounds
        if x_map >= 0 and x_map < 100 and y_map >= 0 and y_map < 100:
            M[y_map, x_map] = 1
    
    # Print map
    print(M)
