from regle import Regle

class BaseFaits:
    def __init__(self, liste_faits):
        self.faits = liste_faits

    def ajout_fait(self, regle):
        if regle.verif(self.faits):
            for alors in regle.alors:
                self.faits.append(alors)
