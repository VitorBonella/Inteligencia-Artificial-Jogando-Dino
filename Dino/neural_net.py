from torch import relu
import torch.nn
import pygad

input_layer = torch.nn.Linear(6, 13)
relu_layer = torch.nn.ReLU()
middle_layer = torch.nn.Linear(13,13)
#last_layer = torch.nn.Linear(12,6)
output_layer = torch.nn.Linear(13,1)
sigmoid_layer = torch.nn.Sigmoid()

model = torch.nn.Sequential(input_layer,
                            relu_layer,
                            middle_layer,
                            relu_layer,
                            output_layer,
                            sigmoid_layer)

import pygad.torchga

torch_ga = pygad.torchga.TorchGA(model=model,
                                num_solutions=55)

def on_generation(ga_instance):
    file = open("generations.txt",mode='a')
    file.write("Generation = {generation}\n".format(generation=ga_instance.generations_completed))
    file.write("Fitness    = {fitness}\n\n".format(fitness=ga_instance.best_solution(ga_instance.last_generation_fitness)[1]))
    file.close()
    