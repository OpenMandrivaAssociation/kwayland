%define libname %mklibname KF6Wayland
%define devname %mklibname KF6Wayland -d
%define git 20230622

Name: kf6-kwayland
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kwayland/-/archive/master/kwayland-master.tar.bz2#/kwayland-%{git}.tar.bz2
Summary: Qt-style Client and Server library wrapper for the Wayland libraries
URL: https://invent.kde.org/frameworks/kwayland
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: wayland-tools
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(VulkanHeaders)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6WaylandScannerTools)
BUildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(WaylandProtocols)
BuildRequires: cmake(EGL)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
Requires: %{libname} = %{EVRD}

%description
Qt-style Client and Server library wrapper for the Wayland libraries

%package -n %{libname}
Summary: Qt-style Client and Server library wrapper for the Wayland libraries
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt-style Client and Server library wrapper for the Wayland libraries

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt-style Client and Server library wrapper for the Wayland libraries

%prep
%autosetup -p1 -n kwayland-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/KWayland
%{_libdir}/cmake/KF6Wayland
%{_libdir}/pkgconfig/KF6WaylandClient.pc
%{_libdir}/qt6/mkspecs/modules/qt_KWaylandClient.pri
%{_libdir}/qt6/doc/KF6Wayland.*

%files -n %{libname}
%{_libdir}/libKF6WaylandClient.so*
