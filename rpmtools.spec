%define name rpmtools
%define version 5.6
%define release %mkrel 1

%define group %(perl -e 'print "%_vendor" =~ /\\bmandr/i ? "System/Configuration/Packaging" : "System Environment/Base"')
%define rpm_version %(rpm -q --queryformat '%|EPOCH?{[%{EPOCH}:%{VERSION}]}:{%{VERSION}}|' rpm)

Summary:	Various RPM command-line tools
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPL
Group:		%{group}
URL:		http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/rpmtools
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	perl%{?mdkversion:-devel}
BuildRequires:	rpm-devel >= 4.2.3
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-MDV-Packdrakeng
BuildRequires:	perl-MDV-Distribconf
Requires:	perl-MDV-Distribconf > 3.00
# we can now expect librpm API to be backward compatible
Requires:	rpm >= %{rpm_version}
Requires:	bzip2 >= 1.0
Requires:	genhdlist2
Conflicts:	rpmtools-compat <= 2.0
Conflicts:	rpmtools-devel <= 2.0
Conflicts:	packdrake < 5.0.26

%description
Various tools needed by urpmi and drakxtools for handling rpm files.

%package -n packdrake
Group:		%{group}
Summary:	A simple Archive Extractor/Builder
Conflicts:	rpmtools <= 5.0.25
Provides:	perl(packdrake)

%description -n packdrake
Packdrake is a simple indexed archive builder and extractor using
standard compression methods.

%package -n genhdlist2
Group:		%{group}
Summary:	Tool to generate urpmi metadata (media_info/*)
Conflicts:	rpmtools <= 5.4

%description -n genhdlist2
genhdlist2 generates hdlist.cz, synthesis.hdlist.cz and *.xml.lzma files used
by urpmi

%prep
%setup -q

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%optflags"

%check
%make test

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dumpdistribconf
%{_bindir}/gendistrib
%{_bindir}/genhdlist
%{_bindir}/parsehdlist
%{_bindir}/rpm2cpio.pl
%{_bindir}/rpm2header
%{_mandir}/man1/dumpdistribconf*
%{_mandir}/man1/gendistrib*
%{_mandir}/man1/genhdlist.*

%files -n packdrake
%defattr(-,root,root)
%{_bindir}/packdrake
%{perl_vendorlib}/packdrake.pm
%{_mandir}/man1/packdrake*

%files -n genhdlist2
%defattr(-,root,root)
%{_bindir}/genhdlist2
%{_mandir}/man1/genhdlist2*

