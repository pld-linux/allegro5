#
# Conditional build:
# _without_alsa		- without alsa modules
# _without_arts		- without arts module
# _without_dbglib	- don't build debug versions of library
# _without_proflib	- don't debug profiling versions of library
# _without_svga		- without svgalib module
# _with_alsa5		- use alsa 0.5 not 0.9
# _without_sse		- build without sse (valgrind doesn't support it yet)
#
%define	_without_arts	1

%ifarch sparc sparc64
%define	_without_alsa	1
%endif
%{!?_without_alsa:%{!?_with_alsa5:%define _with_alsa9 1}}
Summary:	A game programming library
Summary(de):	Eine Bibliothek zur Programmierung von Spielen
Summary(es):	Una libreria de programacion de juegos
Summary(fr):	Une librairie de programmation de jeux
Summary(it):	Una libreria per la programmazione di videogiochi
Summary(pl):	Biblioteka do programowania gier
Name:		allegro
Version:	4.1.11
Release:	2
License:	Giftware
Group:		Libraries
Source0:	http://dl.sourceforge.net/alleg/%{name}-%{version}.tar.gz
# Source0-md5:	61568ff088fd074eaad8b5cc23ac40ff
Patch0:		%{name}-info.patch
Patch1:		%{name}-examples.patch
Patch2:		%{name}-alsa9.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-ldflags.patch
Patch5:		%{name}-frame-pointer.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	XFree86-devel
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
%ifarch %{ix86} alpha
%{!?_without_svga:BuildRequires:	svgalib-devel}
%endif
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l de
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.

%description -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée dans
les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei videogiochi
ed in altri tipi di programmazione multimediale.

%description -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(pl):	Biblioteka do programowania gier - pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling
applications using allegro library.

%description devel -l de
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket wird benötigt, um Programme zu bauen, die Allegro
verwenden.

%description devel -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée dans
les jeux vidéo ou d'autres types de programmation multimédia. Ce package
est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei videogiochi
ed in altri tipi di programmazione multimediale. Questo pacchetto è
necessario per compilare programmi scritti con Allegro.

%description devel -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania
aplikacji wykorzystuj±cych bibliotekê allegro.

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
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera biblioteki statyczne do konsolidacji z aplikacjami
wykorzystuj±cymi allegro.

%package debug
Summary:	liballd - debug version of shared allegro library
Summary(pl):	liballd - wersja debug dzielonej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description debug
liballd - debug version of shared allegro library (contains debugging
symbols and other information).

%description debug -l pl
liballd - wersja debug dzielonej biblioteki allegro (zawieraj±ca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package debug-static
Summary:	liballd - debug version of static allegro library
Summary(pl):	liballd - wersja debug statycznej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description debug-static
liballd - debug version of static allegro library (contains debugging
symbols and other information).

%description debug-static -l pl
liballd - wersja debug statycznej biblioteki allegro (zawieraj±ca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package profile
Summary:	liballp - profiling version of shared allegro library
Summary(pl):	liballp - wersja dzielonej biblioteki allegro s³u¿±ca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description profile
liballp - profiling version of shared allegro library.

%description profile -l pl
liballp - wersja dzielonej biblioteki allegro s³u¿±ca do profilowania.

%package profile-static
Summary:	liballp - profiling version of static allegro library
Summary(pl):	liballp - wersja statycznej biblioteki allegro s³u¿±ca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description profile-static
liballp - profiling version of static allegro library.

%description debug-static -l pl
liballp - wersja statycznej biblioteki allegro s³u¿±ca do
profilowania.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl):	Biblioteka do programowania gier - modu³ dla svgalib
Group:		Libraries
PreReq:		%{name} = %{version}

%description svgalib
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with allegro and svgalib.

%description svgalib -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania allegro z svgalibem.

%package dga2
Summary:	A game programming library - DGA2 module
Summary(pl):	Biblioteka do programowania gier - modu³ dla DGA2
Group:		Libraries
PreReq:		%{name} = %{version}

%description dga2
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with DGA.

%description dga2 -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z DGA.

%package esd
Summary:	A game programming library - esound module
Summary(pl):	Biblioteka do programowania gier - modu³ dla esound
Group:		Libraries
PreReq:		%{name} = %{version}

%description esd
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with ESound daemon.

%description esd -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z demonem ESound.

%package arts
Summary:	A game programming library - aRts module
Summary(pl):	Biblioteka do programowania gier - modu³ dla aRts
Group:		Libraries
PreReq:		%{name} = %{version}

%description arts
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with aRts.

%description arts -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z aRts.

%package fbcon
Summary:	A game programming library - framebuffer module
Summary(pl):	Biblioteka do programowania gier - modu³ dla framebuffera
Group:		Libraries
PreReq:		%{name} = %{version}

%description fbcon
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with framebuffer.

%description fbcon -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z framebufferem.

%package vga
Summary:	A game programming library - vga module
Summary(pl):	Biblioteka do programowania gier - modu³ dla vga
Group:		Libraries
PreReq:		%{name} = %{version}

%description vga
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with vga.

%description vga -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z vga.

%package alsa9
Summary:	A game programming library - ALSA 0.9 modules
Summary(pl):	Biblioteka do programowania gier - modu³y dla ALSA 0.9
Group:		Libraries
PreReq:		%{name} = %{version}

%description alsa9
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA 0.9 sound library.

%description alsa9 -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³y do wykorzystania z bibliotek± d¼wiêkow±
ALSA 0.9.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl):	Biblioteka do programowania gier - modu³y dla ALSA
Group:		Libraries
PreReq:		%{name} = %{version}

%description alsa
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA sound library.

%description alsa -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³y do wykorzystania z bibliotek± d¼wiêkow±
ALSA.

%package tools
Summary:	A game programming library - tools
Summary(de):	Zusätzliche Hilfprogramme für die Allegro Bibliothek
Summary(es):	Herramientas adicionales para la librería de programación Allegro
Summary(fr):	Outils supplémentaires pour la librairie de programmation Allegro
Summary(it):	Programmi di utilità aggiuntivi per la libreria Allegro
Summary(pl):	Biblioteka do programowania gier - narzêdzia
Group:		Libraries
PreReq:		%{name} = %{version}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains tools.

%description tools -l de
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket enthält Programme, die für die Entwicklung von
Allegro Programmen hilfreich sind.

%description tools -l es
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr
Allegro est une librairie multi-plateforme destinée à être utilisée dans
les jeux vidéo ou d'autres types de programmation multimédia. Ce package
contient des outils supplémentaires qui sont utiles pour le développement
de programmes avec Allegro.

%description tools -l it
Allegro è una libreria multipiattaforma dedicata all'uso nei videogiochi
ed in altri tipi di programmazione multimediale. Questo pacchetto
contiene programmi di utilità aggiuntivi utili allo sviluppo di programmi
con Allegro.

%description tools -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera narzêdzia.

%package tests
Summary:	A game programming library - test programs
Summary(pl):	Biblioteka do programowania gier - programy testuj±ce
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description tests
This package contains programs for testing allegro library.

%description tests -l pl
Pakiet zawiera programy testuj±ce bibliotekê allegro.

%package examples
Summary:	A game programming library - examples
Summary(pl):	Biblioteka do programowania gier - programy przyk³adowe
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description examples
This package contains example programs which demonstrate allegro
features.

%description examples -l pl
Pakiet zawiera programy przyk³adowe demonstruj±ce mo¿liwo¶ci
biblioteki allegro.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{!?_without_alsa:%patch2 -p1}
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__aclocal}
%{__autoheader} configure.in > include/allegro/platform/alunixac.hin
%{__autoconf}
TARGET_ARCH="%{rpmcflags}" export TARGET_ARCH
# dbglib & proflib are compiled besides normlib, so it's ok to have them here
%configure \
	--enable-static \
	%{?_without_svga:--disable-svgalib} \
	%{!?_without_dbglib:--enable-dbglib} \
%ifnarch %{ix86} alpha
	--disable-vga \
	--disable-linux \
%endif
	%{!?_without_proflib:--enable-proflib} \
	%{?_without_arts:--disable-artsdigi} \
	%{?_without_sse:--disable-sse} \
	%{?_without_sse:--disable-asm} \
%ifnarch %{ix86}
	--disable-asm \
	--disable-mmx \
	--disable-sse
%endif

%{__make} \
	MAKEINFO=makeinfo

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man install-info install-lib \
	DESTDIR=$RPM_BUILD_ROOT

install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/4.1

mv $RPM_BUILD_ROOT%{_bindir}/demo{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/setup{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS
%attr(755,root,root) %{_libdir}/liballeg-%{version}.so
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/4.1
%{_libdir}/allegro/4.1/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/allegro-config
%{_libdir}/liballeg_unsharable.a
%{_includedir}/*
%{_mandir}/man3/*
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/liballeg.a

%if 0%{!?_without_dbglib:1}
%files debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballd-%{version}.so
%{_libdir}/liballd_unsharable.a

%files debug-static
%defattr(644,root,root,755)
%{_libdir}/liballd.a
%endif

%if 0%{!?_without_proflib:1}
%files profile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballp-%{version}.so
%{_libdir}/liballp_unsharable.a

%files profile-static
%defattr(644,root,root,755)
%{_libdir}/liballp.a
%endif

%if %{!?_without_svga:1}0
%ifarch %{ix86} alpha
%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-svgalib.so
%endif
%endif

%files dga2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-dga2.so

%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-esddigi.so

%if 0%{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-artsdigi.so
%endif

%files fbcon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-fbcon.so

%files vga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-vga.so

%if 0%{?_with_alsa5:1}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-alsadigi.so
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-alsamidi.so
%endif

%if 0%{?_with_alsa9:1}
%files alsa9
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-alsa9digi.so
%attr(755,root,root) %{_libdir}/allegro/4.1/alleg-alsa9midi.so
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/colormap
%attr(755,root,root) %{_bindir}/exedat
%attr(755,root,root) %{_bindir}/pack
%attr(755,root,root) %{_bindir}/rgbmap
%attr(755,root,root) %{_bindir}/textconv
%attr(755,root,root) %{_bindir}/dat
%attr(755,root,root) %{_bindir}/dat2c
%attr(755,root,root) %{_bindir}/dat2s
%attr(755,root,root) %{_bindir}/grabber
%attr(755,root,root) %{_bindir}/pat2dat
%attr(755,root,root) %{_bindir}/setup-allegro
%attr(755,root,root) %{_bindir}/keyconf

%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afinfo
%attr(755,root,root) %{_bindir}/akaitest
%attr(755,root,root) %{_bindir}/demo-allegro
%attr(755,root,root) %{_bindir}/digitest
%attr(755,root,root) %{_bindir}/filetest
%attr(755,root,root) %{_bindir}/gfxinfo
%attr(755,root,root) %{_bindir}/mathtest
%attr(755,root,root) %{_bindir}/miditest
%attr(755,root,root) %{_bindir}/play-allegro
%attr(755,root,root) %{_bindir}/playfli
%attr(755,root,root) %{_bindir}/test-allegro
%attr(755,root,root) %{_bindir}/vesainfo

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex12bit
%attr(755,root,root) %{_bindir}/ex3buf
%attr(755,root,root) %{_bindir}/ex3d
%attr(755,root,root) %{_bindir}/exaccel
%attr(755,root,root) %{_bindir}/exalpha
%attr(755,root,root) %{_bindir}/exbitmap
%attr(755,root,root) %{_bindir}/exblend
%attr(755,root,root) %{_bindir}/excamera
%attr(755,root,root) %{_bindir}/excolmap
%attr(755,root,root) %{_bindir}/exconfig
%attr(755,root,root) %{_bindir}/excustom
%attr(755,root,root) %{_bindir}/exdata
%attr(755,root,root) %{_bindir}/exdbuf
%attr(755,root,root) %{_bindir}/exdodgy
%attr(755,root,root) %{_bindir}/exexedat
%attr(755,root,root) %{_bindir}/exfixed
%attr(755,root,root) %{_bindir}/exflame
%attr(755,root,root) %{_bindir}/exflip
%attr(755,root,root) %{_bindir}/exgui
%attr(755,root,root) %{_bindir}/exhello
%attr(755,root,root) %{_bindir}/exjoy
%attr(755,root,root) %{_bindir}/exkeys
%attr(755,root,root) %{_bindir}/exlights
%attr(755,root,root) %{_bindir}/exmem
%attr(755,root,root) %{_bindir}/exmidi
%attr(755,root,root) %{_bindir}/exmouse
%attr(755,root,root) %{_bindir}/expal
%attr(755,root,root) %{_bindir}/expat
%attr(755,root,root) %{_bindir}/exquat
%attr(755,root,root) %{_bindir}/exrgbhsv
%attr(755,root,root) %{_bindir}/exsample
%attr(755,root,root) %{_bindir}/exscale
%attr(755,root,root) %{_bindir}/exscn3d
%attr(755,root,root) %{_bindir}/exscroll
%attr(755,root,root) %{_bindir}/exshade
%attr(755,root,root) %{_bindir}/exspline
%attr(755,root,root) %{_bindir}/exsprite
%attr(755,root,root) %{_bindir}/exstars
%attr(755,root,root) %{_bindir}/exstream
%attr(755,root,root) %{_bindir}/exswitch
%attr(755,root,root) %{_bindir}/extimer
%attr(755,root,root) %{_bindir}/extrans
%attr(755,root,root) %{_bindir}/extruec
%attr(755,root,root) %{_bindir}/exunicod
%attr(755,root,root) %{_bindir}/exupdate
%attr(755,root,root) %{_bindir}/exxfade
%attr(755,root,root) %{_bindir}/exzbuf
