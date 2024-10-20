# Orc_slayer
A project of a game made together with a friend of mine using Python and Pygame library.

Project report in polish:

Założenia:
Gra typu “survival”. Celem gry jest przetrwanie jak największej liczby poziomów, których trudność z czasem się zwiększa. Gracz ma za zadanie pokonać Orków za pomocą broni inspirowanej Valkirią z gry Clash Royal. Za pokonanie Orka otrzymuje monety, za które może kupić ulepszenia w sklepach. Każdy poziom posiada swoje oryginalne tło. Gra kończy się, gdy gracz straci wszystkie 3 życia. W tle gra muzyka.

Problemy i nowe pomysły:
•	Animacja ataku - Kręcąca się siekiera okazała się trudna do implementacji, ponieważ zarówno transform.rotate oraz transform.rotzoom pogarszają jakość tekstury podczas obrotu oraz mogą “zcrushować” program. Dodatkowo ciężkie było rysowanie hitboxa (recta) za każdym razem gdy broń się obróci.
o	Rozwiązanie: Udało się znaleźć poradnik dotyczący obrotu grafiki. Rozwiązaniem była osobna funkcja do umożliwienia obrotu siekiery. Kręcąca się siekiera jest tylko “animacją” a hitbox, który zabija Orków jest rysowany osobno.

•	Spawnowanie się Orków - Orki spawnowały się losowo na ekranie co powodowało, że mogłyby utworzyć się na graczu. To powodowałoby niechcianą utratę życia.
o	Rozwiązanie: Dodaliśmy cztery pola – po bokach ekranu, które częściowo wychodziły po za niego, przed pojawienie Orka losuje się, na którym polu się pojawi. Następnie losuję się w którym miejscu zostacie zrespiony.

•	Ilość Orków - początkowo zakładaliśmy że będzie się ich tworzyło dużo więcej. Jednakże już po kilku poziomach gra mocno się zwieszała.
o	Rozwiązanie: Na każdym poziomie liczba Orków się zwiększa o 1. Powoduje to, że płynność gry jest przez dłuższy czas na wysokim poziomie. 
Fail’e:
•	Zmiana tła na każdym poziomie oraz rozbudowane tła - postanowiliśmy nie ograniczać liczby poziomów do kilku/kilkunastu przed to, że każdy miałby mieć oryginalne tło , w przypadku tła, na którym znajdują się przedmioty, postać oraz orki nie mogłyby po nich chodzić, co ograniczałoby poruszanie się po mapie
•	Szczegółowe animacje - chcieliśmy dodać szczegółowe animacje, jednakże okazało się to niepraktyczne, ponieważ zmniejszało to płynność gry
•	Płynność gry – nie do uniknięcia było spowolnienie gry na wyższych poziomach, kiedy splanuje się duża lub bardzo dużą ilość Orków

Podsumowanie:
Jest to przyjemna gra, w której występują ciekawe mechaniki np. zwiększanie zasięgu broni, czy też zwiększanie trwania ataku. W przyszłości można by dodać różne poziomy trudności np. za zabicie Orka otrzymywało by się mniej monet co utrudniało by rozgrywkę. Ciekawą opcją byłoby też dodanie mini bossów na poszczególnych levelach. Praca nad grą zajęła nam około 20 godzin. Tworzenie tej gry sprawiło, że odkryliśmy możliwości Pygame’a, o których wcześniej nie wiedzieliśmy.

