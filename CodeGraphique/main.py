# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import subprocess
import time

import ClassFormulaire
import classFolder
import classFiles
import ClassTache1RunDocker

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ######################################################################
        #                                                                    #
        #      Fenetre princiale (menu gauche + scroll bar area vide)        #
        #                                                                    #
        ######################################################################

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 500)
        MainWindow.setWindowTitle("Andalusian Mapping")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 344))
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 400))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_titre = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_titre.setFont(font)
        self.label_titre.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_titre.setAcceptDrops(False)
        self.label_titre.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.label_titre.setObjectName("label_titre")
        self.gridLayout_2.addWidget(self.label_titre, 0, 0, 1, 1)
        self.pushButton_acceuil = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_acceuil.setObjectName("pushButton_acceuil")
        self.gridLayout_2.addWidget(self.pushButton_acceuil, 1, 0, 1, 1)
        self.pushButton_newAnalyse = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_newAnalyse.setObjectName("pushButton_newAnalyse")
        self.gridLayout_2.addWidget(self.pushButton_newAnalyse, 2, 0, 1, 1)
        self.pushButton_oldAnalise = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_oldAnalise.setObjectName("pushButton_oldAnalise")
        self.gridLayout_2.addWidget(self.pushButton_oldAnalise, 3, 0, 1, 1)
        self.pushButton_resultat = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_resultat.setObjectName("pushButton_resultat")
        self.gridLayout_2.addWidget(self.pushButton_resultat, 4, 0, 1, 1)
        self.pushButton_author = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_author.setObjectName("pushButton_author")
        self.gridLayout_2.addWidget(self.pushButton_author, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Signal et connection des boutons d'acceil
        self.pushButton_acceuil.clicked.connect(self.buttonClicked_acceuil)
        self.pushButton_oldAnalise.clicked.connect(self.buttonClicked_reFormualire)
        self.pushButton_author.clicked.connect(self.buttonClicked_author)
        self.pushButton_newAnalyse.clicked.connect(lambda: self.buttonClicked_newAnalyse("nouvelle analyse"))

        #variable qui gère le nombre de fichier de lecture (read) de l'analyse courante.
        self.nbr=2

        #variable qui gère la provenance lors du lancement de la fonction qui gère la première page du formulaire
        #Permet de gérer le comportement du dictionnaire.
        self.indication="Rien"

        #dossier d'instalation pour l'organisatio des fichiers
        commande="pwd "
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        self.dossierCourant=[]
        for line in sortie.stdout:
            self.dossierCourant.append(str(line.rstrip()).strip("b'").strip("'"))

        a=self.dossierCourant[0]+"/"
        a=a.split("/")
        a=a[:-2]

        print(a)


        self.PATH=""
        for chemin in a:
            self.PATH+=chemin
            self.PATH+="/"

        print(self.PATH)

        #Dossier ou sont regrouper les fichiers de config
        self.dossierConfig=self.PATH+"ConfigFiles/"
        print(self.dossierConfig)



        self.buttonClicked_acceuil()

    def buttonClicked_author(self):
        print("acceuil")
        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label1_etape = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label1_etape.setMaximumSize(QtCore.QSize(16777215, 500))
        self.label1_etape.setMinimumSize(QtCore.QSize(16777215, 500))
        self.label1_etape.setObjectName("label_etape")
        self.label1_etape.setText("This software is developped by : \n\n\n- Juliette GEOFFRAY \n- Eric CUMUNEL \n- Hermes PARAQINDES \n\n We are three students at Master 1 Molecular Bio-Informatic of Claude Bernard Lyon 1 University (UCBL) \n\n\nThe original pipeline is developped and maintained by Fabrice BESNARD, researcher at the Ecole Normale Superieure de Lyon (ENS)")
        self.label1_etape.setWordWrap(True)
        self.gridLayout_3.addWidget(self.label1_etape, 0, 0, 1, 1)

    def buttonClicked_acceuil(self):
        print("acceuil")
        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label1_etape = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label1_etape.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setItalic(True)
        self.label1_etape.setFont(font)
        self.label1_etape.setObjectName("label_etape")
        self.label1_etape.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#000000;\">Andalusian Mapping</span></p></body></html>")
        self.gridLayout_3.addWidget(self.label1_etape, 0, 0, 1, 1)

        '''self.label_titre_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        #font.setFamily("Latin Modern Mono")
        font.setPointSize(26)
        self.label_titre_2.setFont(font)
        self.label_titre_2.setObjectName("label_titre_2")
        self.label_titre.setText("<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>")
        self.gridLayout_3.addWidget(self.label_titre_2, 1, 0, 1, 1)'''

        self.label_etape = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setItalic(True)
        self.label_etape.setFont(font)
        self.label_etape.setObjectName("label_etape")
        self.label_etape.setText("<html><head/><body><p><span style=\"font-size:14pt; font-weight:600; font-style:normal; color:#ff0000;\">General description</span></p></body></html>")
        self.gridLayout_3.addWidget(self.label_etape, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setText('<html><head/><body><p align=\"justify\">This pipeline has been originally developped for the nematode species <span style=\" font-style:italic;\">Oscheius tipulae</span> by the <a href=\"http://www.ibens.ens.fr/?rubrique29\"><span style=\" text-decoration: underline; color:#0000ff;\">Félix lab</span></a>. This repository contains all data to perform mapping-by-sequencing with Oscheius tipulae using the reference strain CEW1 and the mapping strain JU170 (see Félix Lab <a href=\"http://www.justbio.com/worms/index.php\"><span style=\" text-decoration: underline; color:#0000ff;\">Strain database</span></a>). However, this is a versatile pipeline that allows working with any species and any mapping strains (Read below &quot;How to adapt it to my purpose ?&quot;).</p><p align=\"justify\"><span style=\" font-weight:600;\">Andalusian_Mapping</span> is mainly encoded in bash and it can be run on Linux (tested on Ubuntu 16.04 LTS) and MacOS (not Windows). It uses popular third-party NGS softwares (six exactly, see &quot;Requirements&quot;) that must be installed in the computing machine.</p><p align=\"justify\">Many bio-informatic steps are needed from the raw sequencing data to the final identification of candidate mutations. <span style=\" font-weight:600;\">Andalusian_Mapping</span> allows pipelining them all via one simple command line. This pipeline can then be used routinely with very basic knowledge in shell coding.</p></body></html>')
        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; font-style:normal; color:#ff0000;\">Why using Andalusian Mapping ?</span></p></body></html>")
        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setText('<html><head/><body><p>Recently, <a href=\"https://usegalaxy.org/u/gm2123/p/cloudmap\"><span style=\" text-decoration: underline; color:#0000ff;\">Cloudmap</span></a>, a nice automatic pipeline of mapping-by-sequencing/mutant-identification has been developped and integrated to Galaxy, with an intuitive and user-friendly GUI. It works very well with model species like <span style=\" font-style:italic;\">Caenorhabditis elegans</span> or <span style=\" font-style:italic;\">Arabidopsis thaliana</span>. However, all genomes are not available in Galaxy. We had to develop Anadalousian-Mapping to work with the non-model species <span style=\" font-style:italic;\">Oscheius tipulae</span>, which had no published genome. But we tried to keep simple procedures so that a large audience of biologists (and not only bio-informaticians) could find it useful.</p><p>We propose that <span style=\" font-weight:600;\">Andalusian-Mapping</span> will be an attractive alternative to other pipelines for people who need to work with non-reference genome assembly but with minimal efforts in computing/bio-informatics. Once the set-up is done, the procedure is really simple: one command line only.</p><p>Here are some advantages of <span style=\" font-weight:600;\">Andalusian-Mapping</span> that may match your needs:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Most third-party software easy to install and so popular that they might already be on your system (e.g. R, bwa, samtools) ;</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The most complicated software to install are GATK and snpEff but they both have very clear tutorials and debug forum online. If it remains a problem for you, any people with intermediate computing skills should easily and quickly debug this step for you ;</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Once the set-up is done, the procedure is really simple: one command line only ;</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can run it locally and don\'t need to queue your job in a distant server ;</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can adapt it to any reference genomes. Hence, you can study non-model organisms or use an alternative assembly of a model-organism (different strain depedning on the design of your mapping cross).</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You manage the versions of your software: you can either benefit from the latest improvements of third-party software or freeze you set-up in the configuration you prefer.</li></ul></body></html>')
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                                                                    #
        #                      RELANCER ANALYSE                              #
        #                                                                    #
        ######################################################################

        ######################################################################
        #               1er page -> liste des analyse existante              #
        ######################################################################

        # Liste des analyses existante et selection possible de l'une d'entre elle

    def buttonClicked_reFormualire(self):
        print("Relancer une analyse")

        self.scrollArea.hide()

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        #Liste des fichiers config deja créer :
        commande="ls "
        commande+=self.dossierConfig
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        self.listeConfigFiles=[]
        for line in sortie.stdout:
            self.listeConfigFiles.append(str(line.rstrip()).strip("b'").strip("'"))

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 4, 0, 1, 1)
        self.label_NAtitre = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_NAtitre.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_NAtitre.setObjectName("label_NAtitre")
        self.label_NAtitre.setText("<html><head/><body><p><center><span style=\" font-size:12pt; font-weight:600;\">Load a previous analysis :</span></center></p></body></html>")
        self.gridLayout_3.addWidget(self.label_NAtitre, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.listeConfigFiles_trier=[]
        for i in range(len(self.listeConfigFiles)):
            if len(self.listeConfigFiles[i].split("_")) >1 and self.listeConfigFiles[i].split("_")[1] == "app.py":
                self.listeConfigFiles_trier.append(self.listeConfigFiles[i].split("_")[0])

        self.label=[]
        for i in range(len(self.listeConfigFiles_trier)):
            self.label.append("label_{0}".format(i))

        #affiche une liste de bouton radio en focntion du nombre de fichier de config présent
        #et met en texte du bouton radio le nom de l'analyse.
        for i in range(len(self.listeConfigFiles_trier)):
            self.label[i] = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
            self.label[i].setObjectName("label")
            self.label[i].setText(self.listeConfigFiles_trier[i])
            self.label[i].setMaximumSize(QtCore.QSize(16777215, 20))
            self.gridLayout_3.addWidget(self.label[i], 1+i, 0, 1, 1)

        #print(self.label[i])

        self.pushButton_NAok = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_NAok.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_NAok.setObjectName("pushButton_NAok")
        self.pushButton_NAok.setText("ok")
        self.horizontalLayout_2.addWidget(self.pushButton_NAok)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 50, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(378, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_NAok.clicked.connect(self.buttonClicked_okReform)

        ######################################################################
        #         intermédiaire pour voir quelle bouton est cliquer          #
        ######################################################################

    def buttonClicked_okReform(self, fichier):
        fic=self.PATH+"/ConfigFiles/"
        for i in range(len(self.label)) :
            if self.label[i].isChecked():
                fic+=self.listeConfigFiles_trier[i]
                fic+="_app.py"
                #print(fic)
                self.buttonClicked_newAnalyse("fichierConfigue", fichier=fic)

        ######################################################################
        #                                                                    #
        #                          ANALYSE                                   #
        #                                                                    #
        ######################################################################

        ######################################################################
        #                   Affichage exécution pipeline                     #
        ######################################################################

    def updatePageExPipeline (self, texte_etape, nombre_pragressBarre):
        print("update de la fenetre")

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_titre_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_titre_2.setObjectName("label_titre_2")
        self.label_titre_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Running pipeline : </span></p></body></html>")
        self.gridLayout_3.addWidget(self.label_titre_2, 0, 0, 1, 1)

        self.label_etape = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape.setObjectName("label_etape")
        label="<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e84d50;\">"
        label+=texte_etape
        label+="</span></p></body></html>"
        self.label_etape.setText(label)
        self.gridLayout_3.addWidget(self.label_etape, 1, 0, 1, 1)

        self.progressBar = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar.setProperty("value", nombre_pragressBarre)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setFormat("%p%")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #               formualire end -> lance l'analyse                    #
        ######################################################################

    def RunAnalysis(self):
        print("Run Analysis")

        # Chope les textes des champs précédant
        listScaff=self.lineEdit_listScaff.text()
        InvarScaf=self.lineEdit_InvarScaf.text()
        warnScaf=self.lineEdit_warnScaf.text()
        #scaffSize=self.lineEdit_scaffSize.text()
        scaffSize=""
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        self.new.dico["configfiles"]=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_docker.py"
        self.new.etape4(listScaff, InvarScaf, warnScaf)
        cheminF=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_app.py"
        self.new.remplisConfig(cheminF)
        chemin=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_docker.py"

        self.new.remplisConfigDocker(chemin)
        cheminFic=self.PATH+"ConfigFiles/list.txt"

        commande="ls "
        commande+=self.dossierConfig
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        self.listeConfigFiles=[]
        for line in sortie.stdout:
            self.listeConfigFiles.append(str(line.rstrip()).strip("b'").strip("'"))

        self.listeConfig=[]
        for i in range(len(self.listeConfigFiles)):
            if len(self.listeConfigFiles[i].split("_")) >1 and self.listeConfigFiles[i].split("_")[1] == "app.py":
                self.listeConfig.append(self.listeConfigFiles[i].split("_")[0])

        self.new.setListe(self.listeConfig, cheminFic)
        #"/home/etudiant/Bureau/Andalusian_mapping/ConfigFile/testecritfichier.py"

        ### Docker test avec un echo toute les 30s ecrit dans un fichier
        #docker=ClassTache1RunDocker.RunDocker(self.new.dico)
        #docker.start()

        script = False
        listeEtape=[]
        lecturefic=0

        #while lecturefic == 0:
         #   try:
         #       with open("/home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt", "r") as fichier:
         #           ligne=fichier.readline()
         #           listeEtape=ligne.strip("\n").split("_")
         #           print(listeEtape)
         #           lecturefic = 1
         #   except:
         #       pass

        listeEnCours=[]

        QtWidgets.QApplication.processEvents()
        i=0
        #while script == False:
                #with open("/home/etudiant/Bureau/Projet/ProjetS2/testDocker/files.txt", "r") as fichier:
                #    ligne=fichier.readline()
                #    ligne=fichier.readlines()
                #for i in range(len(ligne)):
                #    ligne[i]=ligne[i].strip("\n")
                #if ligne != listeEnCours and len(ligne) != 0:
                #    listeEnCours=ligne
                #    self.updatePageExPipeline(ligne)
                #    if listeEnCours[len(ligne)-1] == listeEtape[len(listeEtape)-2]:
                #        script=True

        self.updatePageExPipeline("Running pipeline",0)

        for i in range(10):
            if not i % 1:  # let application process events each 1 steps.
                QtWidgets.QApplication.processEvents()
            nombre=(i+1)*10
            texte=str(i+1)
            texte+=" of 10 steps ("
            texte+=str(nombre)
            texte+="%) done"
            self.updatePageExPipeline(texte,nombre)
            i+=1
            time.sleep(0.5)

        self.results()

    def results(self):
        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_titre_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_titre_2.setObjectName("label_titre_2")
        self.label_titre_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">Results</span></p></body></html>")
        self.gridLayout_3.addWidget(self.label_titre_2, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                                                                    #
        #                          FORMULAIRE                                #
        #             4 étapes + étape de vérification de champs             #
        ######################################################################

        ######################################################################
        #               fenetre info si champs pas valide                    #
        ######################################################################

    def buttonClicked_newAnalyse_probleme(self, chaineCara):
        print("Warning : ")
        # Chope les textes des champs précédant
        listScaff=self.lineEdit_listScaff.text()
        InvarScaf=self.lineEdit_InvarScaf.text()
        warnScaf=self.lineEdit_warnScaf.text()
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        self.new.etape4(listScaff, InvarScaf, warnScaf)

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(80, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../sign-warning-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("This information are emppty : {0} \n".format(chaineCara))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 2, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Ok")
        self.pushButton.clicked.connect(self.buttonClicked_newAnalyse_etape4)
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 4, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                      fenetre ouvrir fichier                        #
        ######################################################################

    #Cette fonction permet d'ouvrir la fénêtre du gestionnaire de fichier
    #et si un fichier est sélectionner de le récupere et remplir la champs de saisie
    #associé (variable le passer en paramètre).
    #Attention : si pluieurs fihiers sont sélectionner, seul le premier renseigner
    #sera pris en compte.
    def ouvrir_fichier(self, le):
        win = classFiles.App()
        if win.nomFichier != "":
            le.setText(win.nomFichier[0])

    def ouvrir_dossier(self, le):
        win = classFolder.App()
        if win.nomFichier != "":
            le.setText(win.nomFichier)

    def buttonClicked_generateCommand(self):
        # Chope les textes des champs précédant
        listScaff=self.lineEdit_listScaff.text()
        InvarScaf=self.lineEdit_InvarScaf.text()
        warnScaf=self.lineEdit_warnScaf.text()
        #scaffSize=self.lineEdit_scaffSize.text()
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        if self.new.dico["nom"] == "":
            self.new.dico["nom"]="Empty"
        self.new.dico["configfiles"]=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_docker.py"
        self.new.etape4(listScaff, InvarScaf, warnScaf)
        cheminF=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_app.py"
        self.new.remplisConfig(cheminF)
        chemin=self.PATH+"ConfigFiles/"+self.new.dico["nom"]+"_docker.py"

        self.new.remplisConfigDocker(chemin)
        cheminFic=self.PATH+"ConfigFiles/list.txt"

        docker=ClassTache1RunDocker.RunDocker(self.new.dico)
        commande = docker.creationCommandeDocker()

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_NAtitre = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_NAtitre.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_NAtitre.setObjectName("label_NAtitre")
        self.label_NAtitre.setText("<html><head/><body><p align=\"center\">Command for run the docker :</p></body></html>")
        self.gridLayout_3.addWidget(self.label_NAtitre, 0, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_NAok = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_NAok.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_NAok.setObjectName("pushButton_NAok")
        self.pushButton_NAok.setText("Ok")
        self.pushButton_NAok.clicked.connect(self.buttonClicked_acceuil)
        self.horizontalLayout_2.addWidget(self.pushButton_NAok)
        self.gridLayout_3.addWidget(self.pushButton_NAok, 6, 0, 1, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.label.setText("Selection : Ctrl +A")
        self.gridLayout_3.addWidget(self.label, 3, 0, 1, 1)

        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 300))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText(commande[0])
        self.gridLayout_3.addWidget(self.textEdit, 5, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        ######################################################################
        #                      Formulaire - Etape 4                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape4(self):
        print("etape 4 formulaire")

        # Chope les textes des champs précédant
        backStrainID=self.lineEdit_backStrainId.text()
        mappStrainId=self.lineEdit_mappStrainId.text()
        dbSNP=self.lineEdit_dbsnp.text()
        backgroundGVCF=self.lineEdit_BGGVCF.text()
        mappingGVCF=self.lineEdit_MGVCF.text()

        if self.radioButton_yesRef.isChecked():
            referenced=0
        elif self.radioButton_noRef.isChecked():
            referenced=1
        else:
            referenced=""

        if self.radioButton_yesRef_bis.isChecked():
            dbSNPbool=0
        elif self.radioButton_noRef_bis.isChecked():
            dbSNPbool=1
        else:
            dbSNPbool=""

        # On les sauvegarde dans le dictionnaire qui gènre les champs
        self.new.etape3(backStrainID, referenced, mappStrainId, dbSNP,dbSNPbool,backgroundGVCF,mappingGVCF)
        #print(self.new.dico)

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_etape4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape4.setObjectName("label_etape4")
        self.label_etape4.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Step 4 of 4</span></p></body></html>")

        self.gridLayout_2.addWidget(self.label_etape4, 0, 0, 1, 1)
        self.label_titre4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre4.setObjectName("label_titre4")
        self.label_titre4.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Additionnal files</span></p></body></html>")

        self.gridLayout_2.addWidget(self.label_titre4, 1, 0, 1, 1)

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")

        self.label_listScaff = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_listScaff.setObjectName("label_listScaff")
        self.label_listScaff.setText("Scaffolds list ID :                          ")

        self.horizontalLayout_18.addWidget(self.label_listScaff)

        self.lineEdit_listScaff = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_listScaff.setText("")
        self.lineEdit_listScaff.setObjectName("lineEdit_listScaff")

        if "listScaff" in self.new.dico.keys():
            if self.new.dico["listScaff"] != "":
                self.lineEdit_listScaff.setText(self.new.dico["listScaff"])

        self.horizontalLayout_18.addWidget(self.lineEdit_listScaff)

        self.toolButton_listScaff = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_listScaff.setObjectName("toolButton_listScaff")
        self.toolButton_listScaff.setText("...")
        self.toolButton_listScaff.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_listScaff))

        self.horizontalLayout_18.addWidget(self.toolButton_listScaff)

        self.gridLayout_2.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_InvarScaf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_InvarScaf.setObjectName("label_InvarScaf")
        self.label_InvarScaf.setText("\"Invariant\" Scaffolds :                      ")

        self.horizontalLayout_11.addWidget(self.label_InvarScaf)

        self.lineEdit_InvarScaf = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_InvarScaf.setText("")
        self.lineEdit_InvarScaf.setObjectName("lineEdit_InvarScaf")

        if "InvarScaf" in self.new.dico.keys():
            if self.new.dico["InvarScaf"] != "":
                self.lineEdit_InvarScaf.setText(self.new.dico["InvarScaf"])

        self.horizontalLayout_11.addWidget(self.lineEdit_InvarScaf)

        self.toolButton_InvarScaf = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_InvarScaf.setObjectName("toolButton_InvarScaf")
        self.toolButton_InvarScaf.setText("...")
        self.toolButton_InvarScaf.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_InvarScaf))

        self.horizontalLayout_11.addWidget(self.toolButton_InvarScaf)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.label_17.setToolTip("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">list of scaffolds you want to test even if they are not linked to your mutation. (e.g. False-positive or so-far-unlinked scaffolds)</span></p></body></html>")
        self.label_17.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_warnScaf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_warnScaf.setObjectName("label_warnScaf")

        self.horizontalLayout_13.addWidget(self.label_warnScaf)

        self.lineEdit_warnScaf = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_warnScaf.setText("")
        self.lineEdit_warnScaf.setObjectName("lineEdit_warnScaf")

        if "warnScaf" in self.new.dico.keys():
            if self.new.dico["warnScaf"] != "":
                self.lineEdit_warnScaf.setText(self.new.dico["warnScaf"])

        self.label_warnScaf.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.label_warnScaf.setText("Warning Scaffolds :                       ")

        self.horizontalLayout_13.addWidget(self.lineEdit_warnScaf)

        self.toolButton_warnScaf = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_warnScaf.setObjectName("toolButton_warnScaf")
        self.toolButton_warnScaf.setText("...")
        self.toolButton_warnScaf.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_warnScaf))

        self.horizontalLayout_13.addWidget(self.toolButton_warnScaf)

        self.gridLayout_2.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_back4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back4.setObjectName("pushButton_back4")
        self.pushButton_back4.setText("Back")
        self.pushButton_back4.clicked.connect(self.buttonClicked_newAnalyse_etape3)

        self.horizontalLayout.addWidget(self.pushButton_back4)

        #------------------
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_com = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_com.setObjectName("pushButton_com")
        self.pushButton_com.setText("Generate command")
        self.pushButton_com.clicked.connect(self.buttonClicked_generateCommand)

        self.horizontalLayout.addWidget(self.pushButton_com)
        #------------------
        spacerItem1 = QtWidgets.QSpacerItem(4000, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        self.pushButton_runAnalysis = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runAnalysis.setMinimumSize(QtCore.QSize(116, 0))
        self.pushButton_runAnalysis.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_runAnalysis.setSizeIncrement(QtCore.QSize(1, 1))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_runAnalysis.setPalette(palette)
        self.pushButton_runAnalysis.setObjectName("pushButton_runAnalysis")
        self.pushButton_runAnalysis.setText("Run Analysis")

        #Vérification des champs :
        #Pour l'instant sur les champs sont vide alors cela retourne un erreur,
        #A voir pour améliorer en fonction des extention du fichier que l'on s'attent
        # a avoir. Si c'est un VCF par exemple : spliter par "." et récupere la deuxieme
        #valeurs pour verrifier qu'elle est bien égale a vcf.
        ChampsOk=0
        infoErr="\n\n"
        for champs in self.new.listeChamps:
            if self.new.dico[champs] == "" :
                ChampsOk=1
                if champs == "nom" :
                    infoErr+="- Analysis name\n"
                if champs == "backgroundGVCF" :
                    infoErr+="- Background GVCF\n"
                if champs == "mappingGVCF" :
                    infoErr+="- Mapping GVCF\n"
                if champs == "SnpEffDBconf" :
                    infoErr+="- SnpEff config file\n"
                if champs == "SnpEffDB" :
                    infoErr+="- SnpEff data base\n"
                if champs == "dossierS" :
                    infoErr+="- Output folder\n"
                if champs == "genRef" :
                    infoErr+="- Reference genome\n"
                if champs == "plateforme" :
                    infoErr+="- platform\n"
                if champs == "backStrainId" :
                    infoErr+="- Back Strain Id\n"
                if champs == "mappStrainId" :
                    infoErr+="- Mapping StrainId\n"

        #pour les read on vérifie pour tous qu'il ne soit pas vide.
        for i in range(self.new.dico["nbrRead"]):
            read="read"
            read+=str(i)
            if self.new.dico[read] == "" :
                ChampsOk=1
                infoErr+="- read {0}\n".format(i)


        #On regarde en fonction de la valeur dbSNPbool si le Champs
        # dbSNP doit être remplis ou non puis on vérifie qu'il le soit.
        if self.new.dico["dbSNPbool"] == 0 :
            if self.new.dico["dbSNP"] == "" :
                ChampsOk=1
                infoErr+="- {0}\n".format(champs)

        #Si tout les champs sont valide on lance l'analyse :
        if ChampsOk == 0 :
            self.pushButton_runAnalysis.clicked.connect(self.RunAnalysis)
        else :
            #pop up avec les champs qui pose probleme
            self.pushButton_runAnalysis.clicked.connect(lambda: self.buttonClicked_newAnalyse_probleme(infoErr))

        self.horizontalLayout.addWidget(self.pushButton_com)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.pushButton_back4)
        self.horizontalLayout.addWidget(self.pushButton_runAnalysis)

        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)

    ######################################################################
    #                      Affichage dynamique                           #
    ######################################################################

    #Ces deux fonctions permettent d'affichier ou de cacher le champs du dbSNP
    # elle sont lancer selon si on clique sur oui (cela affciher le champs)
    # ou sur non, ce qui cache le champs.
    def AfficheSidbSNPexistePas(self):
        self.label_dbsnp.show()
        self.lineEdit_dbsnp.show()
        self.toolButton_dbsnp.show()

    def CacheSidbSNPexiste(self):
        self.label_dbsnp.hide()
        self.lineEdit_dbsnp.hide()
        self.toolButton_dbsnp.hide()

        ######################################################################
        #                      Formulaire - Etape 3                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape3(self):
        print("etape 3 formulaire")

        # Chope les textes des champs précédant
        plateforme=self.lineEdit_plateforme.text()
        sample=self.lineEdit_sample.text()
        library=self.lineEdit_library.text()
        rgid=self.lineEdit_rgid.text()
        rgpu=self.lineEdit_rgpu.text()
        SnpEffDB=self.lineEdit_SnpEffDB.text()
        SnpEffDBconf=self.lineEdit_SnpEffDBconf.text()
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        self.new.etape2(plateforme, sample, library, rgid, rgpu,SnpEffDB,SnpEffDBconf)
        #print(self.new.dico)

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_etape3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape3.setObjectName("label_etape3")
        self.label_etape3.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Step 3 of 4</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_etape3, 0, 0, 1, 1)

        self.label_titre3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre3.setObjectName("label_titre3")
        self.label_titre3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Population design for the mapping</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_titre3, 1, 0, 1, 1)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.label_backStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_backStrainId.setObjectName("label_backStrainId")
        self.label_backStrainId.setText("Background strain ID  :                       ")

        self.horizontalLayout_10.addWidget(self.label_backStrainId)

        self.lineEdit_backStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_backStrainId.setText("")
        self.lineEdit_backStrainId.setObjectName("lineEdit_backStrainId")

        if "backStrainId" in self.new.dico.keys():
            if self.new.dico["backStrainId"] != "":
                self.lineEdit_backStrainId.setText(self.new.dico["backStrainId"])

        self.horizontalLayout_10.addWidget(self.lineEdit_backStrainId)

        self.gridLayout_3.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_ref = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ref.setObjectName("label_ref")
        self.label_ref.setText("Referenced  :                                                         ")

        self.horizontalLayout.addWidget(self.label_ref)
        self.ButtonGroup_snp = QtWidgets.QButtonGroup()

        self.radioButton_yesRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_yesRef.setObjectName("radioButton_yesRef")
        self.radioButton_yesRef.setText("yes")

        if "referenced" in self.new.dico.keys():
            if self.new.dico["referenced"] == 0:
                self.radioButton_yesRef.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_yesRef)
        self.ButtonGroup_snp.addButton(self.radioButton_yesRef)

        self.radioButton_noRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_noRef.setObjectName("radioButton_noRef")
        self.radioButton_noRef.setText("no")

        if "referenced" in self.new.dico.keys():
            if self.new.dico["referenced"] == 1:
                self.radioButton_noRef.setChecked(True)

        self.ButtonGroup_snp.addButton(self.radioButton_noRef)
        self.horizontalLayout.addWidget(self.radioButton_noRef)

        self.horizontalLayout_bis = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bis.setObjectName("horizontalLayout")

        self.label_ref = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ref.setObjectName("label_ref")
        self.label_ref.setText("bdSNP betwen background and mapping  :       ")

        self.horizontalLayout_bis.addWidget(self.label_ref)

        #-----------------------------

        self.horizontalLayout_BGGVCF = QtWidgets.QHBoxLayout()
        self.horizontalLayout_BGGVCF.setObjectName("horizontalLayout_BGGVCF")
        self.label_BGGVCF = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_BGGVCF.setObjectName("label_BGGVCF")
        self.label_BGGVCF.setText("Background GVCF :                             ")

        self.horizontalLayout_BGGVCF.addWidget(self.label_BGGVCF)
        self.lineEdit_BGGVCF = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_BGGVCF.setObjectName("lineEdit_BGGVCF")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "backgroundGVCF" in self.new.dico.keys():
            if self.new.dico["backgroundGVCF"] != "":
                self.lineEdit_BGGVCF.setText(self.new.dico["backgroundGVCF"])

        self.horizontalLayout_BGGVCF.addWidget(self.lineEdit_BGGVCF)
        self.toolButton_BGGVCF = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_BGGVCF.setObjectName("toolButton_BGGVCF")
        self.toolButton_BGGVCF.setText("...")
        self.toolButton_BGGVCF.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_BGGVCF))

        self.horizontalLayout_BGGVCF.addWidget(self.toolButton_BGGVCF)
        self.gridLayout_3.addLayout(self.horizontalLayout_BGGVCF, 4, 0, 1, 1)

        #-----------------------------

        self.ButtonGroup_snpbool = QtWidgets.QButtonGroup()

        self.radioButton_yesRef_bis = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_yesRef_bis.setObjectName("radioButton_yesRef")
        self.radioButton_yesRef_bis.setText("yes")

        if "dbSNPbool" in self.new.dico.keys():
            if self.new.dico["dbSNPbool"] == '0' or self.new.dico["dbSNPbool"] == 0:
                self.radioButton_yesRef_bis.setChecked(True)

        self.ButtonGroup_snpbool.addButton(self.radioButton_yesRef_bis)
        self.horizontalLayout_bis.addWidget(self.radioButton_yesRef_bis)

        self.radioButton_noRef_bis = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_noRef_bis.setObjectName("radioButton_noRef")
        self.radioButton_noRef_bis.setText("no")

        if "dbSNPbool" in self.new.dico.keys():
            if self.new.dico["dbSNPbool"] == '1' or self.new.dico["dbSNPbool"] == 1:
                self.radioButton_noRef_bis.setChecked(True)

        self.ButtonGroup_snpbool.addButton(self.radioButton_noRef_bis)
        self.horizontalLayout_bis.addWidget(self.radioButton_noRef_bis)

        self.gridLayout_3.addLayout(self.horizontalLayout_bis, 7, 0, 1, 1)

        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.label_20.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_20.setToolTip("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">It should be the same as RGSM appearing in the $Mapping_gVCF (determine with &quot;Read Group&quot; information during analysis)</span></p></body></html>")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.label_mappStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_mappStrainId.setObjectName("label_mappStrainId")
        self.label_mappStrainId.setText("Mapping strain ID :                          ")

        self.horizontalLayout_16.addWidget(self.label_mappStrainId)

        self.lineEdit_mappStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_mappStrainId.setText("")
        self.lineEdit_mappStrainId.setObjectName("lineEdit_mappStrainId")

        if "mappStrainId" in self.new.dico.keys():
            if self.new.dico["mappStrainId"] != "":
                self.lineEdit_mappStrainId.setText(self.new.dico["mappStrainId"])

        self.horizontalLayout_16.addWidget(self.lineEdit_mappStrainId)

        self.gridLayout_3.addLayout(self.horizontalLayout_16, 5, 0, 1, 1)

        #-----------------------------

        self.horizontalLayout_MGVCF = QtWidgets.QHBoxLayout()
        self.horizontalLayout_MGVCF.setObjectName("horizontalLayout_MGVCF")
        self.label_MGVCF = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_MGVCF.setObjectName("label_MGVCF")
        self.label_MGVCF.setText("Mapping GVCF :                                   ")

        self.horizontalLayout_MGVCF.addWidget(self.label_MGVCF)
        self.lineEdit_MGVCF = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_MGVCF.setObjectName("lineEdit_MGVCF")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "mappingGVCF" in self.new.dico.keys():
            if self.new.dico["mappingGVCF"] != "":
                self.lineEdit_MGVCF.setText(self.new.dico["mappingGVCF"])

        self.horizontalLayout_MGVCF.addWidget(self.lineEdit_MGVCF)
        self.toolButton_MGVCF = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_MGVCF.setObjectName("toolButton_MGVCF")
        self.toolButton_MGVCF.setText("...")
        self.toolButton_MGVCF.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_MGVCF))

        self.horizontalLayout_MGVCF.addWidget(self.toolButton_MGVCF)
        self.gridLayout_3.addLayout(self.horizontalLayout_MGVCF, 6, 0, 1, 1)

        #-----------------------------

        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        self.label_dbsnp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_dbsnp.setObjectName("label_dbsnp")
        self.label_dbsnp.setText("dbSNP (background vs mapping)  :")

        self.horizontalLayout_17.addWidget(self.label_dbsnp)

        self.lineEdit_dbsnp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_dbsnp.setText("")
        self.lineEdit_dbsnp.setObjectName("lineEdit_dbsnp")

        if "dbSNP" in self.new.dico.keys():
            if self.new.dico["dbSNP"] != "":
                self.lineEdit_dbsnp.setText(self.new.dico["dbSNP"])

        self.horizontalLayout_17.addWidget(self.lineEdit_dbsnp)

        self.toolButton_dbsnp = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_dbsnp.setObjectName("toolButton_dbsnp")
        self.toolButton_dbsnp.setText("...")
        self.toolButton_dbsnp.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_dbsnp))

        self.horizontalLayout_17.addWidget(self.toolButton_dbsnp)

        self.gridLayout_3.addLayout(self.horizontalLayout_17, 8, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_3.addItem(spacerItem, 9, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_back3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back3.setObjectName("pushButton_back3")
        self.pushButton_back3.setText("Back")
        self.pushButton_back3.clicked.connect(self.buttonClicked_newAnalyse_etape2)

        self.horizontalLayout_2.addWidget(self.pushButton_back3)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton_next3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next3.setObjectName("pushButton_next3")
        self.pushButton_next3.setText("Next")
        self.pushButton_next3.clicked.connect(self.buttonClicked_newAnalyse_etape4)

        self.horizontalLayout_2.addWidget(self.pushButton_next3)

        if self.new.dico["dbSNPbool"] == 1 :
                self.label_dbsnp.hide()
                self.lineEdit_dbsnp.hide()
                self.toolButton_dbsnp.hide()
        else :
            if not "dbSNPbool" in self.new.dico.keys():
                self.label_dbsnp.hide()
                self.lineEdit_dbsnp.hide()
                self.toolButton_dbsnp.hide()

        self.radioButton_yesRef_bis.clicked.connect(self.AfficheSidbSNPexistePas)
        self.radioButton_noRef_bis.clicked.connect(self.CacheSidbSNPexiste)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)


        ######################################################################
        #                      Formulaire - Etape 2                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape2(self):
        print("etape 2 formulaire")

        ## Avant de cacher les champs et de les "effacer" je recupere les valeurs des
        ## champs pour remplir le fichier de config
        # Chope les texte
        GenRef=self.lineEdit_genRef.text()
        nom=self.lineEdit_nom.text()
        ram=self.lineEdit_ram.text()
        dossierS=self.lineEdit_dossierS.text()

        read=[]
        if self.nbr==2:
            read.append(self.lineEdit_r1.text())
            read.append(self.lineEdit_r2.text())
        if self.nbr==4:
            read.append(self.lineEdit_r1.text())
            read.append(self.lineEdit_r2.text())
            read.append(self.lineEdit_r3.text())
            read.append(self.lineEdit_r4.text())
        if self.nbr==6:
            read.append(self.lineEdit_r1.text())
            read.append(self.lineEdit_r2.text())
            read.append(self.lineEdit_r3.text())
            read.append(self.lineEdit_r4.text())
            read.append(self.lineEdit_r5.text())
            read.append(self.lineEdit_r6.text())
        if self.nbr==7:
            read.append(self.lineEdit_r1.text())
            read.append(self.lineEdit_r2.text())
            read.append(self.lineEdit_r3.text())
            read.append(self.lineEdit_r4.text())
            read.append(self.lineEdit_r5.text())
            read.append(self.lineEdit_r6.text())
            read.append(self.lineEdit_r7.text())
            read.append(self.lineEdit_r8.text())

        # On les sauvegarde dans le dictionnaire qui gènre les champs
        self.new.etape1(GenRef, self.nbr, read, nom, ram, dossierS)

        ## Mise en place des champs de formulaire pour l'affichage de l'étape 2
        # Cacher les ancien champs en cachant la scroll area
        self.scrollArea.hide()
        # Recréer l'esapce de scroll area vide
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Ajout de tout les champs dans la nouvelle scroll area de l'etape 2

        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.pushButton_next2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next2.setObjectName("pushButton_next2")
        self.pushButton_next2.setText("Next")
        self.pushButton_next2.clicked.connect(self.buttonClicked_newAnalyse_etape3)

        self.gridLayout_4.addWidget(self.pushButton_next2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_back2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back2.setObjectName("pushButton_back2")
        self.pushButton_back2.setText("Back")
        self.pushButton_back2.clicked.connect(lambda: self.buttonClicked_newAnalyse("back"))

        self.gridLayout_4.addWidget(self.pushButton_back2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 6, 0, 1, 2)
        self.label_Indiq2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Indiq2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_Indiq2.setObjectName("label_Indiq2")
        self.label_Indiq2.setText("<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-style:italic;\">Les noms des fichiers seront construis ainsi : {FlowCellID}-{sampleID}_Lane </span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_Indiq2, 2, 0, 1, 2)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_sample = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_sample.setObjectName("label_sample")
        self.label_sample.setText("Sample :            ")

        self.horizontalLayout_2.addWidget(self.label_sample)

        self.lineEdit_sample = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_sample.setObjectName("lineEdit_sample")
        self.lineEdit_sample.setText("")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "sample" in self.new.dico.keys():
            if self.new.dico["sample"] != "":
                self.lineEdit_sample.setText(self.new.dico["sample"])

        self.horizontalLayout_2.addWidget(self.lineEdit_sample)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_library = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_library.setObjectName("label_library")
        self.label_library.setText("Library :             ")

        self.horizontalLayout.addWidget(self.label_library)

        self.lineEdit_library = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_library.setObjectName("lineEdit_library")
        self.lineEdit_library.setText("")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "library" in self.new.dico.keys():
            if self.new.dico["library"] != "":
                self.lineEdit_library.setText(self.new.dico["library"])

        self.horizontalLayout.addWidget(self.lineEdit_library)

        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_8.setToolTip("<html><head/><body><p>Choose \'Flow Cell ID\'_\'sample\'</p></body></html>")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_rgid = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_rgid.setObjectName("label_rgid")
        self.label_rgid.setText("RGID :             ")

        self.horizontalLayout_5.addWidget(self.label_rgid)

        self.lineEdit_rgid = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_rgid.setObjectName("lineEdit_rgid")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "rgid" in self.new.dico.keys():
            if self.new.dico["rgid"] != "":
                self.lineEdit_rgid.setText(self.new.dico["rgid"])

        self.horizontalLayout_5.addWidget(self.lineEdit_rgid)

        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")

        self.label_9.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_9.setToolTip("<html><head/><body><p>Choose \'Flow Cell ID\'_\'Lane\'_\'sample\'</p></body></html>")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_rgpu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_rgpu.setObjectName("label_rgpu")
        self.label_rgpu.setText("RGPU :            ")

        self.horizontalLayout_4.addWidget(self.label_rgpu)

        self.lineEdit_rgpu = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_rgpu.setObjectName("lineEdit_rgpu")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "rgpu" in self.new.dico.keys():
            if self.new.dico["rgpu"] != "":
                self.lineEdit_rgpu.setText(self.new.dico["rgpu"])

        self.horizontalLayout_4.addWidget(self.lineEdit_rgpu)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_plateforme = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_plateforme.setObjectName("label_plateforme")
        self.label_plateforme.setText("Platform :         ")

        self.horizontalLayout_3.addWidget(self.label_plateforme)

        self.lineEdit_plateforme = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_plateforme.setObjectName("lineEdit_plateforme")
        self.lineEdit_plateforme.setText("")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "plateforme" in self.new.dico.keys():
            if self.new.dico["plateforme"] != "":
                self.lineEdit_plateforme.setText(self.new.dico["plateforme"])

        self.horizontalLayout_3.addWidget(self.lineEdit_plateforme)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_3, 3, 0, 1, 2)

        #-----------------------------

        self.horizontalLayout_SnpEffDB = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SnpEffDB.setObjectName("horizontalLayout_SnpEffDB")
        self.label_SnpEffDB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_SnpEffDB.setObjectName("label_SnpEffDB")
        self.label_SnpEffDB.setText("SnpEff data base :    ")

        self.horizontalLayout_SnpEffDB.addWidget(self.label_SnpEffDB)
        self.lineEdit_SnpEffDB = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_SnpEffDB.setObjectName("lineEdit_SnpEffDB")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "SnpEffDB" in self.new.dico.keys():
            if self.new.dico["SnpEffDB"] != "":
                self.lineEdit_SnpEffDB.setText(self.new.dico["SnpEffDB"])

        self.horizontalLayout_SnpEffDB.addWidget(self.lineEdit_SnpEffDB)
        self.toolButton_SnpEffDB = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_SnpEffDB.setObjectName("toolButton_SnpEffDB")
        self.toolButton_SnpEffDB.setText("...")
        self.toolButton_SnpEffDB.clicked.connect(lambda: self.ouvrir_dossier(self.lineEdit_SnpEffDB))

        self.horizontalLayout_SnpEffDB.addWidget(self.toolButton_SnpEffDB)
        self.gridLayout_5.addLayout(self.horizontalLayout_SnpEffDB, 4, 0, 1, 1)

        #-----------------------------

        #-----------------------------

        self.horizontalLayout_SnpEffDBconf = QtWidgets.QHBoxLayout()
        self.horizontalLayout_SnpEffDBconf.setObjectName("horizontalLayout_SnpEffDBconf")
        self.label_SnpEffDBconf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_SnpEffDBconf.setObjectName("label_SnpEffDBconf")
        self.label_SnpEffDBconf.setText("SnpEff config file :   ")

        self.horizontalLayout_SnpEffDBconf.addWidget(self.label_SnpEffDBconf)
        self.lineEdit_SnpEffDBconf = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_SnpEffDBconf.setObjectName("lineEdit_SnpEffDBconf")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "SnpEffDBconf" in self.new.dico.keys():
            if self.new.dico["SnpEffDBconf"] != "":
                self.lineEdit_SnpEffDBconf.setText(self.new.dico["SnpEffDBconf"])

        self.horizontalLayout_SnpEffDBconf.addWidget(self.lineEdit_SnpEffDBconf)
        self.toolButton_SnpEffDBconf = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_SnpEffDBconf.setObjectName("toolButton_SnpEffDBconf")
        self.toolButton_SnpEffDBconf.setText("...")
        self.toolButton_SnpEffDBconf.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_SnpEffDBconf))

        self.horizontalLayout_SnpEffDBconf.addWidget(self.toolButton_SnpEffDBconf)
        self.gridLayout_5.addLayout(self.horizontalLayout_SnpEffDBconf, 5, 0, 1, 1)

        #-----------------------------

        self.label_BGI = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_BGI.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_BGI.setMidLineWidth(0)
        self.label_BGI.setIndent(1)
        self.label_BGI.setOpenExternalLinks(False)
        self.label_BGI.setObjectName("label_BGI")
        self.label_BGI.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># BGI </span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_BGI, 1, 0, 1, 1)

        self.label_etape2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape2.setObjectName("label_etape2")
        self.label_etape2.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Step 2 of 4</span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_etape2, 0, 0, 1, 2)

        self.label_BGI.raise_()
        self.label_Indiq2.raise_()
        self.label_etape2.raise_()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #       fonction permettant de dynamiser les ligne info de read      #
        ######################################################################

    #Cette fonction permet l'affichage de moins de champs de lecture (read) en fonction
    #de ceux qui sont déja présent dans l'anayse. Elle se sert de l'indication donner
    #par self.nbr et le met a jours.
    def moins (self, nbr):

        if self.nbr==4 :
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.hide()
            self.lineEdit_r3.hide()
            self.toolButton_r3.hide()

            self.label_r4.hide()
            self.lineEdit_r4.hide()
            self.toolButton_r4.hide()

            self.label_r5.hide()
            self.lineEdit_r5.hide()
            self.toolButton_r5.hide()

            self.label_r6.hide()
            self.lineEdit_r6.hide()
            self.toolButton_r6.hide()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

            self.nbr=2

        elif self.nbr == 6:
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.show()
            self.lineEdit_r3.show()
            self.toolButton_r3.show()

            self.label_r4.show()
            self.lineEdit_r4.show()
            self.toolButton_r4.show()

            self.label_r5.hide()
            self.lineEdit_r5.hide()
            self.toolButton_r5.hide()

            self.label_r6.hide()
            self.lineEdit_r6.hide()
            self.toolButton_r6.hide()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

            self.nbr=4

        elif self.nbr == 8:
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.show()
            self.lineEdit_r3.show()
            self.toolButton_r3.show()

            self.label_r4.show()
            self.lineEdit_r4.show()
            self.toolButton_r4.show()

            self.label_r5.show()
            self.lineEdit_r5.show()
            self.toolButton_r5.show()

            self.label_r6.show()
            self.lineEdit_r6.show()
            self.toolButton_r6.show()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

            self.nbr=6

    #Cette fonction permet l'affichage de plus de champs de lecture (read) en fonction
    #de ceux qui sont déja présent dans l'anayse. Elle se sert de l'indication donner
    #par self.nbr et le met a jours. Si on affiche 4 champs et que l'on en remplis que deux
    #le formulaire va lever une erreur puisque deux champs serons vide. Si on a vraiment
    #que deux champs il faufra cacher deux champs.
    def plus (self):

        if self.nbr == 2 :
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.show()
            self.lineEdit_r3.show()
            self.toolButton_r3.show()

            self.label_r4.show()
            self.lineEdit_r4.show()
            self.toolButton_r4.show()

            self.label_r5.hide()
            self.lineEdit_r5.hide()
            self.toolButton_r5.hide()

            self.label_r6.hide()
            self.lineEdit_r6.hide()
            self.toolButton_r6.hide()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

            self.nbr=4

        elif self.nbr == 4 :
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.show()
            self.lineEdit_r3.show()
            self.toolButton_r3.show()

            self.label_r4.show()
            self.lineEdit_r4.show()
            self.toolButton_r4.show()

            self.label_r5.show()
            self.lineEdit_r5.show()
            self.toolButton_r5.show()

            self.label_r6.show()
            self.lineEdit_r6.show()
            self.toolButton_r6.show()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

            self.nbr=6

        elif self.nbr == 6 :
            self.label_r1.show()
            self.lineEdit_r1.show()
            self.toolButton_r1.show()

            self.label_r2.show()
            self.lineEdit_r2.show()
            self.toolButton_r2.show()

            self.label_r3.show()
            self.lineEdit_r3.show()
            self.toolButton_r3.show()

            self.label_r4.show()
            self.lineEdit_r4.show()
            self.toolButton_r4.show()

            self.label_r5.show()
            self.lineEdit_r5.show()
            self.toolButton_r5.show()

            self.label_r6.show()
            self.lineEdit_r6.show()
            self.toolButton_r6.show()

            self.label_r7.show()
            self.lineEdit_r7.show()
            self.toolButton_r7.show()

            self.label_r8.show()
            self.lineEdit_r8.show()
            self.toolButton_r8.show()

            self.nbr=8

        ######################################################################
        #                      Formulaire - Etape 1                          #
        ######################################################################

        #if i in self.dico_indexer_read.keys():

    def buttonClicked_newAnalyse(self, indicationDeOuLonViens, fichier=None):
        print("nouvelle annalyse")
        self.scrollArea.hide()

        #Selon d'ou on viens (de quelle bouton nous a amener a cette premiere page du formulaire)
        #le ditionnaire ne se comporte pas de la même manière, une varriable passer en paramettre de
        #la fonction nous l'indique donc.

        #Si l'on viens du bouton back de la page deux du dictionnaire on veux les information du
        #dictionnaire utilisé (en cours) donc on ne fait rien.
        if indicationDeOuLonViens == "back":
            pass
        #Si l'on viens du bouton ok de la première page de recharge d'une analyse on veux charger en mémoire
        #le dictionnaire de l'ancienne analyse (fonction remplisDico de la classe formulaire)
        #On efface aussi le titre dans ce dictionnaire pour ne pas ecracraser par erreur le formulaire de l'nalyse
        #que l'on recharge, et être obliger de lui donner un nouveau titre (il faut eviter de lui donner exactement
        #le même nom).
        #On met a jours le nombre de fichier de lectures (read) ensuite en fonction des données présente
        #dans le dictionnaire charger.
        if indicationDeOuLonViens == "fichierConfigue":
            #print("viens de re forme")
            self.new=ClassFormulaire.Formulaire()
            self.new.remplisDico(fichier)
            self.new.dico["nom"]=""
            if "read1" in self.new.dico.keys():
                #print("1")
                self.nbr=2
            if "read3" in self.new.dico.keys():
                #print("3")
                self.nbr=4
            if "read5" in self.new.dico.keys():
                #print("5")
                self.nbr=6
            if "read7" in self.new.dico.keys():
                #print("7")
                self.nbr=8
        #Si l'on viens du bouton nouvelle analyse du menu gauche on veux vider le dictionnaire
        #si il contient déjà des données pour démaré une nnouvelle analyse.
        if indicationDeOuLonViens == "nouvelle analyse" :
            #print("viens de nouvelle analyse")
            self.new=ClassFormulaire.Formulaire()

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_etape1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape1.setObjectName("label_etape1")
        self.label_etape1.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Step 1 of 4</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_etape1, 0, 0, 1, 1)
        self.label_titre1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre1.setObjectName("label_titre1")
        self.label_titre1.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Your inputs :</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_titre1, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_nom = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_nom.setObjectName("label_nom")
        self.label_nom.setText("Analysis name :              ")

        self.horizontalLayout_11.addWidget(self.label_nom)
        self.lineEdit_nom = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.horizontalLayout_11.addWidget(self.lineEdit_nom)

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "nom" in self.new.dico.keys():
            if self.new.dico["nom"] != "":
                self.lineEdit_nom.setText(self.new.dico["nom"])

        self.gridLayout_3.addLayout(self.horizontalLayout_11, 2, 0, 1, 1)

        #########################################Ajout de choix de docier de sortie :

        self.horizontalLayout_111 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_111.setObjectName("horizontalLayout_10")
        self.label_dossierS = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_dossierS.setObjectName("label_dossierS")
        self.label_dossierS.setText("Output folder :              ")

        self.horizontalLayout_111.addWidget(self.label_dossierS)
        self.lineEdit_dossierS = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_dossierS.setObjectName("lineEdit_dossierS")
        self.horizontalLayout_111.addWidget(self.lineEdit_dossierS)
        self.toolButton_dossierS = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_dossierS.setObjectName("toolButton_dossierS")
        self.toolButton_dossierS.setText("...")
        self.toolButton_dossierS.clicked.connect(lambda: self.ouvrir_dossier(self.lineEdit_dossierS))

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "dossierS" in self.new.dico.keys():
            if self.new.dico["dossierS"] != "":
                self.lineEdit_dossierS.setText(self.new.dico["dossierS"])

        self.horizontalLayout_111.addWidget(self.toolButton_dossierS)
        self.gridLayout_3.addLayout(self.horizontalLayout_111, 3, 0, 1, 1)

        ################################################################################


        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_genRef = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_genRef.setObjectName("label_genRef")
        self.label_genRef.setText("Reference genome :    ")

        self.horizontalLayout_10.addWidget(self.label_genRef)
        self.lineEdit_genRef = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_genRef.setObjectName("lineEdit_genRef")
        self.horizontalLayout_10.addWidget(self.lineEdit_genRef)
        self.toolButton_genRef = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_genRef.setObjectName("toolButton_genRef")
        self.toolButton_genRef.setText("...")
        self.toolButton_genRef.clicked.connect(lambda: self.ouvrir_dossier(self.lineEdit_genRef))

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "genRef" in self.new.dico.keys():
            if self.new.dico["genRef"] != "":
                self.lineEdit_genRef.setText(self.new.dico["genRef"])

        self.horizontalLayout_10.addWidget(self.toolButton_genRef)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)

        self.horizontalLayout_101 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_101.setObjectName("horizontalLayout_10")
        self.label_ram = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ram.setObjectName("label_ram")
        self.label_ram.setText("Ram :                                 ")

        self.horizontalLayout_101.addWidget(self.label_ram)
        self.lineEdit_ram = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_ram.setObjectName("lineEdit_ram")
        self.horizontalLayout_101.addWidget(self.lineEdit_ram)
        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "ram" in self.new.dico.keys():
            if self.new.dico["ram"] != "":
                self.lineEdit_ram.setText(str(self.new.dico["ram"]))

        #self.horizontalLayout_101.addWidget(self.toolButton_ram)
        self.gridLayout_3.addLayout(self.horizontalLayout_101, 5, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_r1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r1.setObjectName("label_r1")
        self.label_r1.setText("[1] Read : ")

        self.horizontalLayout.addWidget(self.label_r1)
        self.lineEdit_r1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r1.setObjectName("lineEdit_r1")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read0" in self.new.dico.keys():
            if self.new.dico["read0"] != "":
                self.lineEdit_r1.setText(self.new.dico["read0"])

        self.horizontalLayout.addWidget(self.lineEdit_r1)
        self.toolButton_r1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r1.setObjectName("toolButton_r1")
        self.toolButton_r1.setText("...")
        self.toolButton_r1.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r1))

        self.horizontalLayout.addWidget(self.toolButton_r1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_r2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r2.setObjectName("label_r2")
        self.label_r2.setText("[2] Read : ")

        self.horizontalLayout_9.addWidget(self.label_r2)
        self.lineEdit_r2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r2.setObjectName("lineEdit_r2")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read1" in self.new.dico.keys():
            if self.new.dico["read1"] != "":
                self.lineEdit_r2.setText(self.new.dico["read1"])

        self.horizontalLayout_9.addWidget(self.lineEdit_r2)
        self.toolButton_r2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r2.setObjectName("toolButton_r2")
        self.toolButton_r2.setText("...")
        self.toolButton_r2.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r2))

        self.horizontalLayout_9.addWidget(self.toolButton_r2)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_r3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r3.setObjectName("label_r3")
        self.label_r3.setText("[3] Read : ")

        self.horizontalLayout_2.addWidget(self.label_r3)
        self.lineEdit_r3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r3.setObjectName("lineEdit_r3")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read2" in self.new.dico.keys():
            if self.new.dico["read2"] != "":
                self.lineEdit_r3.setText(self.new.dico["read2"])

        self.horizontalLayout_2.addWidget(self.lineEdit_r3)
        self.toolButton_r3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r3.setObjectName("toolButton_r3")
        self.toolButton_r3.setText("...")
        self.toolButton_r3.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r3))

        self.horizontalLayout_2.addWidget(self.toolButton_r3)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_r4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r4.setObjectName("label_r4")
        self.label_r4.setText("[4] Read : ")

        self.horizontalLayout_4.addWidget(self.label_r4)
        self.lineEdit_r4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r4.setObjectName("lineEdit_r4")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read3" in self.new.dico.keys():
            if self.new.dico["read3"] != "":
                self.lineEdit_r4.setText(self.new.dico["read3"])

        self.horizontalLayout_4.addWidget(self.lineEdit_r4)
        self.toolButton_r4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r4.setObjectName("toolButton_r4")
        self.toolButton_r4.setText("...")
        self.toolButton_r4.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r4))

        self.horizontalLayout_4.addWidget(self.toolButton_r4)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 9, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_r5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r5.setObjectName("label_r5")
        self.label_r5.setText("[5] Read : ")

        self.horizontalLayout_5.addWidget(self.label_r5)
        self.lineEdit_r5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r5.setObjectName("lineEdit_r5")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read4" in self.new.dico.keys():
            if self.new.dico["read4"] != "":
                self.lineEdit_r5.setText(self.new.dico["read4"])

        self.horizontalLayout_5.addWidget(self.lineEdit_r5)
        self.toolButton_r5 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r5.setObjectName("toolButton_r5")
        self.toolButton_r5.setText("...")
        self.toolButton_r5.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r5))

        self.horizontalLayout_5.addWidget(self.toolButton_r5)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 10, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_r6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r6.setObjectName("label_r6")
        self.label_r6.setText("[6] Read : ")

        self.horizontalLayout_6.addWidget(self.label_r6)
        self.lineEdit_r6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r6.setObjectName("lineEdit_r6")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read5" in self.new.dico.keys():
            if self.new.dico["read5"] != "":
                self.lineEdit_r6.setText(self.new.dico["read5"])

        self.horizontalLayout_6.addWidget(self.lineEdit_r6)
        self.toolButton_r6 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r6.setObjectName("toolButton_r6")
        self.toolButton_r6.setText("...")
        self.toolButton_r6.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r6))

        self.horizontalLayout_6.addWidget(self.toolButton_r6)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 11, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_r7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r7.setObjectName("label_r7")
        self.label_r7.setText("[7] Read : ")

        self.horizontalLayout_7.addWidget(self.label_r7)
        self.lineEdit_r7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r7.setObjectName("lineEdit_r7")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read6" in self.new.dico.keys():
            if self.new.dico["read6"] != "":
                self.lineEdit_r7.setText(self.new.dico["read6"])

        self.horizontalLayout_7.addWidget(self.lineEdit_r7)
        self.toolButton_r7 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r7.setObjectName("toolButton_r7")
        self.toolButton_r7.setText("...")
        self.toolButton_r7.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r7))

        self.horizontalLayout_7.addWidget(self.toolButton_r7)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 12, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_r8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_r8.setObjectName("label_r8")
        self.label_r8.setText("[8] Read : ")

        self.horizontalLayout_8.addWidget(self.label_r8)
        self.lineEdit_r8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_r8.setObjectName("lineEdit_r8")

        #Si la clef est dans le dictionnaire et si la valeur associé n'est pas vide
        #C'est qu'une information est déja présente alors on l'affiche dans la ligne de saisie.
        #Elle peut être présente pasque qu'on la déjà remplis et que l'on revien en arrière dans le dictionnaire
        #ou qu'on a charger une ancienne annalyse.
        if "read7" in self.new.dico.keys():
            if self.new.dico["read7"] != "":
                self.lineEdit_r8.setText(self.new.dico["read7"])

        self.horizontalLayout_8.addWidget(self.lineEdit_r8)
        self.toolButton_r8 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_r8.setObjectName("toolButton_r8")
        self.toolButton_r8.setText("...")
        self.toolButton_r8.clicked.connect(lambda: self.ouvrir_fichier(self.lineEdit_r8))

        ####################
        #gestion du dynasisme des ligne de saisie des fichiers de lectures.
        #La variable self.nbr gère le nombre de fichiers de lectures nécessaire a
        #l'analyse en cours.

        if self.nbr==2:
            self.label_r3.hide()
            self.lineEdit_r3.hide()
            self.toolButton_r3.hide()

            self.label_r4.hide()
            self.lineEdit_r4.hide()
            self.toolButton_r4.hide()

            self.label_r5.hide()
            self.lineEdit_r5.hide()
            self.toolButton_r5.hide()

            self.label_r6.hide()
            self.lineEdit_r6.hide()
            self.toolButton_r6.hide()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()
        elif self.nbr==4:
            self.label_r5.hide()
            self.lineEdit_r5.hide()
            self.toolButton_r5.hide()

            self.label_r6.hide()
            self.lineEdit_r6.hide()
            self.toolButton_r6.hide()

            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()
        elif self.nbr==6:
            self.label_r7.hide()
            self.lineEdit_r7.hide()
            self.toolButton_r7.hide()

            self.label_r8.hide()
            self.lineEdit_r8.hide()
            self.toolButton_r8.hide()

        ########################

        self.horizontalLayout_8.addWidget(self.toolButton_r8)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 12, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.pushButton_plus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_plus.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_plus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_plus.setText("+")
        self.pushButton_plus.clicked.connect(self.plus)

        self.horizontalLayout_12.addWidget(self.pushButton_plus)
        self.pushButton_moins = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_moins.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_moins.setObjectName("pushButton_moins")
        self.pushButton_moins.setText("-")
        self.pushButton_moins.clicked.connect(self.moins)
        self.horizontalLayout_12.addWidget(self.pushButton_moins)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 14, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_next1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_next1.setObjectName("pushButton_next1")
        self.pushButton_next1.setText("Next")
        self.pushButton_next1.clicked.connect(self.buttonClicked_newAnalyse_etape2)
        self.horizontalLayout_3.addWidget(self.pushButton_next1)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 15, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

    #Fonction qui ajoute le texte sur les éléments de la fenetre princiale (= menu a gauche)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>"))
        self.pushButton_acceuil.setText(_translate("MainWindow", "Home"))
        self.pushButton_newAnalyse.setText(_translate("MainWindow", "New analysis"))
        self.pushButton_oldAnalise.setText(_translate("MainWindow", "Load a previous analysis"))
        self.pushButton_resultat.setText(_translate("MainWindow", "Results"))
        self.pushButton_author.setText(_translate("MainWindow", "About author"))

        ######################################################################
        #                                                                    #
        #                Boucle principale du programmme                     #
        #                                                                    #
        ######################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
