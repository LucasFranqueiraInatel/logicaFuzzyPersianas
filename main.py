import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada e saída
indoor_light = ctrl.Antecedent(np.arange(-200, 201, 1), 'indoor_light')
outdoor_light = ctrl.Antecedent(np.arange(0, 1101, 1), 'outdoor_light')
blinds = ctrl.Consequent(np.arange(-64, 65, 1), 'blinds')

# Definindo as funções de pertinência para luz interna
indoor_light['poor'] = fuzz.trimf(indoor_light.universe, [-200, -200, -100])
indoor_light['mediocre'] = fuzz.trimf(indoor_light.universe, [-200, -100, 0])
indoor_light['average'] = fuzz.trimf(indoor_light.universe, [-100, 0, 100])
indoor_light['decent'] = fuzz.trimf(indoor_light.universe, [0, 100, 200])
indoor_light['good'] = fuzz.trimf(indoor_light.universe, [100, 200, 200])

# Definindo as funções de pertinência para luz externa
outdoor_light['poor'] = fuzz.trimf(outdoor_light.universe, [0, 0, 550])
outdoor_light['average'] = fuzz.trimf(outdoor_light.universe, [0, 550, 1100])
outdoor_light['good'] = fuzz.trimf(outdoor_light.universe, [550, 550, 1100])

# Definindo as funções de pertinência para posição das persianas
blinds['fc'] = fuzz.trimf(blinds.universe, [-64, -64, -20])
blinds['c'] = fuzz.trimf(blinds.universe, [-40, -20, 0])
blinds['nm'] = fuzz.trimf(blinds.universe, [-10, 0, 10])
blinds['o'] = fuzz.trimf(blinds.universe, [0, 20, 40])
blinds['fo'] = fuzz.trimf(blinds.universe, [20, 64, 64])

# Definindo as regras
rule1 = ctrl.Rule(indoor_light['poor'] & outdoor_light['poor'], blinds['fo'])
rule2 = ctrl.Rule(indoor_light['poor'] & outdoor_light['average'], blinds['fo'])
# Adicione aqui as demais regras...

# Criando o sistema de controle
blinds_ctrl = ctrl.ControlSystem([rule1, rule2])  # Adicione aqui todas as regras
blinds_simulation = ctrl.ControlSystemSimulation(blinds_ctrl)

# Entrando com alguns valores para teste
blinds_simulation.input['indoor_light'] = -150
blinds_simulation.input['outdoor_light'] = 300

# Calculando o resultado
blinds_simulation.compute()

# Exibindo o resultado
print(blinds_simulation.output['blinds'])
blinds.view(sim=blinds_simulation)
