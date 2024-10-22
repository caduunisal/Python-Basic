class Chatbot():
    def __init__(self, nome):
        print(f"Bem vindo ao Chatbot, {nome.title()}!")
        
    def fala(self):
        print("Oi")
    
    def sai(self):
        print("Tchau!")
    
a = Chatbot("carlos")
a.fala()
a.sai()


