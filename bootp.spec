Summary:	bootp/DHCP server and test programs
Summary(de):	bootp/DHCP-Server und Testprogramme
Summary(fr):	Serveur bootp/DHCP et programmes test
Summary(pl):	Serwer BOOTP/DHCP wraz z programami pomocniczymi
Summary(tr):	bootp/DHCP sunucusu ve test programlarý
Name:		bootp
Version:	2.4.3
Release:	10
Copyright:	BSD
Group:		Networking/Daemons
Source:		ftp://ftp.mc.com/pub/%{name}-%{version}.tar.gz
Source1:	%{name}.inetd
Patch:		bootp-2.4.3-linux.patch
Patch1:		http://www.sghms.ac.uk/~mpreston/tools.htm/dhcp.patch
Patch2:		bootp-2.4.3-glibc.patch
Patch3:		bootp-2.4.3-pathfix.patch
Patch4:		bootp-tmprace.patch
Requires:	inetdaemon
Requires:	rc-inetd
BuildRoot:	/tmp/%{name}-%{version}-root

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
#%patch4 -p1

%build
make linux SYSDEFS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/sysconfig/rc-inetd,%{_sbindir},%{_mandir}/man{5,8}}

make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir} install.man

touch $RPM_BUILD_ROOT/etc/bootptab
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/bootp

strip $RPM_BUILD_ROOT%{_sbindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{5,8}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(640,root,root) %config(noreplace) %verify(not size md5 mtime) /etc/bootptab
%attr(640,root,root) /etc/sysconfig/rc-inetd/bootp
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*
