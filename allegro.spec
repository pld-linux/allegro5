Summary:	A game programming library
Summary(pl):	Biblioteka do programowania gier
Name:		allegro
Version:	3.9.38
Release:	1
License:	giftware
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����
Source0:	http://prdownloads.sourceforge.net/alleg/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.talula.demon.co.uk/allegro/
BuildRequires:	esound-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	svgalib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(pl):	Biblioteka do programowania gier - pliki nag��wkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling applications
using allegro library.

%description devel -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania aplikacji
wykorzystuj�cych bibliotek� allegro.

%package static
Summary:	A game programming library - static libraries
Summary(pl):	Biblioteka do programowania gier - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains static libraries for linking with allegro
applications.

%description static -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera biblioteki statyczne do linkowania z aplikacjami
wykorzystuj�cymi allegro.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl):	Biblioteka do programowania gier - modu� dla svgalib
Group:		Libraries
PreReq:		%{name} = %{version}

%description svgalib
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with allegro and svgalib.

%description svgalib -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania allegro z svgalibem.

%package dga2
Summary:	A game programming library - DGA2 module
Summary(pl):	Biblioteka do programowania gier - modu� dla DGA2
Group:		Libraries
PreReq:		%{name} = %{version}

%description dga2
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with DGA.

%description dga2 -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z DGA.

%package esd
Summary:	A game programming library - esound module
Summary(pl):	Biblioteka do programowania gier - modu� dla esound
Group:		Libraries
PreReq:		%{name} = %{version}

%description esd
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with ESound daemon.

%description esd -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu� do wykorzystania z demonem ESound.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl):	Biblioteka do programowania gier - modu�y dla ALSA
Group:		Libraries
PreReq:		%{name} = %{version}

%description alsa
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA sound library.

%description alsa -l pl
Allegro jest przeno�n� bibliotek� przeznaczon� do wykorzystania w grach
komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu�y do wykorzystania z bibliotek� d�wi�kow� ALSA.

%prep
%setup  -q
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	DESTDIR=$RPM_BUILD_ROOT \
	install \
	install-man \
	install-info

gzip -9nf AUTHORS CHANGES THANKS

echo -e "# List of modules to be loaded by the Unix version of Allegro.\n" \
	> $RPM_BUILD_ROOT%{_libdir}/allegro/modules.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colormap
%attr(755,root,root) %{_bindir}/exedat
%attr(755,root,root) %{_bindir}/pack
%attr(755,root,root) %{_bindir}/rgbmap
%attr(755,root,root) %{_bindir}/textconv
%attr(755,root,root) %{_bindir}/dat
%attr(755,root,root) %{_bindir}/dat2s
%attr(755,root,root) %{_bindir}/grabber
%attr(755,root,root) %{_bindir}/pat2dat
%attr(755,root,root) %{_libdir}/*.so
%dir %{_libdir}/allegro
%{_libdir}/allegro/modules.lst

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_bindir}/allegro-config
%{_mandir}/man3/*
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files svgalib
%defattr(644,root,root,755)
%{_libdir}/allegro/alleg-svgalib-%{version}.so

%files dga2
%defattr(644,root,root,755)
%{_libdir}/allegro/alleg-dga2-%{version}.so

%files esd
%defattr(644,root,root,755)
%{_libdir}/allegro/alleg-esddigi-%{version}.so

%files alsa
%defattr(644,root,root,755)
%{_libdir}/allegro/alleg-alsadigi-%{version}.so
%{_libdir}/allegro/alleg-alsamidi-%{version}.so
