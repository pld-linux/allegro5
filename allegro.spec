Summary:	A game programming library
Summary(pl):	Biblioteka do programowania gier
Name:		allegro
Version:	4.0.2
Release:	0.1
License:	Giftware
Group:		X11/Libraries
Source0:	http://belnet.dl.sourceforge.net/sourceforge/alleg/%{name}-%{version}-rc2.tar.gz
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-info.patch
#Patch2:	%{name}-alsa9.patch
Patch3:		%{name}-examples.patch
URL:		http://alleg.sourceforge.net
BuildRequires:	XFree86-devel
BuildRequires:	esound-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
%ifarch %{ix86}
BuildRequires:	svgalib-devel
%endif
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(pl):	Biblioteka do programowania gier - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling
applications using allegro library.

%description devel -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania
aplikacji wykorzystuj±cych bibliotekê allegro.

%package tests
Summary:	A game programming library - test programs
Summary(pl):	Biblioteka do programowania gier - programy testuj±ce
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description tests
This package contains programs for testing allegro library.

%description tests -l pl
Pakiet zawiera programy testuj±ce bibliotekê allegro.

%package examples
Summary:	A game programming library - examples
Summary(pl):	Biblioteka do programowania gier - programy przyk³adowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description examples
This package contains example programs which are showing
allegro features.

%description examples -l pl
Pakiet zawiera programy przyk³adowe demonstruj±ce mo?liwo¶ci biblioteki allegro.

%package static
Summary:	A game programming library - static libraries
Summary(pl):	Biblioteka do programowania gier - biblioteki statyczne
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains static libraries for linking with allegro
applications.

%description static -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera biblioteki statyczne do linkowania z aplikacjami
wykorzystuj±cymi allegro.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl):	Biblioteka do programowania gier - modu³ dla svgalib
Group:		X11/Libraries
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
Group:		X11/Libraries
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
Group:		X11/Libraries
PreReq:		%{name} = %{version}

%description esd
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with ESound daemon.

%description esd -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera modu³ do wykorzystania z demonem ESound.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl):	Biblioteka do programowania gier - modu³y dla ALSA
Group:		X11/Libraries
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

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
aclocal
%{__autoconf}
%configure \
	--enable-static \
	--enable-dbglib \
	--enable-proflib \
%ifnarch %{ix86}
    	--disable-vga \
	--disable-linux
%endif
	
%{__make} MAKEINFO=makeinfo

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man install-info \
	DESTDIR=$RPM_BUILD_ROOT

echo -e "# List of modules to be loaded by the Unix version of Allegro.\n" \
	> $RPM_BUILD_ROOT%{_libdir}/allegro/4.0/modules.lst

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS
%attr(755,root,root) %{_libdir}/liballeg-%{version}.so
%dir %{_libdir}/allegro/
%{_libdir}/allegro/4.0/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballd-%{version}.so
%attr(755,root,root) %{_libdir}/liballp-%{version}.so
%{_includedir}/*
%attr(755,root,root) %{_bindir}/allegro-config
%attr(755,root,root) %{_bindir}/colormap
%attr(755,root,root) %{_bindir}/exedat
%attr(755,root,root) %{_bindir}/pack
%attr(755,root,root) %{_bindir}/rgbmap
%attr(755,root,root) %{_bindir}/textconv
%attr(755,root,root) %{_bindir}/dat
%attr(755,root,root) %{_bindir}/dat2s
%attr(755,root,root) %{_bindir}/grabber
%attr(755,root,root) %{_bindir}/pat2dat
%{_mandir}/man3/*
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%ifarch %{ix86}
%files svgalib
%defattr(644,root,root,755)
%{_libdir}/allegro/4.0/alleg-svgalib.so
%endif

%files dga2
%defattr(644,root,root,755)
%{_libdir}/allegro/4.0/alleg-dga2.so

%files esd
%defattr(644,root,root,755)
%{_libdir}/allegro/4.0/alleg-esddigi.so

%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%{_libdir}/allegro/4.0/alleg-alsadigi.so
%{_libdir}/allegro/4.0/alleg-alsamidi.so
%endif

%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afinfo
%attr(755,root,root) %{_bindir}/akaitest
%attr(755,root,root) %{_bindir}/digitest
%attr(755,root,root) %{_bindir}/filetest
%attr(755,root,root) %{_bindir}/gfxinfo
%attr(755,root,root) %{_bindir}/mathtest
%attr(755,root,root) %{_bindir}/miditest
%attr(755,root,root) %{_bindir}/play
%attr(755,root,root) %{_bindir}/playfli
%attr(755,root,root) %{_bindir}/test
%attr(755,root,root) %{_bindir}/vesainfo

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex12bit
%attr(755,root,root) %{_bindir}/ex3buf
%attr(755,root,root) %{_bindir}/ex3d
%attr(755,root,root) %{_bindir}/exalpha
%attr(755,root,root) %{_bindir}/exbitmap
%attr(755,root,root) %{_bindir}/exblend
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
%attr(755,root,root) %{_bindir}/exshade
%attr(755,root,root) %{_bindir}/exspline
%attr(755,root,root) %{_bindir}/exsprite
%attr(755,root,root) %{_bindir}/exstars
%attr(755,root,root) %{_bindir}/exstream
%attr(755,root,root) %{_bindir}/extimer
%attr(755,root,root) %{_bindir}/extrans
%attr(755,root,root) %{_bindir}/exupdate
%attr(755,root,root) %{_bindir}/exxfade
%attr(755,root,root) %{_bindir}/exzbuf
