Summary:	Various RPM command-line tools
Name:		rpmtools
Version:	6.1
Release:	%mkrel 1
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/rpm/rpmtools/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl-MDV-Packdrakeng
BuildRequires:	perl-MDV-Distribconf
Requires:	perl-MDV-Distribconf > 3.00
Requires:	xz
Requires:	genhdlist2
Requires:	perl(File::Find)
Requires:	perl(File::Path)
Requires:	perl(File::Temp)
Requires:	perl(Getopt::Long)
Requires:	perl(MDV::Distribconf::Build)
Requires:	perl(Pod::Usage)
Requires:	perl(URPM)
Requires:	perl(URPM::Build)
Conflicts:	rpmtools-compat <= 2.0
Conflicts:	rpmtools-devel <= 2.0
Conflicts:	packdrake < 5.0.26

%description
Various tools needed by urpmi and drakxtools for handling rpm files.

%package -n	packdrake
Group:		%{group}
Summary:	A simple Archive Extractor/Builder
Conflicts:	rpmtools <= 5.0.25
Provides:	perl(packdrake)

%description -n	packdrake
Packdrake is a simple indexed archive builder and extractor using
standard compression methods.

%package -n	genhdlist2
Group:		%{group}
Summary:	Tool to generate urpmi metadata (media_info/*)
Conflicts:	rpmtools <= 5.4

%description -n	genhdlist2
genhdlist2 generates hdlist.cz, synthesis.hdlist.cz and *.xml.lzma files used
by urpmi

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dumpdistribconf
%{_bindir}/gendistrib
%{_bindir}/genhdlist-old
%{_mandir}/man1/dumpdistribconf*
%{_mandir}/man1/gendistrib*
%{_mandir}/man1/genhdlist-old.*

%files -n packdrake
%defattr(-,root,root)
%{_bindir}/packdrake
%{perl_vendorlib}/packdrake.pm
%{_mandir}/man1/packdrake*

%files -n genhdlist2
%defattr(-,root,root)
%{_bindir}/genhdlist2
%{_mandir}/man1/genhdlist2*
