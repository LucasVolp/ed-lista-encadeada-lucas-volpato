class Pilha:
	def __init__(self):
		self.itens = []

	def empilhar(self, item):
		self.itens.append(item)

	def desempilhar(self):
		if not self.vazia():
			return self.itens.pop()
		return None

	def vazia(self):
		return len(self.itens) == 0

class InversorString:
	@staticmethod
	def inverter(palavra):
		pilha = Pilha()
		for char in palavra:
			pilha.empilhar(char)
		invertida = ''
		while not pilha.vazia():
			invertida += pilha.desempilhar()
		return invertida

class VerificadorParenteses:
	@staticmethod
	def balanceado(expressao):
		pilha = Pilha()
		for char in expressao:
			if char == '(': 
				pilha.empilhar(char)
			elif char == ')':
				if pilha.vazia():
					return False
				pilha.desempilhar()
		return pilha.vazia()

if __name__ == "__main__":
	palavra = "ALGORITMO"
	print("Inversão de string:")
	print(f"Entrada: {palavra}")
	print(f"Saída: {InversorString.inverter(palavra)}\n")

	expressoes = [
		"((A+B) * C)",
		"(A+B))",
		"((A+B)"
	]
	print("Verificação de parênteses:")
	for exp in expressoes:
		print(f"Expressão: {exp} -> {'Válido' if VerificadorParenteses.balanceado(exp) else 'Inválido'}")
