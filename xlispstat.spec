Summary:	An implementation of the Lisp language with statistics extensions
Name:		xlispstat
Version:	3.52.9
Release:	2
Copyright:	Distributable
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In¿ynierskie
Source0:	ftp://umnstat.stat.umn.edu:/pub/xlispstat/3-52/%{name}-%{version}.tar.gz
URL:		http://lib.stat.cmu.edu/xlispstat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlispstat package contains XLISP-PLUS, an implementation of the
Lisp programming language for the X Window System. XLISP-PLUS also
includes extensions for performing advanced statistical computations.

Install the xlispstat package if you need a version of the Lisp
programming language for X with statistics extensions.

%prep
%setup -q -n xlispstat-3-52-9

%build
%configure
%{__make} UCFLAGS="%{rpmcflags} -mieee-fp"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf README RELEASE doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz RELEASE.gz doc/*
%dir %{_libdir}/xlispstat
%attr(755,root,root) %{_bindir}/xlispstat
%attr(755,root,root) %{_libdir}/xlispstat/xlisp
%{_libdir}/xlispstat/Autoload
%{_libdir}/xlispstat/Data
%{_libdir}/xlispstat/Examples
%{_libdir}/xlispstat/xlisp.hlp
%{_libdir}/xlispstat/xlisp.wks
