Summary:     bootp/DHCP server and test programs
Summary(de): bootp/DHCP-Server und Testprogramme
Summary(fr): Serveur bootp/DHCP et programmes test
Summary(pl): Serwer BOOTP/DHCP wraz z programami pomocniczymi
Summary(tr): bootp/DHCP sunucusu ve test programlarý
Name:        bootp
Version:     2.4.3
Release:     8
Copyright:   BSD
Group:       Networking/Daemons
Source:      ftp://ftp.mc.com/pub/%{name}-%{version}.tar.Z
Patch:       bootp-2.4.3-linux.patch
Patch1:      http://www.sghms.ac.uk/~mpreston/tools.htm/dhcp.patch
Patch2:      bootp-2.4.3-glibc.patch
Patch3:      bootp-2.4.3-pathfix.patch
Requires:    inetd
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a server for the bootp protocol; which allows network
administrators to setup networking information for clients via an
/etc/bootptab on a server so that the clients can automatically get
their networking information. While this server includes rudimentary
DHCP support as well, we suggest using the dhcpd package if you need
DHCP support, as it is much more complete.

%description -l de
Dies ist ein Server für das bootp-Protokoll, der Netzwerkadministratoren
das Einrichten von Netzinfos für Clients über ein /etc/bootptab auf einem
Server gestattet, so daß die Clients ihre Infos automatisch bekommen. 
Obwohl dieser Server rudimentären DHCP-Support beinhaltet, 
empfehlen wir den Einsatz des dhcpd-Pakets, wenn Sie DHCP-Unterstützung
wünschen, weil sie damit umfassenderen Support erhalten.

%description -l fr
C'est un serveur pour le protocole bootp, qui permet aux administrateurs
réseau de configurer les informations pour les clients réseau via
le fichier /etc/bootptab sur un serveur de telle manière que les clients
puissent automatiquement obtenir les informations. Bien que le serveur
comprenne aussi un support rudimentaire pour dhcp, nous recommandons
d'utiliser le package dhcp si vous désirez un support dhcp, car
il est beaucoup plus complet.

%description -l pl
Pakiet ten zawiera serwer protoko³u bootp, który umo¿liwia zarz±dzanie
informacjami o konfiguracji sieciowej komputerów w pliku /etc/bootptab, a
nastêpnie dostarczenie na rz±danie w/w informacji komputerom (klientom).
Pomimo, ¿e program oferuje czê¶ciow± obs³ugê DHCP, do serwowania informacji
przenoszonych za pomoc± tego protoko³u lepiej u¿yæ dedykowanego serwera z
pakietu dhcp.

%description -l tr
bootp sunucusu, istemcilerin að bilgilerini sunucu üzerindeki bir dosyadan
almalarýna olanak verir. Bu sunucu temel DHCP desteðini içermekle birlikte,
DHCP desteðine gerek duyulan durumlarda dhcpd paketinin kullanýmý önerilir

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{sbin,man/man{5,8}}
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/sbin/*
%attr(644, root,  man) /usr/man/man[58]/*

%changelog
* Fri Sep 18 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.4.3-8]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- simplification in %install and %files,
- added using %%{name} and %%{version} in Source.

* Sat Aug 29 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [2.4.3-8]
- added pl translation,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May 13 1998 Alan Cox <alan@redhat.com>
- Fixed a potential problem with the bootfile buffer being non terminated
  allowing a theoretical exploit. We now check the buffer as we walk it. Bug
  noted and reported by Chris Evans.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- minor spec file cleanups
- now uses a build root and %attr
- requires inetd server

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
