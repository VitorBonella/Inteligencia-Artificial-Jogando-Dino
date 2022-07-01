import tensorflow
import pygad.kerasga
import pygad
from tqdm import tqdm

input_layer = tensorflow.keras.layers.Input(3)
neurons_layer = tensorflow.keras.layers.Dense(4,activation='relu')(input_layer)
output_layer = tensorflow.keras.layers.Dense(3,activation='softmax')(neurons_layer)

net = tensorflow.keras.Model(inputs=input_layer,outputs=output_layer)

net_genetic_alg = pygad.kerasga.KerasGA(model=net,num_solutions = 15)

def on_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution(ga_instance.last_generation_fitness)[1]), end='\n\n')