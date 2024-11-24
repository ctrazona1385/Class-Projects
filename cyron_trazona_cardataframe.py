import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math
from statistics import mean

'''
This is my code for Homework 6

Author: Cyron Trazona
4/19/24

DSCI 1302
Section 2
'''

cars = pd.read_csv('car_info.csv')

print(f'1. Shape of the Dataframe: {cars.shape}')

jap_v6 = cars[(cars.cylinders ==6) & (cars.origin == 'japan')]
print(f'2. Japanese v6 cars: {[i for i in jap_v6.name]}')

no_hp = cars[cars.horsepower.isnull()]

print(f'3. Cars with Missing Horsepower Data:\n{no_hp[:9]}')

over20 = cars[(cars['mpg'] >= 20)]

print(f'4. Number of cars having >= 20mpg: {len(over20)}')

list_mpg = cars.sort_values(by='mpg', ascending = False)
print(f'5. Most Fuel-Efficient Car:{[i for i in list_mpg.name[:1]]}')

print(f'6. Minimum Weight: {min(cars.weight)}, Maximimum Weight: {max(cars.weight)}, Average Weight: {mean(cars.weight):.2f}')

clean_car = cars.dropna()

print(f'7. Shape after removing the missing values: {clean_car.shape}')

japcars = cars[cars['origin'] == 'japan']
uscars = cars[cars['origin']== 'usa']
eurocars = cars[cars['origin'] == 'europe']
total_cars = len(japcars) + len(uscars) + len(eurocars)
percent_by_country = pd.Series([int((len(japcars)/total_cars*100)),int((len(uscars)/total_cars*100)),int((len(japcars)/total_cars*100))])

num_cars = pd.Series([len(japcars),len(uscars),len(eurocars)])
car_origins = pd.Series(['Japan', 'USA', 'Europe'])

print(f'8. To be Displayed')

plt.pie(num_cars, labels = car_origins)
plt.legend()
plt.show()

cars_mpg = pd.Series([i for i in cars.mpg])
cars_weight = pd.Series([i for i in cars.weight])
cars_displace = pd.Series([i for i in cars.displacement])

print(f'9. To be dsiplayed')

plt.subplot(1,2,1)
plt.scatter(cars_mpg,cars_weight,label = 'Weight')
plt.xlabel('MPG')
plt.ylabel('Weight')
plt.title('MPG vs. Weight')
plt.legend()

plt.subplot(1,2,2)
plt.scatter(cars_mpg,cars_displace, label = 'Displacement')
plt.xlabel('MPG')
plt.ylabel('Displacement')
plt.title('MPG vs. Displacement')
plt.legend()
plt.show()