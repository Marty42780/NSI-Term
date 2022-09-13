<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER &quot; essais&quot;"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2lignes="" F2para="" F2etat="inactif" F2defaut=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <param epaisseurPoint="2" nbDecimales="8" epaisseurLigne="2" arrondiAuto="vrai" maxBoucle="500000" totalAffichages="1000" totalBoucles="5000000"/>
    <item algoitem="FONCTIONS_UTILISEES" code="200#declarationfonctions"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="nb EST_DU_TYPE NOMBRE" code="1#NOMBRE#nb"/>
        <item algoitem="prop EST_DU_TYPE NOMBRE" code="1#NOMBRE#prop"/>
        <item algoitem="essais_restants EST_DU_TYPE NOMBRE" code="1#NOMBRE#essais_restants"/>
        <item algoitem="essais_joueur EST_DU_TYPE NOMBRE" code="1#NOMBRE#essais_joueur"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="nb PREND_LA_VALEUR ALGOBOX_ALEA_ENT(0,100)" code="5#nb#ALGOBOX_ALEA_ENT(0,100)#pasliste"/>
        <item algoitem="prop PREND_LA_VALEUR -1" code="5#prop#-1#pasliste"/>
        <item algoitem="LIRE essais_restants" code="2#essais_restants#pasliste"/>
        <item algoitem="essais_joueur PREND_LA_VALEUR 0" code="5#essais_joueur#0#pasliste"/>
        <item algoitem="AFFICHER nb" code="3#nb#0#pasliste"/>
        <item algoitem="TANT_QUE (nb != prop ET essais_restants > 0) FAIRE" code="15#nb != prop ET essais_restants > 0">
            <item algoitem="DEBUT_TANT_QUE" code="16#debuttantque"/>
            <item algoitem="essais_restants PREND_LA_VALEUR essais_restants -1" code="5#essais_restants#essais_restants -1#pasliste"/>
            <item algoitem="essais_joueur PREND_LA_VALEUR essais_joueur + 1" code="5#essais_joueur#essais_joueur + 1#pasliste"/>
            <item algoitem="LIRE prop" code="2#prop#pasliste"/>
            <item algoitem="SI (essais_restants != 0) ALORS" code="6#essais_restants != 0">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="SI (prop > nb) ALORS" code="6#prop > nb">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;Plus petit&quot;" code="4#Plus petit#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="SI (prop &lt; nb) ALORS" code="6#prop &lt; nb">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;Plus grand&quot;" code="4#Plus grand#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="FIN_TANT_QUE" code="17#fintantque"/>
        </item>
        <item algoitem="SI (nb == prop) ALORS" code="6#nb == prop">
            <item algoitem="DEBUT_SI" code="7#debutsi"/>
            <item algoitem="AFFICHER &quot;Vous avez trouvé le nombre en &quot;" code="4#Vous avez trouvé le nombre en #0"/>
            <item algoitem="AFFICHER essais_joueur" code="3#essais_joueur#0#pasliste"/>
            <item algoitem="AFFICHER &quot; essais&quot;" code="4# essais#0"/>
            <item algoitem="FIN_SI" code="8#finsi"/>
            <item algoitem="SINON" code="9#sinon">
                <item algoitem="DEBUT_SINON" code="10#debutsinon"/>
                <item algoitem="SI (essais_restants &lt; 1) ALORS" code="6#essais_restants &lt; 1">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;Vous avez perdu&quot;" code="4#Vous avez perdu#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="FIN_SINON" code="11#finsinon"/>
            </item>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
