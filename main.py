import skfuzzy as fuzz
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Drawing input diagrams
health_level = ctrl.Antecedent(np.arange(0, 100, 0.1), 'health_level')
health_level['Poor'] = fuzz.trimf(health_level.universe, [0, 0, 40])
health_level['Medium'] = fuzz.trimf(health_level.universe, [30, 50, 70])
health_level['Good'] = fuzz.trimf(health_level.universe, [60, 100, 100])

spicy_preference = ctrl.Antecedent(np.arange(0, 10, 0.1), 'spicy_preference')
spicy_preference['Low'] = fuzz.trimf(spicy_preference.universe, [0, 0, 4])
spicy_preference['Medium'] = fuzz.trimf(spicy_preference.universe, [2, 5, 8])
spicy_preference['High'] = fuzz.trimf(spicy_preference.universe, [6, 10, 10])

sweet_preference = ctrl.Antecedent(np.arange(0, 10, 0.1), 'sweet_preference')
sweet_preference['Low'] = fuzz.trimf(sweet_preference.universe, [0, 0, 4])
sweet_preference['Medium'] = fuzz.trimf(sweet_preference.universe, [2, 5, 8])
sweet_preference['High'] = fuzz.trimf(sweet_preference.universe, [6, 10, 10])

sour_preference = ctrl.Antecedent(np.arange(0, 10, 0.1), 'sour_preference')
sour_preference['Low'] = fuzz.trimf(sour_preference.universe, [0, 0, 4])
sour_preference['Medium'] = fuzz.trimf(sour_preference.universe, [2, 5, 8])
sour_preference['High'] = fuzz.trimf(sour_preference.universe, [6, 10, 10])

# Draw a food recommendation
food_recommendation= ctrl.Consequent(np.arange(0, 10, 0.1), 'food_recommendation')
food_recommendation['light'] = fuzz.trimf(food_recommendation.universe, [0, 0, 4])
food_recommendation['Moderate'] = fuzz.trimf(food_recommendation.universe, [3, 5, 7])
food_recommendation['Heavy'] = fuzz.trimf(food_recommendation.universe, [6, 10, 10])


health_level.view(sim=None)
plt.show()
spicy_preference.view(sim=None)
plt.show()
sweet_preference.view(sim=None)
plt.show()
sour_preference.view(sim=None)
plt.show()
food_recommendation.view(sim=None)
plt.show()


# Writing rules
rule1 = ctrl.Rule(health_level['Poor'] & spicy_preference['High'], food_recommendation['light'])
rule2 = ctrl.Rule(health_level['Poor'] & sweet_preference['High'], food_recommendation['light'])
rule3 = ctrl.Rule(health_level['Poor'] & sour_preference['High'], food_recommendation['light'])
rule4 = ctrl.Rule(health_level['Poor'] & sweet_preference['Low'] & spicy_preference['Low'], food_recommendation['light'])

rule5 = ctrl.Rule(health_level['Medium'] & sweet_preference['High'], food_recommendation['Moderate'])
rule6 = ctrl.Rule(health_level['Medium'] & spicy_preference['Medium'], food_recommendation['Moderate'])
rule7 = ctrl.Rule(health_level['Medium'] & sour_preference['Medium'], food_recommendation['Moderate'])
rule8 = ctrl.Rule(health_level['Medium'] & sweet_preference['Low'] & spicy_preference['Low'], food_recommendation['light'])

rule9 = ctrl.Rule(health_level['Good'] & sweet_preference['High'], food_recommendation['Heavy'])
rule10 = ctrl.Rule(health_level['Good'] & spicy_preference['High'], food_recommendation['Heavy'])
rule11 = ctrl.Rule(health_level['Good'] & sour_preference['High'], food_recommendation['Moderate'])
rule12 = ctrl.Rule(health_level['Good'] & sweet_preference['Medium'] & spicy_preference['Medium'], food_recommendation['Moderate'])
rule13 = ctrl.Rule(health_level['Good'] & sweet_preference['Low'] & spicy_preference['Low'], food_recommendation['light'])

rule14 = ctrl.Rule(health_level['Medium'] & spicy_preference['High'] & sweet_preference['High'], food_recommendation['Heavy'])
rule15 = ctrl.Rule(health_level['Poor'] & spicy_preference['Medium'] & sweet_preference['Medium'], food_recommendation['light'])

#Applying the rules
recommendation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15])
recommendation = ctrl.ControlSystemSimulation(recommendation_ctrl)

# Getting a value from the user
health = float(input("Enter your health level (0 to 100): "))
spicy = float(input("Enter your spicy preference (0 to 10): "))
sweet = float(input("Enter your sweet preference (0 to 10): "))
sour = float(input("Enter your sour preference (0 to 10): "))
# Initializing the inputs of a fuzzy system
recommendation.input['health_level'] = health
recommendation.input['spicy_preference'] = spicy
recommendation.input['sweet_preference'] = sweet
recommendation.input['sour_preference'] = sour
#Run inference
recommendation.compute()
#Display numeric output
print("Food Recommendation Level:", round(recommendation.output['food_recommendation'], 2))
#Graphical display of output
food_recommendation.view(sim=recommendation)
plt.show()
