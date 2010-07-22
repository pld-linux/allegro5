#
# TODO: - Handle situations when there are no modules (most bconds turned off)
#	- make bconds work again or remove
#
# Conditional build:
%bcond_without	alsa	# without ALSA modules
#%%bcond_without	arts	# without aRts module
#%%bcond_without	dga2	# without DGA2 module
#%%bcond_without	dbglib	# don't build debug versions of library
#%%bcond_without	esd	# without esound module
#%%bcond_without	fbcon	# without framebuffer module
#%%bcond_without	jack	# without JACK module
#%%bcond_without	proflib	# don't debug profiling versions of library
#%%bcond_without	sse	# build without sse
%bcond_without	static	# don't build static versions of library
#%%bcond_without	svga	# without svgalib module
#%%bcond_without	vga	# without vga module
#
Summary:	A game programming library
Summary(de.UTF-8):	Eine Bibliothek zur Programmierung von Spielen
Summary(es.UTF-8):	Una biblioteca de programación de juegos
Summary(fr.UTF-8):	Une librairie de programmation de jeux
Summary(it.UTF-8):	Una libreria per la programmazione di videogiochi
Summary(pl.UTF-8):	Biblioteka do programowania gier
Name:		allegro
Version:	4.9.20
Release:	0.1
License:	Giftware
Group:		Libraries
Source0:	http://downloads.sourceforge.net/alleg/%{name}-%{version}.tar.gz
# Source0-md5:	3efd906549df2f3d96d6775f955f1be7
Patch0:		%{name}-info.patch
Patch1:		%{name}-examples.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-frame-pointer.patch
Patch4:		%{name}-config.patch
URL:		http://alleg.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
#%%{?with_arts:BuildRequires:	artsc-devel}
BuildRequires:	cmake >= 2.6
BuildRequires:	curl-devel
#%%{?with_esd:BuildRequires:	esound-devel}
#%%if %{with jack}
#BuildRequires:	jack-audio-connection-kit-devel
#BuildRequires:	physfs-devel
#BuildRequires:	pkgconfig
#%%endif
#BuildRequires:	sed >= 4.0
#%%{?with_svga:BuildRequires:	svgalib-devel}
#BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
#BuildRequires:	xorg-lib-libXxf86dga-devel
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

%package debug
Summary:	liballd - debug version of shared allegro library
Summary(pl.UTF-8):	liballd - wersja debug dzielonej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description debug
liballd - debug version of shared allegro library (contains debugging
symbols and other information).

%description debug -l pl.UTF-8
liballd - wersja debug dzielonej biblioteki allegro (zawierająca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package debug-static
Summary:	liballd - debug version of static allegro library
Summary(pl.UTF-8):	liballd - wersja debug statycznej biblioteki allegro
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description debug-static
liballd - debug version of static allegro library (contains debugging
symbols and other information).

%description debug-static -l pl.UTF-8
liballd - wersja debug statycznej biblioteki allegro (zawierająca
symbole i inne informacje potrzebne przy odpluskwianiu).

%package profile
Summary:	liballp - profiling version of shared allegro library
Summary(pl.UTF-8):	liballp - wersja dzielonej biblioteki allegro służąca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description profile
liballp - profiling version of shared allegro library.

%description profile -l pl.UTF-8
liballp - wersja dzielonej biblioteki allegro służąca do profilowania.

%package profile-static
Summary:	liballp - profiling version of static allegro library
Summary(pl.UTF-8):	liballp - wersja statycznej biblioteki allegro służąca do profilowania
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description profile-static
liballp - profiling version of static allegro library.

%description profile-static -l pl.UTF-8
liballp - wersja statycznej biblioteki allegro służąca do
profilowania.

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

%package esd
Summary:	A game programming library - esound module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla esound
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description esd
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with ESound daemon.

%description esd -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z demonem ESound.

%package arts
Summary:	A game programming library - aRts module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla aRts
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description arts
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with aRts.

%description arts -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z aRts.

%package fbcon
Summary:	A game programming library - framebuffer module
Summary(pl.UTF-8):	Biblioteka do programowania gier - moduł dla framebuffera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fbcon
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming.

This package contains a esound module for use with framebuffer.

%description fbcon -l pl.UTF-8
Allegro jest przenośną biblioteką przeznaczoną do wykorzystania w
grach komputerowych i innych rodzajach oprogramowania multimedialnego.

Ten pakiet zawiera moduł do wykorzystania z framebufferem.

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
#%%patch0 -p1
#%%patch1 -p1
#%%patch2 -p1
#%%patch3 -p1
#%%patch4 -p1

#find include/allegro5 -name '*.h' -print0 | xargs -0 %{__sed} -i -e 's@allegro5/@%{_headers_dir}/include/allegro5@'
#%%{__sed} -i -e 's@allegro5/@../@' include/allegro5/internal/alconfig.h

%build
#TARGET_ARCH="%{rpmcflags}" export TARGET_ARCH
# dbglib & proflib are compiled besides normlib, so it's ok to have them here
#%%configure \
#%	%{?with_dbglib:--enable-dbglib} \
#%	%{?with_proflib:--enable-proflib} \
#%%endif
#%	%{!?with_arts:--disable-artsdigi} \
#%	%{!?with_dga2:--disable-xwin-dga2} \
#%	%{!?with_esd:--disable-esddigi} \
#%	%{!?with_fbcon:--disable-fbcon} \
#%	%{!?with_jack:--disable-jackdigi} \
#%	%{!?with_svga:--disable-svgalib} \
#%	%{!?with_vga:--disable-vga} \
#%%if !%{with sse}
#	--disable-sse \
#	--disable-asm \
#%%endif
#%%ifnarch %{ix86}
#	--disable-asm \
#	--disable-mmx \
#	--disable-sse
#%%endif
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DMANDIR=%{_mandir} \
	-DINFODIR=%{_infodir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

#install modules.lst $RPM_BUILD_ROOT%{_libdir}/allegro/%{version}

# install examples and tests
find build/examples -maxdepth 1 -perm 755 -name "ex*" -exec install {} $RPM_BUILD_ROOT%{_bindir} \;
#find build/tests -maxdepth 1 -perm 755 ! -name CMakeFiles -exec install {} $RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_bindir}/demo{,-allegro}
#mv $RPM_BUILD_ROOT%{_bindir}/play{,-allegro}
#mv $RPM_BUILD_ROOT%{_bindir}/setup{,-allegro}
#mv $RPM_BUILD_ROOT%{_bindir}/test{,-allegro}

# help rpm to find reqs for ELF objects
#chmod 755 $RPM_BUILD_ROOT%{_libdir}/{*.so,allegro/*/*.so}

%clean
rm -rf $RPM_BUILD_ROOT

#%%post	-p /sbin/ldconfig
#%%postun	-p /sbin/ldconfig

#%%post devel	-p	/sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%%postun devel	-p	/sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc docs/html/refman readme_a5.txt
#%%attr(755,root,root) %{_libdir}/liballeg-%{version}.so
#%%dir %{_libdir}/allegro
#%%dir %{_libdir}/allegro/%{version}
#%%{_libdir}/allegro/%{version}/modules.lst

%files devel
%defattr(644,root,root,755)
#%%attr(755,root,root) %{_bindir}/allegro5-config
#%%{_libdir}/liballeg_unsharable.a
%{_includedir}/*
#%%{_aclocaldir}/allegro.m4
#%%{_mandir}/man3/*
#%%{_infodir}/*.info*

#%%if %{with static}
#%%files static
#%%defattr(644,root,root,755)
#%%{_libdir}/liballeg.a
#%%endif

#%%if %{with dbglib}
#%%files debug
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/liballd-%{version}.so
#%%{_libdir}/liballd_unsharable.a

#%%if %{with static}
#%%files debug-static
#%%defattr(644,root,root,755)
#%%{_libdir}/liballd.a
#%%endif
#%%endif

#%%if %{with proflib}
#%%files profile
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/liballp-%{version}.so
#%%{_libdir}/liballp_unsharable.a

#%%if %{with static}
#%%files profile-static
#%%defattr(644,root,root,755)
#%%{_libdir}/liballp.a
#%%endif
#%%endif

#%%if %{with svga}
#%%files svgalib
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-svgalib.so
#%%endif

#%%if %{with dga2}
#%%files dga2
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-dga2.so
#%%endif

#%%if %{with esd}
#%%files esd
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-esddigi.so
#%%endif

#%%if %{with arts}
#%%files arts
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-artsdigi.so
#%%endif

#%%if %{with fbcon}
#%%files fbcon
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-fbcon.so
#%%endif

#%%ifarch %{ix86}
#%%if %{with vga}
#%%files vga
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-vga.so
#%%endif
#%%endif

#%%if %{with alsa}
#%%files alsa
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-alsadigi.so
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-alsamidi.so
#%%endif

#%%if %{with jack}
#%%files jack
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_libdir}/allegro/%{version}/alleg-jackdigi.so
#%%endif

#%%files tools
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_bindir}/colormap
#%%attr(755,root,root) %{_bindir}/exedat
#%%attr(755,root,root) %{_bindir}/pack
#%%attr(755,root,root) %{_bindir}/rgbmap
#%%attr(755,root,root) %{_bindir}/textconv
#%attr(755,root,root) %{_bindir}/xkeymap
#%%attr(755,root,root) %{_bindir}/xf2pcx
#%%attr(755,root,root) %{_bindir}/dat
#%%attr(755,root,root) %{_bindir}/dat2c
#%%attr(755,root,root) %{_bindir}/dat2s
#%%attr(755,root,root) %{_bindir}/grabber
#%%attr(755,root,root) %{_bindir}/pat2dat
#%attr(755,root,root) %{_bindir}/setup-allegro

#%%files tests
#%%defattr(644,root,root,755)
#%%attr(755,root,root) %{_bindir}/afinfo
#%%attr(755,root,root) %{_bindir}/akaitest
#%%attr(755,root,root) %{_bindir}/cpptest
#%%attr(755,root,root) %{_bindir}/demo-allegro
#%%attr(755,root,root) %{_bindir}/digitest
#%%attr(755,root,root) %{_bindir}/filetest
#%%attr(755,root,root) %{_bindir}/gfxinfo
#%%attr(755,root,root) %{_bindir}/mathtest
#%%attr(755,root,root) %{_bindir}/miditest
#%%attr(755,root,root) %{_bindir}/play-allegro
#%%attr(755,root,root) %{_bindir}/playfli
#%%attr(755,root,root) %{_bindir}/test-allegro
#%%attr(755,root,root) %{_bindir}/vesainfo

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex_acodec
%attr(755,root,root) %{_bindir}/ex_acodec_multi
%attr(755,root,root) %{_bindir}/ex_audio_props
%attr(755,root,root) %{_bindir}/ex_audio_simple
%attr(755,root,root) %{_bindir}/ex_bitmap
%attr(755,root,root) %{_bindir}/ex_bitmap_flip
%attr(755,root,root) %{_bindir}/ex_bitmap_target
%attr(755,root,root) %{_bindir}/ex_blend
%attr(755,root,root) %{_bindir}/ex_blend2
%attr(755,root,root) %{_bindir}/ex_blend_bench
%attr(755,root,root) %{_bindir}/ex_blend_test
%attr(755,root,root) %{_bindir}/ex_blit
%attr(755,root,root) %{_bindir}/ex_clip
%attr(755,root,root) %{_bindir}/ex_color
%attr(755,root,root) %{_bindir}/ex_config
%attr(755,root,root) %{_bindir}/ex_convert
%attr(755,root,root) %{_bindir}/ex_dir
%attr(755,root,root) %{_bindir}/ex_disable_screensaver
%attr(755,root,root) %{_bindir}/ex_display_options
%attr(755,root,root) %{_bindir}/ex_draw
%attr(755,root,root) %{_bindir}/ex_draw_bitmap
%attr(755,root,root) %{_bindir}/ex_drawpixels
%attr(755,root,root) %{_bindir}/ex_dualies
%attr(755,root,root) %{_bindir}/ex_expose
%attr(755,root,root) %{_bindir}/ex_font
%attr(755,root,root) %{_bindir}/ex_font_justify
%attr(755,root,root) %{_bindir}/ex_fs_resize
%attr(755,root,root) %{_bindir}/ex_fs_window
%attr(755,root,root) %{_bindir}/ex_get_path
%attr(755,root,root) %{_bindir}/ex_gldepth
%attr(755,root,root) %{_bindir}/ex_glext
%attr(755,root,root) %{_bindir}/ex_icon
%attr(755,root,root) %{_bindir}/ex_joystick_events
%attr(755,root,root) %{_bindir}/ex_kcm_direct
%attr(755,root,root) %{_bindir}/ex_keyboard_events
%attr(755,root,root) %{_bindir}/ex_keyboard_focus
%attr(755,root,root) %{_bindir}/ex_lines
%attr(755,root,root) %{_bindir}/ex_lockbitmap
%attr(755,root,root) %{_bindir}/ex_lockscreen
%attr(755,root,root) %{_bindir}/ex_logo
%attr(755,root,root) %{_bindir}/ex_membmp
%attr(755,root,root) %{_bindir}/ex_memfile
%attr(755,root,root) %{_bindir}/ex_mixer_chain
%attr(755,root,root) %{_bindir}/ex_mixer_pp
%attr(755,root,root) %{_bindir}/ex_monitorinfo
%attr(755,root,root) %{_bindir}/ex_mouse
%attr(755,root,root) %{_bindir}/ex_mouse_cursor
%attr(755,root,root) %{_bindir}/ex_mouse_events
%attr(755,root,root) %{_bindir}/ex_mouse_focus
%attr(755,root,root) %{_bindir}/ex_multisample
%attr(755,root,root) %{_bindir}/ex_multiwin
%attr(755,root,root) %{_bindir}/ex_native_filechooser
%attr(755,root,root) %{_bindir}/ex_noframe
%attr(755,root,root) %{_bindir}/ex_opengl
%attr(755,root,root) %{_bindir}/ex_opengl_pixel_shader
%attr(755,root,root) %{_bindir}/ex_path
%attr(755,root,root) %{_bindir}/ex_path_test
%attr(755,root,root) %{_bindir}/ex_pixelformat
%attr(755,root,root) %{_bindir}/ex_prim
%attr(755,root,root) %{_bindir}/ex_resize
%attr(755,root,root) %{_bindir}/ex_resize2
%attr(755,root,root) %{_bindir}/ex_rotate
%attr(755,root,root) %{_bindir}/ex_saw
%attr(755,root,root) %{_bindir}/ex_scale
%attr(755,root,root) %{_bindir}/ex_stream_file
%attr(755,root,root) %{_bindir}/ex_stream_seek
%attr(755,root,root) %{_bindir}/ex_subbitmap
%attr(755,root,root) %{_bindir}/ex_synth
%attr(755,root,root) %{_bindir}/ex_threads
%attr(755,root,root) %{_bindir}/ex_threads2
%attr(755,root,root) %{_bindir}/ex_timedwait
%attr(755,root,root) %{_bindir}/ex_timer
%attr(755,root,root) %{_bindir}/ex_transform
%attr(755,root,root) %{_bindir}/ex_ttf
%attr(755,root,root) %{_bindir}/ex_user_events
%attr(755,root,root) %{_bindir}/ex_utf8
%attr(755,root,root) %{_bindir}/ex_vsync
%attr(755,root,root) %{_bindir}/ex_warp_mouse
%attr(755,root,root) %{_bindir}/ex_windows
%attr(755,root,root) %{_bindir}/ex_winfull
