%define	libname %mklibname %{name} %{version}
%define	oname GrandOrgue

Summary:	Virtual Pipe Organ Software
Name:	grandorgue
Version:	3.15.4
Release:	1
License:	GPLv2+
Group:	Sound
Url:		https://github.com/GrandOrgue/grandorgue
Source0:	https://github.com/GrandOrgue/grandorgue/archive/%{version}-1.tar.gz?/%{name}-%{version}-1.tar.gz
Patch0:		grandorgue-3.15.4-fix-rtmidi-header-path.patch
Patch1:		grandorgue-3.15.4-fix-missing-header.patch
BuildRequires:	cmake
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-style-xsl-ns
BuildRequires:	gettext
BuildRequires:	imagemagick
BuildRequires:	po4a
BuildRequires:	xsltproc
BuildRequires:	libzita-convolver-devel
BuildRequires:wxgtku3.2-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3f)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(rtaudio)
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(yaml-cpp)
BuildRequires:	pkgconfig(zlib)
Recommends:		%{name}-demo = %{EVRD}

%description
GrandOrgue is a virtual pipe organ sample player application supporting a HW1
compatible file format.

%files -f %{oname}.lang
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{oname}*
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/metainfo/%{oname}.appdata.xml
%{_iconsdir}/hicolor/*/apps/%{oname}.png
%{_mandir}/man1/%{oname}*.1*

#----------------------------------------------------------------------------

%package demo
Summary:	Sample files for %{name}
Group:	Sound
BuildArch:	noarch

%description demo
Sample files for %{name}.

%files demo
%{_datadir}/%{oname}/packages/*.orgue

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
Library for %{name} application.

%files -n %{libname}
%{_libdir}/lib%{oname}*.so.%{version}*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}-1


%build
# Yaml-cpp detection is rather broken...
%cmake	\
	-DDOC_INSTALL_DIR="%{_docdir}"	\
	-DLIBINSTDIR=%{_lib} \
	-DYAML_CPP_LIBRARIES="%{_libdir}" \
	-Dyaml-cpp_DIR="%{_libdir}/cmake/yaml-cpp" \
	-DYAML_CPP_INCLUDE_DIRS="%{_includedir}/yaml-cpp" \
	-DUSE_INTERNAL_PORTAUDIO=OFF	\
	-DUSE_INTERNAL_RTAUDIO=OFF	\
	-DUSE_INTERNAL_ZITACONVOLVER=OFF
%make




%install
%makeinstall_std -C build

%find_lang %{oname}
