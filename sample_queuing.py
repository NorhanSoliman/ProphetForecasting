import numpy as np

def calculate_queue_size(predicted_orders, service_rate):
    queue_sizes = []
    for orders in predicted_orders:
        queue_size = np.ceil(orders / service_rate)  # ceiling to round up to the nearest whole number
        queue_sizes.append(int(queue_size))

    return queue_sizes

#a simple example of orders predictions at 20 minute intervals
predicted_orders = [15, 30, 25, 40, 20, 35, 50]
service_rate = 10  # number of orders per 20 minutes captains can fulfill

queue_sizes = calculate_queue_size(predicted_orders, service_rate)
print("Required queue sizes for captains at each 20-minute interval:", queue_sizes)
