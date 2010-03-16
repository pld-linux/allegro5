#
# TODO: - check (and update if required) allegro-frame-pointer.patch
#	- force install man pages (sometimes it just doesn't work)
#	- check allegro-vga and allegro-svga packages if they should contains any files
#	- unpackaged files
#
# Conditional build:
%bcond_without	alsa	# without ALSA modules
%bcond_without	dga2	# without DGA2 module
%bcond_without	jack	# without JACK module
%bcond_without	svga	# without svgalib module
%bcond_without	vga	# without vga module
#
Summary:	A game programming library
Summary(de.UTF-8):	Eine Bibliothek zur Programmierung von Spielen
Summary(es.UTF-8):	Una biblioteca de programación de juegos
Summary(fr.UTF-8):	Une librairie de programmation de jeux
Summary(it.UTF-8):	Una libreria per la programmazione di videogiochi
Summary(pl.UTF-8):	Biblioteka do programowania gier
Name:		allegro
Version:	4.4.1.1
Release:	0.1
License:	Giftware
Group:		Libraries
Source0:	http://downloads.sourceforge.net/alleg/%{name}-%{version}.tar.gz
# Source0-md5:	0f1cfff8f2cf88e5c91a667d9fd386ec
Patch0:		%{name}-info.patch
#Patch1: %{name}-frame-pointer.patch
Patch2:		%{name}-config.patch
URL:		http://alleg.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	cmake >= 2.6
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

%description -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.

%description -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia.

%description -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia.

%description -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale.

%description -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

%package devel
Summary:	A game programming library - header files
Summary(es.UTF-8):	Archivos de inclusión
Summary(pl.UTF-8):	Biblioteka do programowania gier - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains header files neccessary for compiling
applications using allegro library.

%description devel -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket wird benötigt, um Programme zu bauen, die Allegro
verwenden.

%description devel -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete es necesario para compilar los programas que usen Allegro.

%description devel -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package est nécessaire pour compiler les programmes utilisant Allegro.

%description devel -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto è necessario per compilare programmi scritti con Allegro.

%description devel -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilowania
aplikacji wykorzystujących bibliotekę allegro.

%package static
Summary:	A game programming library - static libraries
Summary(pl.UTF-8):	Biblioteka do programowania gier - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXxf86vm-devel

%description static
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains static libraries for linking with allegro
applications.

%description static -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera biblioteki statyczne do konsolidacji z aplikacjami
wykorzystującymi allegro.

%package svgalib
Summary:	A game programming library - svgalib module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla svgalib
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description svgalib
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with allegro and svgalib.

%description svgalib -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania allegro z svgalibem.

%package dga2
Summary:	A game programming library - DGA2 module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla DGA2
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dga2
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with DGA.

%description dga2 -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z DGA.

%package vga
Summary:	A game programming library - vga module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla vga
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description vga
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with vga.

%description vga -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z vga.

%package alsa
Summary:	A game programming library - ALSA modules
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduły dla ALSA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-alsa9

%description alsa
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains modules for use with ALSA sound library.

%description alsa -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduły do wykorzystania z biblioteką dźwiękową
ALSA.

%package jack
Summary:	A game programming library - JACK module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla JACK-a
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description jack
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains module for use with JACK sound library.

%description jack -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z biblioteką dźwiękową JACK.

%package tools
Summary:	A game programming library - tools
Summary(de.UTF-8):	Zusätzliche Hilfprogramme für die Allegro Bibliothek
Summary(es.UTF-8):	Herramientas adicionales para la librería de programación Allegro
Summary(fr.UTF-8):	Outils supplémentaires pour la librairie de programmation Allegro
Summary(it.UTF-8):	Programmi di utilità aggiuntivi per la libreria Allegro
Summary(pl.UTF-8):	Biblioteka do programowania gier - narzędzia
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains tools.

%description tools -l de.UTF-8
Allegro ist eine plattformübergreifende Bibliothek zur Verwendung in
Computerspielen und anderen Formen von Multinediaprogrammierung.
Dieses Paket enthält Programme, die für die Entwicklung von Allegro
Programmen hilfreich sind.

%description tools -l es.UTF-8
Allegro es una librería multi-plataforma creada para ser usada en la
programación de juegos u otro tipo de programación multimedia. Este
paquete contiene herramientas adicionales que son útiles para
desarrollar programas que usen Allegro.

%description tools -l fr.UTF-8
Allegro est une librairie multi-plateforme destinée à être utilisée
dans les jeux vidéo ou d'autres types de programmation multimédia. Ce
package contient des outils supplémentaires qui sont utiles pour le
développement de programmes avec Allegro.

%description tools -l it.UTF-8
Allegro è una libreria multipiattaforma dedicata all'uso nei
videogiochi ed in altri tipi di programmazione multimediale. Questo
pacchetto contiene programmi di utilità aggiuntivi utili allo sviluppo
di programmi con Allegro.

%description tools -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera narzędzia.

%package tests
Summary:	A game programming library - test programs
Summary(pl.UTF-8):	Biblioteka do programowania gier - programy testujące
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description tests
This package contains programs for testing allegro library.

%description tests -l pl.UTF-8
Pakiet zawiera programy testujące bibliotekę allegro.

%package examples
Summary:	A game programming library - examples
Summary(pl.UTF-8):	Biblioteka do programowania gier - programy przykładowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs which demonstrate allegro
features.

%description examples -l pl.UTF-8
Pakiet zawiera programy przykładowe demonstrujące możliwości
biblioteki allegro.

%prep
%setup -q
%patch0 -p1
#%%patch1 -p1
%patch2 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DMANDIR=%{_mandir} \
	-DINFODIR=%{_infodir} \
	%{!?with_vga:-DWANT_LINUX_VGA=off} \
	%{!?with_svga:-DWANT_LINUX_SVGALIB=off} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/%{version}

# install examples and tests
find build/examples -perm 755 -maxdepth 1 -name "ex*" -exec install {} $RPM_BUILD_ROOT%{_bindir} \;
find build/tests -perm 755 -maxdepth 1 ! -name CMakeFiles -exec install {} $RPM_BUILD_ROOT%{_bindir} \;

mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

%clean
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES THANKS readme.txt todo.txt
%attr(755,root,root) %{_libdir}/liballeg.so.*.*.*
%attr(755,root,root) %{_libdir}/liballeg.so
%dir %{_libdir}/allegro
%dir %{_libdir}/allegro/4.4.1
%{_libdir}/allegro/4.4.1/modules.lst

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/allegro-config
%{_includedir}/*
#%%{_mandir}/man3/*
%{_infodir}/*.info*

%if %{with svga}
%files svgalib
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-svgalib.so
%endif

%if %{with dga2}
%files dga2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.4.1/alleg-dga2.so
%endif

%ifarch %{ix86}
%if %{with vga}
%files vga
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-vga.so
%endif
%endif

%if %{with alsa}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.4.1/alleg-alsadigi.so
%attr(755,root,root) %{_libdir}/allegro/4.4.1/alleg-alsamidi.so
%endif

%if %{with jack}
%files jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/allegro/4.4.1/alleg-jack.so
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

%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afinfo
%attr(755,root,root) %{_bindir}/akaitest
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
%attr(755,root,root) %{_bindir}/exexedat
%attr(755,root,root) %{_bindir}/exfixed
%attr(755,root,root) %{_bindir}/exflame
%attr(755,root,root) %{_bindir}/exflip
%attr(755,root,root) %{_bindir}/exfont
%attr(755,root,root) %{_bindir}/exgui
%attr(755,root,root) %{_bindir}/exhello
%attr(755,root,root) %{_bindir}/exjoy
%attr(755,root,root) %{_bindir}/exkeys
%attr(755,root,root) %{_bindir}/exlights
%attr(755,root,root) %{_bindir}/exmem
%attr(755,root,root) %{_bindir}/exmidi
%attr(755,root,root) %{_bindir}/exmouse
%attr(755,root,root) %{_bindir}/expackf
%attr(755,root,root) %{_bindir}/expal
%attr(755,root,root) %{_bindir}/expat
%attr(755,root,root) %{_bindir}/exquat
%attr(755,root,root) %{_bindir}/exrgbhsv
%attr(755,root,root) %{_bindir}/exrotscl
%attr(755,root,root) %{_bindir}/extrans2
%attr(755,root,root) %{_bindir}/exsample
%attr(755,root,root) %{_bindir}/exsyscur
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
