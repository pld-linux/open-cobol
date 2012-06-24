Summary:	COBOL compiler
Summary(pl):	Kompilator j�zyka COBOL
Name:		open-cobol
Version:	0.32
Release:	1
License:	GPL/LGPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/open-cobol/%{name}-%{version}.tar.gz
# Source0-md5:	9ffc3b75eca988e40206b3e310bba635
URL:		http://www.opencobol.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gmp-devel
Requires:	libltdl-devel
Requires:	ncurses-devel
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
OpenCOBOL jest kompilerem COBOLa o otwartych �r�d�ach. OpenCOBOL
implementuje znaczn� cz�� standard�w COBOL 85 i COBOL 2002, jak i
wiele z rozszerze� z istniej�cych kompilator�w COBOLa. OpenCOBOL
t�umaczy �r�d�a COBOLa do j�zyka C i nast�pnie kompiluje
przet�umaczony kod u�ywaj�c GCC. Pozwala budowa� programy COBOLowe na
wielu platformach, w tym takich jak GNU/Linux, Mac OS X i Microsoft
Windows. Kompilator jest obj�ty licencj� GNU General Public License.
Biblioteka uruchomieniowa jest obj�ta licencj� GNU Lesser General
Public License.

%package libs
Summary:	OpenCOBOL runtime library
Summary(pl):	Biblioteka uruchomieniowa OpenCOBOLa
License:	LGPL
Group:		Libraries

%description libs
OpenCOBOL runtime library.

%description libs -l pl
Biblioteka uruchomieniowa OpenCOBOLa.

%package static
Summary:	Static OpenCOBOL runtime library
Summary(pl):	Statyczna biblioteka uruchomieniowa OpenCOBOLa
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static OpenCOBOL runtime library, needed to build statically
linked COBOL programs.

%description static -l pl
Statyczna biblioteka uruchomieniowa OpenCOBOLa, potrzebna do tworzenia
statycznie linkowanych program�w w COBOLu.

%prep
%setup -q

%build
%{__libtoolize}
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_includedir}/libcob.h
%{_includedir}/libcob
%attr(755,root,root) %{_libdir}/libcob.so
%{_libdir}/libcob.la
%{_infodir}/*.info*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcob.so.*.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcob.a
