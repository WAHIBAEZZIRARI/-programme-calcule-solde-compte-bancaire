class CompteBancaire:
    def __init__(self, identifiant_titulaire, numero_compte, solde):
        self.identifiant_titulaire = identifiant_titulaire
        self.numero_compte = numero_compte
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"{montant} euros ont été déposés. Nouveau solde : {self.solde} euros.")
        else:
            print("Le montant du dépôt doit être supérieur à zéro.")

    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"{montant} euros ont été retirés. Nouveau solde : {self.solde} euros.")
            else:
                print("Fonds insuffisants.")
        else:
            print("Le montant du retrait doit être supérieur à zéro.")


class Client:
    def __init__(self, code_secret, compte_bancaire):
        self.code_secret = code_secret
        self.compte_bancaire = compte_bancaire


class AgentBanque:
    @staticmethod
    def afficher_solde(compte):
        print(f"Solde du compte {compte.numero_compte}: {compte.solde} euros.")

    @staticmethod
    def effectuer_operation(compte, montant, operation):
        if operation == "depot":
            compte.deposer(montant)
        elif operation == "retrait":
            compte.retirer(montant)


# Exemple d'utilisation
compte_client1 = CompteBancaire(identifiant_titulaire="ID123", numero_compte="C1001", solde=1000)
client1 = Client(code_secret="1234", compte_bancaire=compte_client1)

agent = AgentBanque()

# Affichage du solde
agent.afficher_solde(compte_client1)

# Dépôt
agent.effectuer_operation(compte_client1, montant=500, operation="depot")

# Retrait
agent.effectuer_operation(compte_client1, montant=200, operation="retrait")
