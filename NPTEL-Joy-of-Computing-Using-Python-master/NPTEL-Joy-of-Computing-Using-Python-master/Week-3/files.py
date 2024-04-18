# import random

# messages = ['It is certain',
#             'It is decidedly so',
#             'Yes definitely',
#             'Reply hazy try again',
#             'Ask again later',
#             'Concentrate and ask again',
#             'My reply is no',
#             'Outlook not so good',
#             'Very doubtful']

# select_number = random.randint(0, len(messages) - 1)
# list_select  = messages[select_number]
# print(list_select)



import random

random()                          # Random float:  0.0 <= x < 1.0


uniform(2.5, 10.0)                # Random float:  2.5 <= x <= 10.0


expovariate(1 / 5)                # Interval between arrivals averaging 5 seconds

randrange(10)                     # Integer from 0 to 9 inclusive


randrange(0, 101, 2)              # Even integer from 0 to 100 inclusive


choice(['win', 'lose', 'draw'])   # Single random element from a sequence
'draw'

deck = 'ace two three four'.split()
shuffle(deck)                     # Shuffle a list
deck
['four', 'two', 'ace', 'three']

sample([10, 20, 30, 40, 50], k=4) # Four samples without replacement
[40, 10, 50, 30]




from heapq import heapify, heapreplace
from random import expovariate, gauss
from statistics import mean, quantiles

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
heapify(servers)
for i in range(1_000_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = servers[0]
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
    service_completed = arrival_time + wait + service_duration
    heapreplace(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
print('Quartiles:', [round(q, 1) for q in quantiles(waits)])


# Six roulette wheel spins (weighted sampling with replacement)
choices(['red', 'black', 'green'], [18, 18, 2], k=6)
['red', 'green', 'black', 'black', 'red', 'black']

# Deal 20 cards without replacement from a deck
# of 52 playing cards, and determine the proportion of cards
# with a ten-value:  ten, jack, queen, or king.
deal = sample(['tens', 'low cards'], counts=[16, 36], k=20)
deal.count('tens') / 20
0.15

# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.
sum(binomialvariate(n=7, p=0.6) >= 5 for i in range(10_000)) / 10_000
0.4169




# Probability of the median of 5 samples being in middle two quartiles
def trial():
    return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500

sum(trial() for i in range(10_000)) / 10_000




# https://www.thoughtco.com/example-of-bootstrapping-3126155
from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(choices(data, k=len(data))) for i in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')



# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
from statistics import fmean as mean
from random import shuffle

drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)

n = 10_000
count = 0
combined = drug + placebo
for i in range(n):
    shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')
