import tensorflow
import pygad.kerasga
import pygad

input_layer = tensorflow.keras.layers.Input(3)
neurons_layer = tensorflow.keras.layers.Dense(4,activation='relu')(input_layer)
output_layer = tensorflow.keras.layers.Dense(2,activation='relu')(neurons_layer)

net = tensorflow.keras.Model(inputs=input_layer,outputs=output_layer)

net_genetic_alg = pygad.kerasga.KerasGA(model=net,num_solutions = 15)

def on_generation(ga_instance):
    file = open("generations.txt",mode='a')
    file.write("Generation = {generation}\n".format(generation=ga_instance.generations_completed))
    file.write("Fitness    = {fitness}\n\n".format(fitness=ga_instance.best_solution(ga_instance.last_generation_fitness)[1]))
    file.close()
    score = ga_instance.best_solution(ga_instance.last_generation_fitness)[1]