# Projet "Programmation pour le Web Sémantique" (printemps 2021)

## Déroulement
 1. *Aligner et modifier les ontologies de [music_ontology](https://gitlab.com/myclassunil/repository/-/raw/master/ontologies/music_ontology.owl) et [dbpedia](https://gitlab.com/myclassunil/repository/-/raw/master/ontologies/dbpedia_3.8.owl) pour les adapter aux taches de votre projet.*
 
	 Je n'ai malheureusement pas pris spécialement de notes sur cette étape du processus. J'ai pris comme ontologie de base dbpedia, et j'ai ensuite regardé un à un les éléments de music ontology pour les aligner aussi précisément que possible. Parfois, comme dans le cas de "Album" (dbo:Album), c'était simple, mais dans d'autres cas, comme le cas des artistes musicaux, cela nécessitait bien de la réflexion et une lecture attentive de la documentation des deux ontologies. J'ai fini par classer les groupes et les artistes solo comme agents, mais je reste encore peu convaincue de cette décision.
 2. *Explorer le dataset [jamendo](http://dbtune.org/jamendo/#query)*
 	Ceci était une étape plutôt ludique et stimulant du projet: j'ai simplement fait un grand nombre de requêtes, de formes aussi diverses et variés que possible, pour essayer d'acquérir une connaissance intuitive du grand dataset Jamendo. C'est durant cette étape que j'ai réellement saisi la diversité de possibilités offerts par la programmation pour le web sémantique.
3. *Pour chaque [prefix](http://dbtune.org/jamendo/cliopatria/browse/list_prefixes?format=turtle), vérifier si et où il est utilisé dans les triplets du dataset. [ICI]*
4. *Répéter le point 3 pour chaque [prefix](http://dbtune.org/jamendo/cliopatria/browse/list_prefixes?format=turtle) et pour chaque partie du triplet (sujet, prédicat, object)*
5. *Vérifier si le sujet, prédicat et/ou object a un élement équivalent dans les ontologies alignées au point 1  par exemple on teste si le prefix qui commence avec `http://www.holygoat` apparait dans le prédicat (il faudra voir s'il apparait également dans le sujet et l'objet)*

    Si l'étape 2 était ludique, les étapes 3, 4 et 5 étaient tout son contraire! Le fait de tester systématiquement chaque prefix pour le sujet prédicat et objet était souvent laborieux, mais compensé par les moments plus stimulants lorsqu'il fallait intégrer ces éléments dans l'ontologie. Ce n'était pas toujours simple! Là encore, j'ai tenté de beaucoup m'appuyer sur la documentation. Certaines parties de ces documentations donnaient des informations exceptionnellement utiles, comme le domain et le range de certains propriétés. Cependant, j'ai du renoncer à correctement ingérer chaque prefix, car notamment pour http://purl.org/NET/c4dm/timeline.owl#, cette data property était déprécié et les informations à ce sujet manquaient. En vue de l'absence d'élément équivalent ou d'informations me permettant d'intégrer cet élément de façon adéquate, j'ai donc décidé de ne pas le faire.

6. *Lancer le raisonnement pour voir si tout est correct.*

	 Rien a signaler ici à part que, pour éviter de potentiellement devoir refaire beaucoup de travail, j'ai lancé et synchronisé le *reasoner* à plusieurs reprises.
7. *Installer [fuseki](https://jena.apache.org/documentation/fuseki2/) pour [win](/ish_unil/students_sw/2020_2021/-/blob/master/Setting%20Up%20Jena%20Fuseki%20with%20Update%20in%20Windows%2010%20_%20by%20Fariz%20Darari%20_%20Medium.html) or for [Mac](https://brewinstall.org/install-fuseki-on-mac-with-brew/)*

	Ici non plus rien de particulier à signaler, si ce n'est que, par paresse ou par habitude, j'avais souhaité dans un premier temps utiliser la version de fueski déja installée via Docker. Pour des raisons qui deviendront apparantes plus tard, j'ai dû renoncer à cela.
8.  *Uploader votre ontologie ainsi que les [rdf jamendo](/ish_unil/students_sw/2020_2021/-/blob/master/Jamendo.zip) dans fuseki comme montré [ici](https://youtu.be/3WTtKaIfqnk?t=119) (cette vidéo est utile aussi pour l'installation de fuseki dans win)*

	Ici j'ai eu plusieurs soucis. D'une part, je n'étais pas parvenue à trouver les bons RDF Jamendo de moi-même, et ai dû demander de l'aide au professeur. Par la suite, je me suis rendue compte d'un erreur qui s'était glissé dans ce dataset: il y avait un espace quelque part.
 ![Erreur dans le dataset](https://imgur.com/668sZrE.jpg)
 
	Afin de résoudre cette erreur, je suis simplement allée dans la fenêtre command prompt d'où j'avais lancé le serveur. Le message m'indiquait la ligne et la colonne précise de l'espace, j'ai donc pu l'ouvrir dans un éditeur de texte simple et trouver l'espace pour le transformer en underscore.
	Malheureusement, mes peines n'étaient pas encore terminées. Le dataset jamendo semblait être trop grand pour la configuration Java de base. J'ai donc encore appelé à l'aide du patient professeur Picca, qui m'a proposé une solution pour augmenter le entityExpansionLimit du côté de Java.
	Il reste un problème auquel je n'ai pas encore trouvé la solution: si je veux lancer à nouveau Jena Fuseki après avoir éteint mon ordinateur, je suis obligée de supprimer les fichiers et de dezipper à nouveau les fichiers. Sinon, je rencontre cette erreur: `Server ERROR Exception in initialization: File size (1024) not a multiple of blocksize (8192)`, ainsi qu'une erreur 503 dans le navigateur.
9. *Créer une interface API python pour interroger l'ontologie à l'aide [sparqlwrapper](https://sparqlwrapper.readthedocs.io/en/latest/) et [sparql fuseki](https://www.youtube.com/watch?v=-ynsMc2I-CA) (voici comment utiliser sparqlwrapper pour faire des requêtes [ICI](https://sparqlwrapper.readthedocs.io/en/latest/main.html)*

	Étant donné que ce projet était surtout axé sur les prefixes, c'est donc également comme cela que j'ai axé mon API. Il ne s'agit en réalité que d'une seule fonction, mais qui est paramétré de façon à pouvoir faire la même opération qu'aux points 3-5. 
 
 ## Conclusion
 Il est difficile pour moi de tirer des vraies conclusions de ce projet. J'ai eu, tout au long, beaucoup de questionnements sur ma façon de faire. Effectivement, en temps normal pour des projets informatiques il est plutôt facile de savoir si notre opération est réussie ou pas. Dans ce projet, le seul vrai outil de vérification était le reasoner et, dans une certaine mesure, mon intelligence. Une des choses les plus difficiles durant ce projet pour moi était de surmonter ces doutes et aller de l'avant.
