# Supports séances en autonomie de 4TC(A)-CSC : Cryptographie et Sécurité des Communications

_Mathieu Cunche ([mathieu.cunche@insa-lyon.fr](mailto:mathieu.cunche@insa-lyon.fr)_

<!-- https://tls.ulfheim.net/ -->

[Intro](#introduction-à-la-crypto) |
[Enjeux](#enjeux-éthiques) |
[Bases](#bases-de-la-crypto) |
[PKI](#infrastructures-à-clés-publiques-pki) |
[Protocoles](#protocoles-cryptographiques) |
[Biblio](#bibliographie)

Ce document décrit le travail à réaliser pendant **les séances en autonomie**. Pour certaines séances, des ouvertures sont proposées, elles sont à lire sans trop entrer dans les détails, comme des éclairages sur le sujet. Ces ouvertures sont soit obligatoires (doivent donc être consultées), soit facultatives (j'attends que vous lisiez au moins une facultative sur l'ensemble de la matière).

Introduction à la crypto
========================

Pour cette séance, vous devez étudier l'histoire de la cryptographie et de son utilisation. Nous nous baserons pour cela d'abord sur l'article de Wikipedia qui propose un bon historique : [WikipediaFR](https://fr.wikipedia.org/wiki/Histoire_de_la_cryptologie) (environ 1 heure).

Ouverture obligatoire : [Public Key Cryptography’s Impact on Society: How Diffie and Hellman Changed the World, _Paul C. van Oorschot_](https://people.scs.carleton.ca/~paulv/papers/society-impact-of-pkc-v3.pdf). Consacrez une heure à cet article. 

<!-- Ensuite, consacrez 1 heure à la consultation de l'article [Public Key Cryptography’s Impact on Society: How Diffie and Hellman Changed the World, _Paul C. van Oorschot_](https://people.scs.carleton.ca/~paulv/papers/society-impact-of-pkc-v3.pdf). La lecture n'a pas nécessairement à être exhaustive (selon votre aise en anglais, notamment), faîtes une lecture rapide du plan et des thèmes puis approfondissez les parties de votre choix. -->


Enjeux éthiques
===============

Pour cette séance, nous allons nous intéresser aux enjeux de société liés à la cryptographie. Pour cela, vous devez consacrer le temps de préparation à lire des (parties de) documents suivants (si possible pas tous les mêmes, afin de diversifier vos apports lors de la séance de TD qui suivra) :

* [WikipediaEN : Crypto wars](https://en.wikipedia.org/wiki/Crypto_Wars)
* [Backdoor infecting VPNs used “magic packets” for stealth and security](https://arstechnica.com/security/2025/01/backdoor-infecting-vpns-used-magic-packets-for-stealth-and-security/)
* [The Risks of “Responsible Encryption”, _Riana Pfefferkorn_](https://cyberlaw.stanford.edu/publications/risks-responsible-encryption)
* [Keys Under Doormats: Mandating insecurity by requiring government access to all data and communications,_Abelson, Harold; Anderson, Ross; Bellovin, Steven M.; Benaloh, Josh; Blaze, Matt; Diffie, Whitfield; Gilmore, John; Green, Matthew; Landau, Susan; Neumann, Peter G.; Rivest, Ronald L.; Schiller, Jeffrey I.; Schneier, Bruce; Specter, Michael; Weitzner, Daniel J._](https://dspace.mit.edu/bitstream/handle/1721.1/97690/MIT-CSAIL-TR-2015-026.pdf?sequence=8)
* [The Moral Character of Cryptographic Work, _Phillip Rogaway_](http://web.cs.ucdavis.edu/~rogaway/papers/moral-fn.pdf)
* [Decrypting the encryption debate](https://www.nap.edu/catalog/25010/decrypting-the-encryption-debate-a-framework-for-decision-makers)
* [Conférence de clôture du SSTIC 2018, Patrick Pailloux, Directeur technique de la DGSE (vidéo, 1h)](https://www.sstic.org/2018/presentation/2018_cloture/)
* [Tous connectés, tous responsables, _Guillaume Poupard, Directeur général de l’ANSSI_](https://www.liberation.fr/debats/2019/01/21/securite-informatique-tous-connectes-tous-responsables_1704228/)
* Sur un mécanisme de séquestre proposé en 2018 par Ray Ozzie, lire [la proposition](https://www.wired.com/story/crypto-war-clear-encryption/), ainsi qu'au moins une critique parmi celles de [Robert Graham](https://blog.erratasec.com/2018/04/no-ray-ozzie-hasnt-solved-crypto.html), [Matthew Green](https://twitter.com/matthew_d_green/status/989222188287954945) et [Steven M. Bellovin, Matt Blaze, Dan Boneh, Susan Landau, and Ronald L. Rivest](https://arstechnica.com/information-technology/2018/05/op-ed-ray-ozzies-crypto-proposal-a-dose-of-technical-reality/).
* [Using the laws of nature to limit digital surveillance by law enforcement.](https://blog.xot.nl/2023/10/24/clearghost-using-the-laws-of-nature-to-limit-digital-surveillance-by-law-enforcement/index.html)
* Messageries sécurisées et backdoor dans la proposition de loi contre le narcotrafic : [l'ex-boss de l'ANSSI détruit l'article sur les backdoors du projet de loi Narcotrafic](https://www.clubic.com/actualite-557559-irrealiste-dangereux-et-inefficace-l-ex-boss-de-l-anssi-detruit-l-article-sur-les-backdoors-du-projet-de-loi-narcotrafic.html?utm_source=chatgpt.com)

<!-- https://citizenlab.ca/2019/09/annotated-bibliography-dual-use-technologies-network-traffic-management-and-device-intrusion-for-targeted-monitoring/ -->

Cette liste n'est bien sûr pas exhaustive, toutes les suggestions d'ajout sont les bienvenues.

Cette partie mènera à une discussion/débat lors de la séance de TD.

Voici la liste des questions : 

* Comment réguler la cryptographie ? Quels seraient les moyens techniques ?
* Estimez-vous que la communication privée soit un droit essentiel ? Privée jusqu'à quel point ? Pourquoi ? Exemples de risques ?
* Le sentiment de surveillance modifie-t-il votre comportement ? Exemples ?
* Selon vous, la surveillance de masse est-elle dangereuse pour la démocratie ? Exemples ?
* Acceptez-vous de donner vos informations à Facebook et autres GAFA ? Aux institutions étatiques ? Pourquoi ?
* Quelle est votre perception des évolutions récentes ? Qui des informations collectées dans le cadre des lois "sanitaires" ?
* Quel rôle vous voyiez vous tenir sur ces questions en tant que futur ingénieur ? 


Bases de la crypto
=================

Vous devez lire le cours de [Ghislaine Labouret](https://web.archive.org/web/20170516210655/http://www.hsc.fr/ressources/cours/crypto/crypto.pdf) <!-- http://www.hsc.fr/ressources/cours/crypto/crypto.pdf https://doc.lagout.org/security/Cryptographie%20.%20Algorithmes%20.%20Steganographie/HSC%20-%20Introduction%20a%20la%20cryptographie.pdf --> (jusqu'à la page 27/32). Vous y verrez les notions de cryptographie symétrique (ex AES), asymétrique (ex RSA), hash, chiffrement, signature ainsi que le problème de la distribution des clés. Ce cours est intéressant car bien construit mais assez ancien (2001). Les notions, principes et difficultés n'ont pas changé depuis, les algorithmes et tailles de clés si : cela vous donne une idée de l'évolution à attendre pendant les 10 prochaines années (hors découverte majeure). À vous de chercher quels sont les algorithmes souhaitables aujourd'hui. Pour les tailles de clés, le site [Key Length](http://www.keylength.com/) est très pratique.

La suite du travail est d'étudier le fonctionnement de RSA (sans entrer, pour l'instant, dans les fondements mathématiques), par exemple sur [Wikipedia](https://fr.wikipedia.org/wiki/Chiffrement_RSA). Prêtez une attention particulière à la génération des clés, aux mécanismes de chiffrement et déchiffrement.

Enfin, le programme [Bullrun](https://fr.wikipedia.org/wiki/Bullrun) donne un bon aperçu des forces et faiblesses de la cryptographie moderne : la partie mathématique est plutôt sûre, les attaques se concentrent sur l'usage (standardisation), le déploiement, l'implémentation, etc.

Ouverture (obligatoire): [La sélection de l'AES](https://videlalvaro.github.io/2014/03/you-dont-roll-your-own-crypto.html)

Ouverture (facultative):

* [L'histoire de Dual\_EC\_DRBG](https://en.wikipedia.org/wiki/Dual_EC_DRBG)
* [Listen up, FBI: Juniper code shows the problem with backdoors, _Fahmida Y. Rashid, InfoWorld_](http://www.infoworld.com/article/3018029/virtual-private-network/listen-up-fbi-juniper-code-shows-the-problem-with-backdoors.html)
* [Cryptographic competitions, _Daniel J. Bernstein_](https://eprint.iacr.org/2020/1608.pdf)

Cette section sera suivie d'une heure de questions-réponses (vous **devez** venir avec une question sur cette partie) puis conclue par le TD2 JDR.

Pour aller (un peu plus loin), je jette en vrac des lectures intéressantes : 
* [Une analyse grand publique de la surveillance de la NSA](https://www.theguardian.com/world/2013/sep/05/nsa-how-to-remain-secure-surveillance), où l'on prend un peu la mesure des capacités de la NSA en particulier. Note : on est en droit de penser que la NSA n'est pas la seule à pouvoir faire ce qu'elle peut faire, même si elle a certainement des moyens plus importants que des agences équivalentes à travers le monde (probablement de plusieurs ordre de grandeurs aux équivalents européens). 

Infrastructures à clés publiques (PKI)
=======================================

Le rôle d'une PKI est de lier une clé publique à une identité (typiquement, à une chaîne de caractères intelligible comme une URL `www.acme.org` ou une adresse mail `brice@acme.org`). L'obtention de clés publiques est un service orthogonal au service de sécurité rendu par la cryptographie (ie, un même service, le mail chiffré et signé par exemple, peut-être rendu avec une approche type CA avec S/MIME ou une approche toile de confiance avec PGP).

Vous devez lire la [page anglaise de Wikipedia](https://en.wikipedia.org/wiki/Public_key_infrastructure) sur ce sujet, qui présente différentes formes de PKI (autorités de certifications, toile de confiance, SPKI, blockchain). Attention, la page française n'est pas assez détaillée.<!-- très différente et présente une vision réduites à l'approche CA, c'est uniquement la page anglaise qui fait référence pour ce cours. -->

Vous devez détailler chacune des différentes formes, avec une attention particulière pour les [CA](https://en.wikipedia.org/wiki/Certificate_authority) et le [Web of trust](https://en.wikipedia.org/wiki/Web_of_trust). La PKI DANE/TLSA est très bien décrite et positionnée dans cet [article](http://www.bortzmeyer.org/6698.html). Vous devez enfin lire les [Criticisms](https://en.wikipedia.org/wiki/Public_key_infrastructure#Criticism) de la page principale (et les détails de PKI security issues with X.509, Breach of Comodo CA, Breach of Diginotar).

> Pour comprendre DANE/TLSA qui repose sur DNSSEC, vous devrez peut-être vous rafraichir la mémoire sur le fonctionnement et les différents acteurs du système DNS (typiquement, notions de _registry_, _registrar_, gestion d'une zone et mécanisme de résolution récursif). Ces points ont normalement déjà été vus en TC mais vous pouvez par exemple lire [Sebsauvage](http://sebsauvage.net/comprendre/dns/) jusque "Dans ce cas, ils sont à la fois registry et registrar.", [Bortzmeyer](http://www.bortzmeyer.org/files/cours-dns-cnam-PRINT.pdf) sections "Le protocole DNS" et "Gouvernance" et/ou d'autres ressources équivalentes.

Ouvertures (facultatives) :

* [Experiences Deploying Multi-Vantage-Point Domain Validation at Let's Encrypt, _Henry Birge-Lee, Liang Wang, Daniel McCarney, Roland Shoemaker, Jennifer Rexford and Prateek Mittal_](https://www.usenix.org/system/files/sec21fall-birge-lee.pdf)
* [SSL And The Future Of Authenticity, _Moxie Marlinspike (aka Mr. Signal)_](https://moxie.org/blog/ssl-and-the-future-of-authenticity/), ainsi que la [vidéo associée](https://media.defcon.org/DEF%20CON%2019/DEF%20CON%2019%20video%20and%20slides/DEF%20CON%2019%20Hacking%20Conference%20Presentation%20By%20-%20Moxie%20Marlinspike%20-%20SSL%20And%20The%20Future%20Of%20Authenticity%20-%20Video%20and%20Slides.m4v)
* [Quantifying Untrusted Symantec Certificates, _Arkadiy Tetelman_](https://arkadiyt.com/2018/02/04/quantifying-untrusted-symantec-certificates/)


<!-- moxie : https://www.youtube.com/watch?v=pDmj_xe7EIQ  https://www.youtube.com/watch?v=Z7Wl2FW2TcA  https://moxie.org/blog/ssl-and-the-future-of-authenticity/  https://media.defcon.org/DEF%20CON%2019/DEF%20CON%2019%20video%20and%20slides/DEF%20CON%2019%20Hacking%20Conference%20Presentation%20By%20-%20Moxie%20Marlinspike%20-%20SSL%20And%20The%20Future%20Of%20Authenticity%20-%20Video%20and%20Slides.m4v-->


Protocoles cryptographiques
===========================

Cette partie ne contient pas de travail personnel (uniquement le CM3 et le TP1). À la suite de ces séances, voici une liste d'ouvertures facultatives :

* [Certificate Transparency: a bird's-eye view, _Emily M. Stark_](https://emilymstark.com/2020/07/20/certificate-transparency-a-birds-eye-view.html)
* [The Security Impact of HTTPS Interception, _Zakir Durumeric et al._](https://jhalderm.com/pub/papers/interception-ndss17.pdf)
* [Annotated Bibliography on Dual-Use Technologies, _Siena Anstis, Sharly Chan, Adam Senft, and Ron Deibert_](https://citizenlab.ca/2019/09/annotated-bibliography-dual-use-technologies-network-traffic-management-and-device-intrusion-for-targeted-monitoring/)
* [SSL/TLS and PKI History](https://www.feistyduck.com/ssl-tls-and-pki-history/)



Bibliographie
=============

Livres :
* [Secure communication principles, _UKNCSC_](https://www.ncsc.gov.uk/guidance/secure-communication-principles-alpha-release)
* [The Cyber Security Body of Knowledge](https://www.cybok.org/media/downloads/CyBOK-version-1.0.pdf), en particulier le chapitre 10 dédié à la cryptographie
* Histoire des codes secrets : De l'Égypte des Pharaons à l'ordinateur quantique, _Simon Singh_
* Architectures PKI et communications sécurisées, _DUMAS Jean-Guillaume, LAFOURCADE Pascal, REDON Patrick_
* Serious Cryptography, _Jean-Philippe Aumasson_


Films :
* Mr Robot
* The Imitation Game
* Citizenfour

![xkcd](https://imgs.xkcd.com/comics/security.png)

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/fr/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/2.0/fr/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/fr/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 2.0 France</a>.
