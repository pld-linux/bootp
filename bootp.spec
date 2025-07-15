Summary:	bootp/DHCP server and test programs
Summary(de.UTF-8):	bootp/DHCP-Server und Testprogramme
Summary(fr.UTF-8):	Serveur bootp/DHCP et programmes test
Summary(pl.UTF-8):	Serwer bootp/DHCP wraz z programami pomocniczymi
Summary(tr.UTF-8):	bootp/DHCP sunucusu ve test programları
Name:		bootp
Version:	2.4.3
Release:	12
License:	BSD
Group:		Networking/Daemons
Source0:	ftp://ftp.ntplx.net/pub/networking/bootp/%{name}-%{version}.tar.gz
# Source0-md5:	2a12d862f11908acf84652387be4e03b
Source1:	%{name}.inetd
Patch0:		%{name}-2.4.3-linux.patch
Patch1:		http://www.sghms.ac.uk/~mpreston/tools.htm/dhcp.patch
Patch2:		%{name}-2.4.3-glibc.patch
Patch3:		%{name}-2.4.3-pathfix.patch
Patch4:		%{name}-tmprace.patch
Patch5:		%{name}-errno.patch
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	inetdaemon
Requires:	rc-inetd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a server for the bootp protocol; which allows network
administrators to setup networking information for clients via an
/etc/bootptab on a server so that the clients can automatically get
their networking information. While this server includes rudimentary
DHCP support as well, we suggest using the dhcpd package if you need
DHCP support, as it is much more complete.

%description -l de.UTF-8
Dies ist ein Server für das bootp-Protokoll, der
Netzwerkadministratoren das Einrichten von Netzinfos für Clients über
ein /etc/bootptab auf einem Server gestattet, so daß die Clients ihre
Infos automatisch bekommen. Obwohl dieser Server rudimentären
DHCP-Support beinhaltet, empfehlen wir den Einsatz des dhcpd-Pakets,
wenn Sie DHCP-Unterstützung wünschen, weil sie damit umfassenderen
Support erhalten.

%description -l fr.UTF-8
C'est un serveur pour le protocole bootp, qui permet aux
administrateurs réseau de configurer les informations pour les clients
réseau via le fichier /etc/bootptab sur un serveur de telle manière
que les clients puissent automatiquement obtenir les informations.
Bien que le serveur comprenne aussi un support rudimentaire pour dhcp,
nous recommandons d'utiliser le package dhcp si vous désirez un
support dhcp, car il est beaucoup plus complet.

%description -l pl.UTF-8
Pakiet ten zawiera serwer protokołu bootp, który umożliwia zarządzanie
informacjami o konfiguracji sieciowej komputerów w pliku
/etc/bootptab, a następnie dostarczenie na żądanie w/w informacji
komputerom (klientom). Pomimo, że program oferuje częściową obsługę
DHCP, do serwowania informacji przenoszonych za pomocą tego protokołu
lepiej użyć dedykowanego serwera z pakietu dhcp.

%description -l tr.UTF-8
bootp sunucusu, istemcilerin ağ bilgilerini sunucu üzerindeki bir
dosyadan almalarına olanak verir. Bu sunucu temel DHCP desteğini
içermekle birlikte, DHCP desteğine gerek duyulan durumlarda dhcpd
paketinin kullanımı önerilir

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
#%%patch4 -p1
%patch -P5 -p1

%build
%{__make} linux SYSDEFS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/sysconfig/rc-inetd,%{_sbindir},%{_mandir}/man{5,8}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

touch $RPM_BUILD_ROOT%{_sysconfdir}/bootptab
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/bootp

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q rc-inetd reload

%postun
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bootptab
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/bootp
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[58]/*
