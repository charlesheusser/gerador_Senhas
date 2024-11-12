import string
import random

def gerar_Senha(tamanho):
    if tamanho < 6:
        print("O tamanho da senha deve ser maior que 6")
    
    else:
        senha = [
            random.choice(string.ascii_letters),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        possibilidades = ''.join([string.ascii_letters, string.digits, string.punctuation])
        senha.extend(random.choices(possibilidades, k=tamanho-3))

        random.shuffle(senha)
        return ''.join(senha)