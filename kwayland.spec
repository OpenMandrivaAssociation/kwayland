%define major 5
%define libname %mklibname KF5WaylandClient %{major}
%define devname %mklibname KF5WaylandClient -d
%define debug_package %{nil}
%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: 		kwayland
Version: 	5.6.1
Release: 	1
Source0: 	http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: 	KDE Library for working with the Wayland display server
Url: 		http://kde.org/
License: 	GPL
Group: 		System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(wayland-client) >= 1.8.1
BuildRequires: pkgconfig(wayland-scanner) >= 1.8.1
BuildRequires: pkgconfig(wayland-server) >= 1.8.1
BuildRequires: wayland-tools >= 1.8.1
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
Requires: qt5-qtwayland
Requires: qt5-output-driver-eglfs
Requires: kwayland-integration
Requires: %{libname} = %{EVRD}

%description
KDE Library for working with the Wayland display server.

%package -n %{libname}
Summary: KDE Library for working with the Wayland display server
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE Library for working with the Wayland display server.

%package -n %{devname}
Summary: Development files for the KDE Plasma 5 Wayland library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Plasma 5 Wayland library.

%prep
%setup -qn %{name}-%{plasmaver}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/org_kde_kwayland.categories

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{plasmaver}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
