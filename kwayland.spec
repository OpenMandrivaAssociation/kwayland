%define major 5
%define libname %mklibname KF5WaylandClient %{major}
%define devname %mklibname KF5WaylandClient -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# Workaround for bug in clang 7.0-336482
# Compile-time error:
# Called function is not the same type as the call!
#  tail call void @wl_event_queue_destroy(%struct.org_kde_kwin_appmenu_manager* nonnull %4) #18, !dbg !61555
#  LLVM ERROR: Broken function found, compilation aborted!
%define _disable_lto 1

Summary: KDE Library for working with the Wayland display server
Name: kwayland
Version: 5.51.0
Release: 1
License: GPL
Group: System/Libraries
Url: http://kde.org/
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-client) >= 1.8.1
BuildRequires: pkgconfig(wayland-scanner) >= 1.8.1
BuildRequires: pkgconfig(wayland-server) >= 1.8.1
BuildRequires: wayland-tools >= 1.8.1
BuildRequires: cmake(ECM)
Requires: qt5-qtwayland
Requires: %{_lib}qt5-output-driver-eglfs
Requires: %{libname} = %{EVRD}

%description
KDE Library for working with the Wayland display server.

%package -n %{libname}
Summary: KDE Library for working with the Wayland display server
Group: System/Libraries

%description -n %{libname}
KDE Library for working with the Wayland display server.

%package -n %{devname}
Summary: Development files for the KDE Frameworks Wayland library
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks Wayland library.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/org_kde_kwayland.categories
%{_libdir}/libexec/org-kde-kf5-kwayland-testserver

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5*
%{_libdir}/qt5/mkspecs/modules/*.pri
