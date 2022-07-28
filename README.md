# Inteligencia-Artificial-Jogando-Dino

Aluno> Vitor Berger Bonella

Entrar no diretorio Dino

## Requisitos

Instalar o pytorch seguindo as instruções de acordo com sua maquina https://pytorch.org/get-started/locally/

Instalar o pygad:
```
pip install pygad
```

## Treino

Para treinar e salvar a melhor solução->
```
python dinoIA.py train
```
A cada melhor solução encontrada ela é salva no arquivo best_sol

Existe a opção de enviar uma solução inicial
```
python dinoIA.py train <nome-da-soluçao>
```

## Validação

Para testar os resultados da melhor solução->
```
python dinoIA.py eval best_solution
```
Arquivo best_solution disponivel no repositorio
