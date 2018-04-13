#Clas qui permet de réaliser le lancement de l'analyse via le docker.

import threading
import time
import subprocess
from PyQt5.QtCore import QProcess


class RunDocker (threading.Thread):
    def __init__(self, dico):
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)
        self.etat = False
        self.dico=dico

    def ecrit(self):
        print("Commande terminé")

    def creationCommandeDocker(self):
        #cette liste permet de retourner en premiere valeur une chaine de caractere de la commande :
        # affichage dans generate commande
        # dans une seconde valeur se trouve la liste des arguments pour lancer la commande via un processus bash
        retour = []
        retour.append("docker run docker run -ite DISPLAY --net=host \ \n")

        #liste intermédiaire qui me permet de créer la commande processus pour le lancement du docker
        list_monter=[]

        dossier_sortie=self.dico["dossierS"].strip("\n")+":/"+self.dico["nom"].strip("\n")
        list_monter.append(dossier_sortie)
        retour[0]+="-v "+dossier_sortie+" \ \n"

        dossier_configFile=self.dico["configfiles"].strip("\n")+":/ConfigFiles/"+self.dico["configfiles"].split("/")[-1].strip("\n")
        list_monter.append(dossier_configFile)
        retour[0]+="-v "+dossier_configFile+" \ \n"

        #genome de reference
        genome=""
        genomeList=self.dico["genRef"].split("/")[:-1]
        for cheminGenome in genomeList :
            if cheminGenome != "":
                genome+="/"
                genome+=cheminGenome
        genome+=":/data/Reference_genomes"
        list_monter.append(genome)
        retour[0]+="-v "+genome+" \ \n"

        #reads :
        for nbr in range(self.dico["nbrRead"]):
            #print(self.dico[("read"+str(nbr))])
            read=""
            readList=self.dico[("read"+str(nbr))].strip("\n").split("/")
            #print(readList)
            for cheminRead in readList:
                if cheminRead != "":
                    read+="/"
                    read+=cheminRead
            read+=":/data/reads/"
            read+=self.dico[("read"+str(nbr))].strip("\n").split("/")[-1]
            list_monter.append(read)
            retour[0]+="-v "+read+" \ \n"

        # snepEffDB
        snpEffDB=""
        snpEffDBList=self.dico["SnpEffDB"].strip("\n").split("/")
        for i in snpEffDBList :
            if i != "":
                snpEffDB+="/"
                snpEffDB+=i
        snpEffDB+=":/data/snpEff-Databases/"
        snpEffDB+=self.dico["SnpEffDB"].strip("\n").split("/")[-1]
        list_monter.append(snpEffDB)
        retour[0]+="-v "+snpEffDB+" \ \n"

        #SNPeff config :
        snpEffconf=""
        snpEffconfList=self.dico["SnpEffDBconf"].strip("\n").split("/")
        for i in snpEffconfList :
            if i != "":
                snpEffconf+="/"
                snpEffconf+=i
        snpEffconf+=":/data/snpEff-Databases/"
        snpEffconf+=self.dico["SnpEffDBconf"].split("/")[-1]
        list_monter.append(snpEffconf)
        retour[0]+="-v "+snpEffconf+" \ \n"

        #backgroundGVCF
        backGVCF=self.dico["backgroundGVCF"].strip("\n")
        backGVCF+=":/data/"
        backGVCF+=self.dico["backgroundGVCF"].strip("\n").split("/")[-1]
        list_monter.append(backGVCF)
        retour[0]+="-v "+backGVCF+" \ \n"

        #mapping GVCF
        mappGVCF=self.dico["mappingGVCF"].strip("\n")
        mappGVCF+=":/data/"
        mappGVCF+=self.dico["mappingGVCF"].strip("\n").split("/")[-1]
        list_monter.append(mappGVCF)
        retour[0]+="-v "+mappGVCF+" \ \n"

        #invarscaff
        invarScaff=self.dico["InvarScaf"].strip("\n")
        invarScaff+=":/data/"
        invarScaff+=self.dico["InvarScaf"].strip("\n").split("/")[-1]
        list_monter.append(invarScaff)
        retour[0]+="-v "+invarScaff+" \ \n"

        #warn scaff
        warnScaff=self.dico["warnScaf"].strip("\n")
        warnScaff+=":/data/"
        warnScaff+=self.dico["warnScaf"].strip("\n").split("/")[-1]
        list_monter.append(warnScaff)
        retour[0]+="-v "+warnScaff+" \ \n"

        #dbSNP :
        dbnsp=self.dico["dbSNP"].strip("\n")
        dbnsp+=":/data/"
        dbnsp+=self.dico["dbSNP"].strip("\n").split("/")[-1]
        list_monter.append(dbnsp)
        retour[0]+="-v "+dbnsp+" \ \n"

        #scaff list
        scaflist=self.dico["listScaff"].strip("\n")
        scaflist+=":/data/"
        scaflist+=self.dico["listScaff"].strip("\n").split("/")[-1]
        list_monter.append(scaflist)
        retour[0]+="-v "+scaflist+" \ \n"

        args = []
        args.append('run')
        args.append('-ite')
        args.append('DISPLAY')
        for i in list_monter :
            args.append('-v')
            args.append(i)
        args.append('hermespara/andalusian_mapping:latest')
        retour[0]+="hermespara/andalusian_mapping:latest /bin/bash ./launch.sh"
        retour.append(args)

        return(retour)

    def run(self):
        ## La première étapte est de pull le docker :
        #command = 'docker'
        #args1 = ["pull", "hermespara/andalusian_mapping:juliette"]
        #process1 = QProcess()
        #process1.startDetached(command, args1)

        commande="docker pull hermespara/andalusian_mapping:latest"
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        self.listeConfigFiles=[]
        for line in sortie.stdout:
            self.listeConfigFiles.append(str(line.rstrip()).strip("b'").strip("'"))

        args = self.creationCommandeDocker()

        ## Ensuite on peut runner le docker
        #command= 'docker'
        #process = QProcess()
        #process.startDetached(command, args)

        commande=args[0]
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        self.listeConfigFiles=[]
        for line in sortie.stdout:
            self.listeConfigFiles.append(str(line.rstrip()).strip("b'").strip("'"))

        print(self.listeConfigFiles)


if __name__ == "__main__":
    dico={}
    with open("/home/etudiant/Bureau/Andalusian_mapping/ConfigFiles/testVF_app.py", "r") as fichier_sortie:
        ligne=fichier_sortie.readline()
        while ligne != "":
            ligne=ligne.split("=")
            try:
                dico[ligne[0]]=int(ligne[1])
            except:
                dico[ligne[0]]=ligne[1]
            ligne=fichier_sortie.readline()

    #print(dico)
    #print(dico["SnpEffDB"])

    docker=RunDocker(dico)
    docker.start()

    print("--------FINI----------")
