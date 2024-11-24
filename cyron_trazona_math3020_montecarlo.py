import numpy as np
import matplotlib.pyplot as plt

#Parameters
num_cpu = 20
infection_prob = .1
num_trials = 1000
technician_cleans = 5

#Simulation function
def monte_carlo_simulation():
    #Initial infection status: 1 infected computer
    infection_status = np.zeros(num_cpu, dtype=bool)
    initial_infected = np.random.randint(0, num_cpu)  #Infect one computer at random
    infection_status[initial_infected] = True

    #Track if a computer has ever been infected
    ever_infected = infection_status.copy()
    
    #Count how many days it takes to clean all infections
    days = 0
    while infection_status.any():  #While there are infected computers
        days += 1
        
        #Spread infection: Each infected computer has a chance to infect others
        new_infections = np.zeros(num_cpu, dtype=bool)
        for i in range(num_cpu):
            if infection_status[i]:  #If computer i is infected
                #Determine infections for each uninfected computer
                uninfected = np.where(~infection_status)[0]  #Indices of uninfected computers
                if uninfected.size > 0:
                    infections = np.random.rand(uninfected.size) < infection_prob
                    new_infections[uninfected] = infections
        
        #Update infection status
        infection_status |= new_infections
        ever_infected |= infection_status  #Track ever-infected computers

        #Technician cleans 5 infected computers at random
        infected_indices = np.where(infection_status)[0]
        if len(infected_indices) > technician_cleans:
            cleaned = np.random.choice(infected_indices, size=technician_cleans, replace=False)
        else:
            cleaned = infected_indices  #Clean all if fewer than 5
        infection_status[cleaned] = False  #Clean selected computers

    #Return the number of days, the total number of infected computers, and the ever infected status
    return days, ever_infected.sum(), ever_infected

#Run Monte Carlo Simulation
results_days = []
results_total_infected = []
ever_infected_counts = np.zeros(num_cpu, dtype=int)

for n in range(num_trials):
    days_to_clear, total_infected, ever_infected = monte_carlo_simulation()
    results_days.append(days_to_clear)
    results_total_infected.append(total_infected)
    ever_infected_counts += ever_infected  #Increment count for computers that were infected

#Convert results to NumPy arrays
results_days = np.array(results_days)
results_total_infected = np.array(results_total_infected)

#Calculate statistics
average_days_to_clear = np.mean(results_days)
average_infections = np.mean(results_total_infected)

#Output Results
print(f"Average days to completely clean the computers: {average_days_to_clear:.2f}")
print(f"Average number of computers infected per trial: {average_infections:.2f}")

#Visualize Results
#1. Histogram of days to clear infections
hist_data, bins, n = plt.hist(results_days, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel("Days to Clear Infections")
plt.ylabel("Frequency")
plt.title(f"Days to Clear Infections\nAverage: {average_days_to_clear:.2f} Days")
#Add numeric values above bars (exclude zeros)
for i in range(len(hist_data)):
    if hist_data[i] > 0:  #Only display non-zero values
        plt.text(bins[i] + (bins[i + 1] - bins[i]) / 2, hist_data[i], str(int(hist_data[i])), ha='center', va='bottom', fontsize=8)
plt.show()

#2. Histogram of total infections
hist_data, bins, n = plt.hist(results_total_infected, bins=np.arange(0, num_cpu + 1), edgecolor='black', alpha=0.7)
plt.xlabel("Number of Computers Infected")
plt.ylabel("Frequency")
plt.title(f"Number of Infected Computers Per Trial\nAverage: {average_infections:.2f}")

#Set integer ticks for x-axis
plt.xticks(ticks=np.arange(0, num_cpu + 1, 2))  #Show ticks at every 2 computers

#Add numeric values above bars (exclude zeros)
for i in range(len(hist_data)):
    if hist_data[i] > 0:  #Only display non-zero values
        plt.text(bins[i] + 0.5, hist_data[i], str(int(hist_data[i])), ha='center', va='bottom', fontsize=8)

plt.show()


#3. Bar chart of "ever infected" occurrences for each computer
plt.bar(range(1, num_cpu + 1), ever_infected_counts)
plt.xlabel("Computer")
plt.ylabel("Number of Trials Ever Infected")
plt.title("Number of Trials Each Computer Was Ever Infected")
#Add numeric values above bars (exclude zeros)
for i, count in enumerate(ever_infected_counts):
    if count > 0:  #Only display non-zero values
        plt.text(i + 1, count, str(count), ha='center', va='bottom', fontsize=8)
plt.xticks(range(1, num_cpu + 1))  #Label each computer
plt.show()
