# -*- coding: utf-8 -*-

# Classe permettant le remplisage du fichier de config nécéssaire au lancement du pipeline
# Dans un premier temps tout les champs sont stocké dans un dictionnaire
# Puis le fichier texte est créer avec des vérification des champs.

import datetime

class Formulaire():
    def __init__(self):
        #Dossier des fichier de config -> nom ajouter au moment du nexte de la première page du formulaire
        self.fichier_config="/home/etudiant/Bureau/Andalusian_mapping/ConfigFiles/"
        self.dico = {}
        self.listeChamps=["backgroundGVCF","mappingGVCF","SnpEffDBconf","SnpEffDB","dossierS","nom","genRef","plateforme","sample","dbSNPbool","library","rgid","rgpu","backStrainId","mappStrainId", "referenced"]
        for clef in self.listeChamps:
            self.dico[clef]=""

    def etape1(self, genRef, nbrRead, listRead, nom, ram, dossierS):
        self.dico["genRef"]=genRef.strip("\n").strip(" ")
        self.dico["nbrRead"]=nbrRead
        self.dico["nom"]=str(nom).strip("\n").strip(" ")
        self.dico["ram"]=ram.strip("\n").strip(" ")
        self.dico["dossierS"]=dossierS.strip("\n").strip(" ")
        self.fichier=nom
        self.fichier+="_config.py"

        self.dico["READS"]=listRead
        for i in range(len(listRead)):
            read="read"
            read+=str(i)
            self.dico[read]=listRead[i].strip("\n").strip(" ")

    def etape2(self, plateforme, sample, Library, rgid, rgpu,SnpEffDB,SnpEffDBconf):
        self.dico["plateforme"]=plateforme.strip("\n").strip(" ")
        self.dico["sample"]=sample.strip("\n").strip(" ")
        self.dico["library"]=Library.strip("\n").strip(" ")
        self.dico["rgid"]=rgid.strip("\n").strip(" ")
        self.dico["rgpu"]=rgpu.strip("\n").strip(" ")
        self.dico["SnpEffDB"]=SnpEffDB.strip("\n").strip(" ")
        self.dico["SnpEffDBconf"]=SnpEffDBconf.strip("\n").strip(" ")

    def etape3(self,backStrainID, Referenced, MappStrainId, dbsnp, dbSNPbool, backgroundGVCF, mappingGVCF):
        self.dico["backStrainId"]=backStrainID.strip("\n").strip(" ")
        try:
            self.dico["referenced"]=Referenced.strip("\n").strip(" ")
        except:
            self.dico["referenced"]=Referenced
        try :
            self.dico["dbSNPbool"]=dbSNPbool.strip("\n").strip(" ")
        except:
            self.dico["dbSNPbool"]=dbSNPbool
        self.dico["mappStrainId"]=MappStrainId.strip("\n").strip(" ")
        self.dico["dbSNP"]=dbsnp.strip("\n").strip(" ")
        self.dico["backgroundGVCF"]=backgroundGVCF.strip("\n").strip(" ")
        self.dico["mappingGVCF"]=mappingGVCF.strip("\n").strip(" ")

    def etape4(self, listScaff, InvarScaf, warnScaf):
        self.dico["listScaff"]=listScaff.strip("\n").strip(" ")
        self.dico["InvarScaf"]=InvarScaf.strip("\n").strip(" ")
        self.dico["warnScaf"]=warnScaf.strip("\n").strip(" ")

    def setFichier(self, fichier):
        self.fichier=fichier

    def remplisConfig(self, fichier):
        with open(fichier, "w") as fichier_sortie:
            for clef in self.dico:
                s=clef
                s+="="
                s+=str(self.dico[clef])
                s+="\n"
                fichier_sortie.write(s)

    def remplisDico(self, fichier):
        with open(fichier, "r") as fichier_sortie:
            ligne=fichier_sortie.readline()
            while ligne != "":
                ligne=ligne.split("=")
                try:
                    self.dico[ligne[0]]=int(ligne[1])
                except:
                    self.dico[ligne[0]]=ligne[1]
                ligne=fichier_sortie.readline()

    def remplisConfigDocker(self,fichier):
        with open(fichier, "w") as fichier_sortie:
            fichier_sortie.write("nbRun = 1\n")
            fichier_sortie.write("readID = '"+self.dico["nom"]+"'\n")
            #PATH
            # read -> enlever \n et ne laisser que le nom des fichiers ici
            l=[]
            for nom_read in self.dico["READS"]:
                l.append("/data/reads/"+nom_read.strip("\n").split("/")[-1])
            fichier_sortie.write("READS = "+str(l)+"\n")
            genRef=self.dico["genRef"].split("/")[-1]
            fichier_sortie.write("REFERENCE = '/data/Reference_genomes/"+genRef+"'\n")
            fichier_sortie.write("RAM = "+self.dico["ram"]+"\n")
            fichier_sortie.write("RGPL = '"+self.dico["plateforme"]+"'\n")
            fichier_sortie.write("RGSM = '"+self.dico["sample"]+"'\n")
            fichier_sortie.write("RGLB = '"+self.dico["library"]+"'\n")
            fichier_sortie.write("RGID = '"+self.dico["rgid"]+"'\n")
            fichier_sortie.write("RGPU = '"+self.dico["rgpu"]+"'\n")
            fichier_sortie.write("dbSNP = '/data/"+self.dico["dbSNP"].split("/")[-1]+"'\n")
            fichier_sortie.write("SCAFF_SIZE = '/data/"+self.dico["listScaff"].split("/")[-1]+"'\n")
            fichier_sortie.write("INVARIANT_SCAFF = '/data/"+self.dico["InvarScaf"].split("/")[-1]+"'\n")
            fichier_sortie.write("BACKGROUND_GVCF = '/data/"+self.dico["backgroundGVCF"].split("/")[-1]+"'\n")
            fichier_sortie.write("MAPPING_GVCF = '/data/"+self.dico["mappingGVCF"].split("/")[-1]+"'\n")
            fichier_sortie.write("snpEff_database = '"+self.dico["SnpEffDB"].split("/")[-1]+"'\n")
            fichier_sortie.write("snpEff_contig = '/data/snpEff-Databases/"+self.dico["SnpEffDBconf"].split("/")[-1]+"'\n")
            fichier_sortie.write("Warning_Scaff = '/data/"+self.dico["warnScaf"].split("/")[-1]+"'\n")
            fichier_sortie.write("Mapping_strain = '"+self.dico["mappStrainId"]+"'\n")
            fichier_sortie.write("Background_strain = '"+self.dico["backStrainId"]+"'\n")
            fichier_sortie.write("picard = '/software/picard.jar'\n")
            fichier_sortie.write("GATK = '/software/GenomeAnalysisTK.jar'\n")
            fichier_sortie.write("snpEff = '/software/snpEff/snpEff.jar'\n")
            fichier_sortie.write("snpEff_pl = '/software/snpEff/scripts/vcfEffOnePerLine.pl'\n")
            fichier_sortie.write("snpEff_SnpSift = '/software/snpEff/SnpSift.jar'\n")

    def setListe(self,listCongif, fichier):
        with open(fichier, "w") as fichierS:
            for i in listCongif :
                if i == self.dico["nom"]:
                    fichierS.write("*"+i+"_docker.py\n")
                else:
                    fichierS.write(i+"_docker.py\n")
