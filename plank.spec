%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A port of docky to Vala
Name:		plank
Version:	0.11.89
Release:	1
License:	GPLv3+
Group:		Graphical desktop/GNOME
Url:		http://wiki.go-docky.com/index.php?title=Plank:Introduction
Source0:	https://launchpad.net/%{name}/1.0/%{version}/+download/%{name}-%{version}.tar.xz
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	vala
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libbamf3)
BuildRequires:	pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:	libxml2-utils
Requires:	bamf-daemon

%description
A very simple dock written in Vala.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
#{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	vala-tools
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/vala/vapi/%{name}.vapi
%{_datadir}/vala/vapi/%{name}.deps

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make LIBS="-lm"

%install
%make_install
# Don't use apport
rm -f %{buildroot}%{_sysconfdir}/apport/crashdb.conf.d/%{name}-crashdb.conf
rm -f %{buildroot}%{_datadir}/apport/package-hooks/source_%{name}.py

%find_lang %{name}

