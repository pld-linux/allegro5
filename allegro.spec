#
# Conditional build:
# --without alsa
#
Summary:	A game programming library
Summary(pl):	Biblioteka do programowania gier
Name:		allegro
Version:	4.1.6
Release:	1
License:	Giftware
Group:		Libraries
Source0:	http://belnet.dl.sourceforge.net/sourceforge/alleg/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-examples.patch
Patch2:		%{name}-alsa9.patch
URL:		http://alleg.sourceforge.net
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
%ifarch %{ix86} alpha
BuildRequires:	svgalib-devel
%endif
BuildRequires:	arts-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

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

%description devel -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania
aplikacji wykorzystuj±cych bibliotekê allegro.

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
This package contains example programs which are showing
allegro features.

%description examples -l pl
Pakiet zawiera programy przyk³adowe demonstruj±ce mo?liwo¶ci biblioteki allegro.

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

Ten pakiet zawiera biblioteki statyczne do linkowania z aplikacjami
wykorzystuj±cymi allegro.

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
Summary(pl):	Biblioteka do programowania gier - narzêdzia
Group:		Libraries
PreReq:		%{name} = %{version}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains tools.

%description tools -l pl
Allegro jest przeno¶n± bibliotek± przeznaczon± do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera narzêdzia.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
# dbglib & proflib are compiled besides normlib, so it's ok to have them here
%configure \
	--enable-static \
	--enable-dbglib \
%ifnarch %{ix86} alpha
    	--disable-vga \
	--disable-linux \
%endif
	--enable-proflib \
%ifnarch %{ix86}
	--disable-asm
%endif

	
%{__make} \
	MAKEINFO=makeinfo \
	CFLAGS="%{rpmcflags} `artsc-config --cflags` -pipe %{?!debug:-funroll-loops -ffast-math -fomit-frame-pointer} -Wall \
%ifnarch %{ix86}
	-DALLEGRO_USE_C \
%endif
	-DALLEGRO_LIB_BUILD"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man install-info install-lib \
	DESTDIR=$RPM_BUILD_ROOT

install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/4.1/

mv $RPM_BUILD_ROOT%{_bindir}/demo{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/setup{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS
%attr(755,root,root) %{_libdir}/liballeg-%{version}.so
%dir %{_libdir}/allegro/
%{_libdir}/allegro/4.1/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballd-%{version}.so
%attr(755,root,root) %{_libdir}/liballp-%{version}.so
%{_includedir}/*
%attr(755,root,root) %{_bindir}/allegro-config
%{_mandir}/man3/*
%{_infodir}/*
%{_libdir}/*_unsharable.a

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

%files static
%defattr(644,root,root,755)
%{_libdir}/liballd.a
%{_libdir}/liballeg.a
%{_libdir}/liballp.a

%ifarch %{ix86} alpha
%files svgalib
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-svgalib.so
%endif

%files dga2
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-dga2.so

%files esd
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-esddigi.so

%files arts
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-artsdigi.so

%files fbcon
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-fbcon.so

%files vga
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-vga.so

%if %{?_without_alsa:0}%{!?_without_alsa:1}
%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%{_libdir}/allegro/4.1/alleg-alsadigi.so
%{_libdir}/allegro/4.1/alleg-alsamidi.so
%endif
%endif

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
