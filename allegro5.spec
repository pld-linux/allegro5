#
# TODO:
# - texinfo docs (BR: pandoc)
# - check if it's usable now
#
# Conditional build:
%bcond_without	alsa		# ALSA support in allegro_audio library
%bcond_with	curl		# cURL example
%bcond_without	dumb		# MOD support in allegro_acodec library
%bcond_without	gtk		# (GTK+ 2.x based) native dialog library
%bcond_without	openal		# OpenAL support in allegro_audio library
%bcond_without	physfs		# PhysFS addon library
%bcond_without	pulseaudio	# PulseAudio support in allegro_audio library
%bcond_without	python		# Python wrapper
%bcond_with	sse		# SSE instructions usage
#
%ifarch pentium3 pentium4 %{x8664}
%define	with_sse	1
%endif
Summary:	A game programming library
Summary(de.UTF-8):	Eine Bibliothek zur Programmierung von Spielen
Summary(es.UTF-8):	Una biblioteca de programación de juegos
Summary(fr.UTF-8):	Une librairie de programmation de jeux
Summary(it.UTF-8):	Una libreria per la programmazione di videogiochi
Summary(pl.UTF-8):	Biblioteka do programowania gier
Name:		allegro5
Version:	5.0.9
Release:	0.1
License:	Giftware
Group:		Libraries
Source0:	http://downloads.sourceforge.net/alleg/allegro-%{version}.tar.gz
# Source0-md5:	59fb41dccc300be0044cfad5fff0ca81
URL:		http://alleg.sourceforge.net/
%{?with_openal:BuildRequires:	OpenAL-devel}
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	cmake >= 2.6
%{?with_curl:BuildRequires:	curl-devel}
BuildRequires:	dumb-devel
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
%{?with_gtk:BuildRequires:	glib2-devel >= 2.0}
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
%{?with_physfs:BuildRequires:	physfs-devel}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9.15}
BuildRequires:	rpmbuild(macros) >= 1.605
#BuildRequires:	texinfo
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
%if %{with python}
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%endif
Obsoletes:	allegro
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
Obsoletes:	allegro-devel

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

%package acodec
Summary:	Allegro acodec addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro acodec
Group:		Libraries
Requires:	%{name}-audio = %{version}-%{release}

%description acodec
Allegro acodec addon library.

%description acodec -l pl.UTF-8
Biblioteka dodatkowa Allegro acodec.

%package acodec-devel
Summary:	Header files for Allegro acodec addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro acodec
Group:		Libraries
Requires:	%{name}-acodec = %{version}-%{release}
Requires:	%{name}-audio-devel = %{version}-%{release}

%description acodec-devel
Header files for Allegro acodec addon library.

%description acodec-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro acodec.

%package audio
Summary:	Allegro audio addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro audio
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description audio
Allegro audio addon library.

%description audio -l pl.UTF-8
Biblioteka dodatkowa Allegro audio.

%package audio-devel
Summary:	Header files for Allegro audio addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro audio
Group:		Libraries
Requires:	%{name}-audio = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description audio-devel
Header files for Allegro audio addon library.

%description audio-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro audio.

%package dialog
Summary:	Allegro dialog addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro dialog
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description dialog
Allegro dialog addon library.

%description dialog -l pl.UTF-8
Biblioteka dodatkowa Allegro dialog.

%package dialog-devel
Summary:	Header files for Allegro dialog addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro dialog
Group:		Libraries
Requires:	%{name}-dialog = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description dialog-devel
Header files for Allegro dialog addon library.

%description dialog-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro dialog.

%package image
Summary:	Allegro image addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro image
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description image
Allegro image addon library.

%description image -l pl.UTF-8
Biblioteka dodatkowa Allegro image.

%package image-devel
Summary:	Header files for Allegro image addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro image
Group:		Libraries
Requires:	%{name}-image = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description image-devel
Header files for Allegro image addon library.

%description image-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro image.

%package physfs
Summary:	Allegro physfs addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro physfs
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description physfs
Allegro physfs addon library.

%description physfs -l pl.UTF-8
Biblioteka dodatkowa Allegro physfs.

%package physfs-devel
Summary:	Header files for Allegro physfs addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro physfs
Group:		Libraries
Requires:	%{name}-physfs = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description physfs-devel
Header files for Allegro physfs addon library.

%description physfs-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro physfs.

%package ttf
Summary:	Allegro ttf addon library
Summary(pl.UTF-8):	Biblioteka dodatkowa Allegro ttf
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description ttf
Allegro ttf addon library.

%description ttf -l pl.UTF-8
Biblioteka dodatkowa Allegro ttf.

%package ttf-devel
Summary:	Header files for Allegro ttf addon library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dodatkowej Allegro ttf
Group:		Libraries
Requires:	%{name}-ttf = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description ttf-devel
Header files for Allegro ttf addon library.

%description ttf-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dodatkowej Allegro ttf.

%package tools
Summary:	A game programming library - tools
Summary(de.UTF-8):	Zusätzliche Hilfprogramme für die Allegro Bibliothek
Summary(es.UTF-8):	Herramientas adicionales para la librería de programación Allegro
Summary(fr.UTF-8):	Outils supplémentaires pour la librairie de programmation Allegro
Summary(it.UTF-8):	Programmi di utilità aggiuntivi per la libreria Allegro
Summary(pl.UTF-8):	Biblioteka do programowania gier - narzędzia
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-tools

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

%package examples
Summary:	A game programming library - examples
Summary(pl.UTF-8):	Biblioteka do programowania gier - programy przykładowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	allegro-examples

%description examples
This package contains example programs which demonstrate allegro
features.

%description examples -l pl.UTF-8
Pakiet zawiera programy przykładowe demonstrujące możliwości
biblioteki allegro.

%package -n python-%{name}
Summary:	Python wrapper for Allegro library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki Allegro
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-modules

%description -n python-%{name}
Python wrapper for Allegro library.

%description -n python-%{name} -l pl.UTF-8
Pythonowy interfejs do biblioteki Allegro.

%prep
%setup -q -n allegro-%{version}

%build
install -d build
cd build
%cmake .. \
	-DMANDIR=%{_mandir} \
	-DINFODIR=%{_infodir} \
	%{!?with_sse:-DWANT_ALLOW_SSE=OFF} \
	%{!?with_alsa:-DWANT_ALSA=OFF} \
	%{?with_curl:-DWANT_CURL_EXAMPLE=ON} \
	%{!?with_dumb:-DWANT_MODAUDIO=OFF} \
	%{!?with_gtk:-DWANT_NATIVE_DIALOG=OFF} \
	%{!?with_openal:-DWANT_OPENAL=OFF} \
	%{!?with_physfs:-DWANT_PHYSFS=OFF} \
	%{!?with_pulseaudio:-DWANT_PULSEAUDIO=OFF} \
	%{?with_python:-DWANT_PYTHON_WRAPPER=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install -C build \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
install build/python/allegro.py $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

install -d $RPM_BUILD_ROOT%{_mandir}/man3
cp -p docs/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3

# install examples
find build/examples -maxdepth 1 -perm 755 -name "ex*" -exec install {} $RPM_BUILD_ROOT%{_bindir} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	acodec -p /sbin/ldconfig
%postun	acodec -p /sbin/ldconfig

%post	audio -p /sbin/ldconfig
%postun	audio -p /sbin/ldconfig

%post	dialog -p /sbin/ldconfig
%postun	dialog -p /sbin/ldconfig

%post	image -p /sbin/ldconfig
%postun	image -p /sbin/ldconfig

%post	physfs -p /sbin/ldconfig
%postun	physfs -p /sbin/ldconfig

%post	ttf -p /sbin/ldconfig
%postun	ttf -p /sbin/ldconfig

#%%post devel	-p	/sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

#%%postun devel	-p	/sbin/postshell
#-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc CHANGES-5.0.txt README.txt docs/html/refman
%attr(755,root,root) %{_libdir}/liballegro.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_color.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_color.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_font.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_font.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_main.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_main.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_memfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_memfile.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_primitives.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_primitives.so.5.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro.so
%attr(755,root,root) %{_libdir}/liballegro_color.so
%attr(755,root,root) %{_libdir}/liballegro_font.so
%attr(755,root,root) %{_libdir}/liballegro_main.so
%attr(755,root,root) %{_libdir}/liballegro_memfile.so
%attr(755,root,root) %{_libdir}/liballegro_primitives.so
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_image.h
%{?with_gtk:%exclude %{_includedir}/allegro5/allegro_native_dialog.h}
%{?with_physfs:%exclude %{_includedir}/allegro5/allegro_physfs.h}
%exclude %{_includedir}/allegro5/allegro_ttf.h
%{_pkgconfigdir}/allegro-5.0.pc
%{_pkgconfigdir}/allegro-5.pc
%{_pkgconfigdir}/allegro_color-5.0.pc
%{_pkgconfigdir}/allegro_color-5.pc
%{_pkgconfigdir}/allegro_font-5.0.pc
%{_pkgconfigdir}/allegro_font-5.pc
%{_pkgconfigdir}/allegro_main-5.0.pc
%{_pkgconfigdir}/allegro_main-5.pc
%{_pkgconfigdir}/allegro_memfile-5.0.pc
%{_pkgconfigdir}/allegro_memfile-5.pc
%{_pkgconfigdir}/allegro_primitives-5.0.pc
%{_pkgconfigdir}/allegro_primitives-5.pc
%{_mandir}/man3/ALLEGRO_*.3*
%{_mandir}/man3/al_*.3*

%files acodec
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_acodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_acodec.so.5.0

%files acodec-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_acodec.so
%{_includedir}/allegro5/allegro_acodec.h
%{_pkgconfigdir}/allegro_acodec-5.0.pc
%{_pkgconfigdir}/allegro_acodec-5.pc

%files audio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_audio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_audio.so.5.0

%files audio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_audio.so
%{_includedir}/allegro5/allegro_audio.h
%{_pkgconfigdir}/allegro_audio-5.0.pc
%{_pkgconfigdir}/allegro_audio-5.pc

%if %{with gtk}
%files dialog
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_dialog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_dialog.so.5.0

%files dialog-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_dialog.so
%{_includedir}/allegro5/allegro_native_dialog.h
%{_pkgconfigdir}/allegro_dialog-5.0.pc
%{_pkgconfigdir}/allegro_dialog-5.pc
%endif

%files image
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_image.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_image.so.5.0

%files image-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_image.so
%{_includedir}/allegro5/allegro_image.h
%{_pkgconfigdir}/allegro_image-5.0.pc
%{_pkgconfigdir}/allegro_image-5.pc

%if %{with physfs}
%files physfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_physfs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liballegro_physfs.so.5.0

%files physfs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_physfs.so
%{_includedir}/allegro5/allegro_physfs.h
%{_pkgconfigdir}/allegro_physfs-5.0.pc
%{_pkgconfigdir}/allegro_physfs-5.pc
%endif

%files ttf
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/liballegro_ttf.so.5.0
%attr(755,root,root) %{_libdir}/liballegro_ttf.so.*.*.*

%files ttf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liballegro_ttf.so
%{_includedir}/allegro5/allegro_ttf.h
%{_pkgconfigdir}/allegro_ttf-5.0.pc
%{_pkgconfigdir}/allegro_ttf-5.pc

#%files tools
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/xkeymap
#%attr(755,root,root) %{_bindir}/xf2pcx
#%attr(755,root,root) %{_bindir}/xfixicon.sh

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ex_acodec
%attr(755,root,root) %{_bindir}/ex_acodec_multi
%attr(755,root,root) %{_bindir}/ex_audio_chain
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
%{?with_curl:%attr(755,root,root) %{_bindir}/ex_curl}
%attr(755,root,root) %{_bindir}/ex_dir
%attr(755,root,root) %{_bindir}/ex_disable_screensaver
%attr(755,root,root) %{_bindir}/ex_display_events
%attr(755,root,root) %{_bindir}/ex_display_options
%attr(755,root,root) %{_bindir}/ex_draw
%attr(755,root,root) %{_bindir}/ex_draw_bitmap
%attr(755,root,root) %{_bindir}/ex_drawpixels
%attr(755,root,root) %{_bindir}/ex_dualies
%attr(755,root,root) %{_bindir}/ex_expose
%attr(755,root,root) %{_bindir}/ex_file_slice
%attr(755,root,root) %{_bindir}/ex_filter
%attr(755,root,root) %{_bindir}/ex_font
%attr(755,root,root) %{_bindir}/ex_fs_resize
%attr(755,root,root) %{_bindir}/ex_fs_window
%attr(755,root,root) %{_bindir}/ex_get_path
%attr(755,root,root) %{_bindir}/ex_gldepth
%attr(755,root,root) %{_bindir}/ex_glext
%attr(755,root,root) %{_bindir}/ex_haiku
%attr(755,root,root) %{_bindir}/ex_icon
%attr(755,root,root) %{_bindir}/ex_icon2
%attr(755,root,root) %{_bindir}/ex_joystick_events
%attr(755,root,root) %{_bindir}/ex_joystick_hotplugging
%attr(755,root,root) %{_bindir}/ex_font_justify
%attr(755,root,root) %{_bindir}/ex_kcm_direct
%attr(755,root,root) %{_bindir}/ex_keyboard_events
%attr(755,root,root) %{_bindir}/ex_keyboard_focus
%attr(755,root,root) %{_bindir}/ex_lines
%attr(755,root,root) %{_bindir}/ex_lockbitmap
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
%attr(755,root,root) %{_bindir}/ex_nodisplay
%attr(755,root,root) %{_bindir}/ex_noframe
%attr(755,root,root) %{_bindir}/ex_opengl
%attr(755,root,root) %{_bindir}/ex_opengl_pixel_shader
%attr(755,root,root) %{_bindir}/ex_path
%attr(755,root,root) %{_bindir}/ex_path_test
%{?with_physfs:%attr(755,root,root) %{_bindir}/ex_physfs}
%attr(755,root,root) %{_bindir}/ex_pixelformat
%attr(755,root,root) %{_bindir}/ex_premulalpha
%attr(755,root,root) %{_bindir}/ex_prim
%attr(755,root,root) %{_bindir}/ex_resample_test
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

%if %{with python}
%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/allegro.py[co]
%endif
