def getGasPrice(travel_states, fuel_type):
  price = 0
  count = 0
  for state in travel_states:
    price += states[state][fuel_type]
    count += 1

  return price / count

states = {
  "Alaska": {
    "Regular": 4.76,
    "Midgrade": 4.906,
    "Premium": 5.127,
    "Diesel": 5.287
  },
  "Alabama": {
    "Regular": 3.308,
    "Midgrade": 3.682,
    "Premium": 4.065,
    "Diesel": 4.995
  },
  "Arkansas": {
    "Regular": 3.247,
    "Midgrade": 3.603,
    "Premium": 3.962,
    "Diesel": 4.935
  },
  "Arizona": {
    "Regular": 4.256,
    "Midgrade": 4.563,
    "Premium": 4.833,
    "Diesel": 5.14
  },
  "California": {
    "Regular": 5.461,
    "Midgrade": 5.669,
    "Premium": 5.819,
    "Diesel": 6.296
  },
  "Colorado": {
    "Regular": 3.514,
    "Midgrade": 3.853,
    "Premium": 4.148,
    "Diesel": 5.104
  },
  "Connecticut": {
    "Regular": 3.76,
    "Midgrade": 4.24,
    "Premium": 4.639,
    "Diesel": 5.993
  },
  "District of Columbia": {
    "Regular": 3.809,
    "Midgrade": 4.363,
    "Premium": 4.742,
    "Diesel": 5.238
  },
  "Delaware": {
    "Regular": 3.863,
    "Midgrade": 4.262,
    "Premium": 4.564,
    "Diesel": 5.75
  },
  "Florida": {
    "Regular": 3.456,
    "Midgrade": 3.829,
    "Premium": 4.151,
    "Diesel": 5.231
  },
  "Georgia": {
    "Regular": 3.125,
    "Midgrade": 3.51,
    "Premium": 3.866,
    "Diesel": 4.938
  },
  "Hawaii": {
    "Regular": 5.201,
    "Midgrade": 5.447,
    "Premium": 5.683,
    "Diesel": 6.067
  },
  "Iowa": {
    "Regular": 3.551,
    "Midgrade": 3.813,
    "Premium": 4.291,
    "Diesel": 5.135
  },
  "Idaho": {
    "Regular": 4.298,
    "Midgrade": 4.482,
    "Premium": 4.712,
    "Diesel": 5.435
  },
  "Illinois": {
    "Regular": 4.324,
    "Midgrade": 4.765,
    "Premium": 5.173,
    "Diesel": 5.318
  },
  "Indiana": {
    "Regular": 4.197,
    "Midgrade": 4.575,
    "Premium": 4.962,
    "Diesel": 5.539
  },
  "Kansas": {
    "Regular": 3.379,
    "Midgrade": 3.661,
    "Premium": 3.956,
    "Diesel": 4.999
  },
  "Kentucky": {
    "Regular": 3.5,
    "Midgrade": 3.917,
    "Premium": 4.264,
    "Diesel": 5.268
  },
  "Louisiana": {
    "Regular": 3.264,
    "Midgrade": 3.636,
    "Premium": 3.995,
    "Diesel": 4.862
  },
  "Massachusetts": {
    "Regular": 3.837,
    "Midgrade": 4.332,
    "Premium": 4.665,
    "Diesel": 5.841
  },
  "Maryland": {
    "Regular": 3.76,
    "Midgrade": 4.238,
    "Premium": 4.524,
    "Diesel": 5.763
  },
  "Maine": {
    "Regular": 3.93,
    "Midgrade": 4.302,
    "Premium": 4.673,
    "Diesel": 5.889
  },
  "Michigan": {
    "Regular": 4.228,
    "Midgrade": 4.607,
    "Premium": 5.042,
    "Diesel": 5.44
  },
  "Minnesota": {
    "Regular": 3.606,
    "Midgrade": 3.911,
    "Premium": 4.294,
    "Diesel": 5.236
  },
  "Missouri": {
    "Regular": 3.366,
    "Midgrade": 3.624,
    "Premium": 3.952,
    "Diesel": 5.025
  },
  "Mississippi": {
    "Regular": 3.216,
    "Midgrade": 3.569,
    "Premium": 3.927,
    "Diesel": 4.872
  },
  "Montana": {
    "Regular": 3.889,
    "Midgrade": 4.165,
    "Premium": 4.446,
    "Diesel": 5.385
  },
  "North Carolina": {
    "Regular": 3.364,
    "Midgrade": 3.721,
    "Premium": 4.079,
    "Diesel": 5.156
  },
  "North Dakota": {
    "Regular": 3.641,
    "Midgrade": 3.954,
    "Premium": 4.301,
    "Diesel": 5.23
  },
  "Nebraska": {
    "Regular": 3.474,
    "Midgrade": 3.71,
    "Premium": 4.193,
    "Diesel": 5.058
  },
  "New Hampshire": {
    "Regular": 3.778,
    "Midgrade": 4.217,
    "Premium": 4.598,
    "Diesel": 5.782
  },
  "New Jersey": {
    "Regular": 3.92,
    "Midgrade": 4.418,
    "Premium": 4.682,
    "Diesel": 5.876
  },
  "New Mexico": {
    "Regular": 3.542,
    "Midgrade": 3.866,
    "Premium": 4.148,
    "Diesel": 4.984
  },
  "Nevada": {
    "Regular": 4.956,
    "Midgrade": 5.193,
    "Premium": 5.406,
    "Diesel": 5.417
  },
  "New York": {
    "Regular": 3.866,
    "Midgrade": 4.285,
    "Premium": 4.636,
    "Diesel": 5.893
  },
  "Ohio": {
    "Regular": 3.874,
    "Midgrade": 4.255,
    "Premium": 4.641,
    "Diesel": 5.723
  },
  "Oklahoma": {
    "Regular": 3.371,
    "Midgrade": 3.705,
    "Premium": 3.939,
    "Diesel": 4.922
  },
  "Oregon": {
    "Regular": 4.841,
    "Midgrade": 5.062,
    "Premium": 5.26,
    "Diesel": 5.564
  },
  "Pennsylvania": {
    "Regular": 4.07,
    "Midgrade": 4.412,
    "Premium": 4.679,
    "Diesel": 6.09
  },
  "Rhode Island": {
    "Regular": 3.851,
    "Midgrade": 4.422,
    "Premium": 4.733,
    "Diesel": 5.925
  },
  "South Carolina": {
    "Regular": 3.277,
    "Midgrade": 3.636,
    "Premium": 3.989,
    "Diesel": 5.016
  },
  "South Dakota": {
    "Regular": 3.654,
    "Midgrade": 3.843,
    "Premium": 4.295,
    "Diesel": 5.158
  },
  "Tennessee": {
    "Regular": 3.287,
    "Midgrade": 3.66,
    "Premium": 4.021,
    "Diesel": 5.134
  },
  "Texas": {
    "Regular": 3.176,
    "Midgrade": 3.546,
    "Premium": 3.882,
    "Diesel": 4.724
  },
  "Utah": {
    "Regular": 4.104,
    "Midgrade": 4.312,
    "Premium": 4.509,
    "Diesel": 5.319
  },
  "Virginia": {
    "Regular": 3.487,
    "Midgrade": 3.898,
    "Premium": 4.218,
    "Diesel": 5.283
  },
  "Vermont": {
    "Regular": 3.959,
    "Midgrade": 4.478,
    "Premium": 4.89,
    "Diesel": 6.013
  },
  "Washington": {
    "Regular": 4.83,
    "Midgrade": 5.057,
    "Premium": 5.255,
    "Diesel": 5.713
  },
  "Wisconsin": {
    "Regular": 3.862,
    "Midgrade": 4.217,
    "Premium": 4.683,
    "Diesel": 5.137
  },
  "West Virginia": {
    "Regular": 3.601,
    "Midgrade": 3.873,
    "Premium": 4.152,
    "Diesel": 5.562
  },
  "Wyoming": {
    "Regular": 3.723,
    "Midgrade": 3.918,
    "Premium": 4.201,
    "Diesel": 5.406
  }
}