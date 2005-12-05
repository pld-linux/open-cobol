#
# Conditional build:
Summary:	COBOL compiler
Summary(pl):	Kompilator jêzyka COBOL
Name:		open-cobol
Version:	0.32
Release:	0.2
License:	GPL/LGPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9ffc3b75eca988e40206b3e310bba635
URL:		http://www.opencobol.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCOBOL is an open-source COBOL compiler. OpenCOBOL implements
substantial part of the COBOL 85 and COBOL 2002 standards, as well as
many extensions of the existent COBOL compilers. OpenCOBOL translates
COBOL into C and compiles the translated code using GCC. You can build
your COBOL programs on various platforms, including GNU/Linux, Mac OS
X, and Microsoft Windows. The compiler is licensed under GNU General
Public License. The run-time library is licensed under GNU Lesser
General Public License.

%description -l pl
OpenCOBOL jest kompilerem COBOLa o otwartych ¼ród³ach. OpenCOBOL
implementuje znaczn± czê¶æ standardów COBOL 85 i COBOL 2002, jak i
wiele z rozszerzeñ z istniej±cych kompilatorów COBOLa. OpenCOBOL
t³umaczy ¼ród³a COBOLa do jêzyka C i nastêpnie kompiluje
przet³umaczony kod u¿ywaj±c GCC. Mo¿esz budowaæ twoje programy
COBOLowe na wielu platwormach, tj. GNU/Linux, Mac OS X i Microsoft
Windows. Kompiler jest objêty licencj± GNU General Public License.
Biblioteka "run-time" jest objêta licencj± GNU Lesser General Public
License.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
        CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/config/*.conf
%{_includedir}/libcob.h
%{_includedir}/libcob/*
%attr(755,root,root) %{_libdir}/libcob.*.*.*
%{_libdir}/libcob.la
