Summary:	Various RPM command-line tools
Name:		rpmtools
Version:	6.1
Release:	13
Source0:	%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		System/Configuration/Packaging
URL:		https://abf.rosalinux.ru/omv_software/rpmtools
# (tpg) from Mageia
# http://svnweb.mageia.org/soft?view=revision&revision=6438
Patch0:		rpmtools-6.1-use-external-gzip.patch
# (tpg) http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft?view=revision&revision=271508
# fix it :)
Patch1:		rpmtools-6.1-really-use-xz-and-text-option-for-compression.patch
BuildRequires:	perl-devel
BuildRequires:	perl-MDV-Packdrakeng
BuildRequires:	perl-MDV-Distribconf
BuildArch:	noarch
Requires:	perl-MDV-Distribconf > 3.00
Requires:	xz
Requires:	gzip
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
%apply_patches

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%{_bindir}/dumpdistribconf
%{_bindir}/gendistrib
%{_bindir}/genhdlist-old
%{_mandir}/man1/dumpdistribconf*
%{_mandir}/man1/gendistrib*
%{_mandir}/man1/genhdlist-old.*

%files -n packdrake
%{_bindir}/packdrake
%{perl_vendorlib}/packdrake.pm
%{_mandir}/man1/packdrake*

%files -n genhdlist2
%{_bindir}/genhdlist2
%{_mandir}/man1/genhdlist2*


%changelog
* Tue May 31 2011 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 6.1-1mdv2011.0
+ Revision: 682063
- add disttag & distepoch to .xml.lzma metadata so that we can parse name,
  version, release & arch properly from filename

* Sun May 08 2011 Eugeni Dodonov <eugeni@mandriva.com> 6.0-4
+ Revision: 672593
- Use correct locale for genhdlist2 (patch from pterjan, #63229)

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 6.0-3
+ Revision: 669766
- add missing requires

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 6.0-2
+ Revision: 669449
- mass rebuild

* Wed Dec 15 2010 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 6.0-1mdv2011.0
+ Revision: 621872
- replace 'bzip2' dependency with 'xz'
- cleanup spec
- new release: 6.2
  	o compress xml files with '--text' flag passed to lzma (shrinks
  	  files.xml.lzma by 25%% \o/)
  	o add support for custom compression filter used for xml-info &
  	  synthesis.

  + Funda Wang <fwang@mandriva.org>
    - update URL

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 5.9-4mdv2011.0
+ Revision: 557004
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 5.9-3mdv2010.1
+ Revision: 523930
- rebuilt for 2010.1

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 5.9-2mdv2010.0
+ Revision: 453293
- perl-Compress-Zlib not needed any more

* Tue Jan 20 2009 Pixel <pixel@mandriva.com> 5.9-1mdv2009.1
+ Revision: 331814
- 5.9
- drop parsehdlist, rpm2header: unused, partially duplicated with perl-URPM
- drop rpm2cpio.pl (doesn't handle lzma payload which is the default)

* Tue Sep 30 2008 Pixel <pixel@mandriva.com> 5.8-1mdv2009.0
+ Revision: 290150
- 5.8:
- gendistrib:
  o don't call genhdlist2 with --no-md5sum for no good reason

* Tue Sep 23 2008 Pixel <pixel@mandriva.com> 5.7-1mdv2009.0
+ Revision: 287193
- genhdlist2:
  o with --versioned, create "versioned" metadata
  o add xml header to xml files generated
- gendistrib:
  o if "xml-info" is set in media.cfg, pass --xml-info to genhdlist2
- parsehdlist, rpm2header
  o fix support for rpm5
  o update deprecated code
- genhdlist-old
  o genhdlist is now renamed as genhdlist-old

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 5.6-2mdv2009.0
+ Revision: 225335
- rebuild

* Tue Mar 18 2008 Pixel <pixel@mandriva.com> 5.6-1mdv2008.1
+ Revision: 188468
- 5.6:
- gendistrib:
  o "askmedia" and "suppl" must not modify gendistrib behaviour (#39017)

* Wed Mar 05 2008 Pixel <pixel@mandriva.com> 5.5-2mdv2008.1
+ Revision: 180075
- fix upgrade: new pkg genhdlist2 must conflicts with previous rpmtools

* Wed Mar 05 2008 Pixel <pixel@mandriva.com> 5.5-1mdv2008.1
+ Revision: 179782
- move genhdlist2 to its own package
- 5.5:
- genhdlist2:
  o use utf8:: functions instead of Encode
    (to be able to work with only perl base modules)

* Tue Feb 26 2008 Pixel <pixel@mandriva.com> 5.4-1mdv2008.1
+ Revision: 175446
- 5.4:
- parsehdlist, rpm2header:
  o do not add/use FILENAME_TAG and FILESIZE_TAG to/in hdlist anymore

* Tue Feb 05 2008 Pixel <pixel@mandriva.com> 5.3.6-1mdv2008.1
+ Revision: 162588
- 5.3.6:
- genhdlist2:
  o fix writing utf8 in xml info files (#37482)

* Fri Jan 25 2008 Pixel <pixel@mandriva.com> 5.3.5-2mdv2008.1
+ Revision: 158001
- we can now expect librpm API to be backward compatible

* Tue Jan 15 2008 Pixel <pixel@mandriva.com> 5.3.5-1mdv2008.1
+ Revision: 152579
- 5.3.5:
- genhdlist2:
  o rename --xml-media-info into --xml-info
    (to be coherent with urpmi)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Pixel <pixel@mandriva.com> 5.3.4-1mdv2008.1
+ Revision: 132233
- 5.3.4:
- genhdlist2:
  o add --no-hdlist option (to be used by urpmi for --probe-rpms)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Pixel <pixel@mandriva.com> 5.3.3-1mdv2008.1
+ Revision: 121717
- require rpm used for build, including epoch
- 5.3.3:
- genhdlist2:
  o generate {info,changelog,files}.xml.lzma when they already exist,
    or when --xml-media-info is used
  o error message when parse_hdlist (partially) fail
  o handle old-rpms.lst (to be generated by youri)
    which will allow keeping rpms for some time without having in hdlist
    (useful for installs which expect the pkgs to be in sync in hdlist during
    the full install time)
    it will also allow keeping deprecated packages for some time

* Fri Jun 22 2007 Pixel <pixel@mandriva.com> 5.3.2-1mdv2008.0
+ Revision: 43048
- bug fix release
- gendistrib:
  o do generate global MD5SUM (in media/media_info)
- new release, 5.3.1
- genhdlist2:
  o add --allow-empty-media
  o fix MD5SUM generation
  o allow using this script with perl-URPM 1.47 (ie mdv2007.0)
- gendistrib:
  o call genhdlist2 instead of doing things here
  o media/media_info/hdlist_xxx_yyy.cz is now a symlink to media/xxx/yyy/media_info/hdlist.cz
  o synthesis.hdlist_xxx_yyy.cz and pubkey_xxx_yyy are also symlinks now
- parsehdlist:
  o display pkgsize with --all (Christiaan Welvaart)

* Fri Jun 15 2007 Pixel <pixel@mandriva.com> 5.2.1-1mdv2008.0
+ Revision: 40155
- new genhdlist2 (which will deprecate genhdlist)

* Mon Jun 11 2007 Olivier Thauvin <nanardon@mandriva.org> 5.2.0-1mdv2008.0
+ Revision: 37979
- 5.2.0 (kill old compat modules)

* Sun Jun 10 2007 Olivier Thauvin <nanardon@mandriva.org> 5.1.0-2mdv2008.0
+ Revision: 37965
- rebuild for rpm 4.4.8


* Tue Aug 22 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-22 13:48:39 (57497)
- 5.1.0

* Mon Aug 21 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-21 15:18:37 (57022)
- 5.0.29

* Mon Aug 21 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-21 14:33:43 (57000)
Import rpmtools

* Mon Mar 20 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.28-1mdk
- Add --norecursive option to genhdlist (M. Scherer)

* Wed Mar 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.27-2mdk
- Rebuild for rpm 4.4.5

* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.27-1mdk
- Replace serial by epoch everywhere in parsehdlist (rpm 4.4.4 compatibility)
- Fix BuildRequires
- Misc. code cleanup in gendistrib

* Fri Dec 30 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.26-2mdk
- Bump conflicts due to file moves
- Don't install empty manpages
- Update copyright notices

* Wed Nov 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.26-1mdk
- Use MDV:: perl modules, replaces the ones shipped by compatibility wrappers
- Move packdrake manpage to packdrake rpm
- gendistrib: Fix the location where the MD5SUM files are generated
  (thanks joeghi)

* Mon Oct 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.25-1mdk
- Documentation: new manpages for gendistrib, genhdlist, dumpdistribconf.
  More internal docs for Perl modules.
- gendistrib: new --version switch. Remove --distrib switch.
- Use Pod::Usage to implement --help in Perl tools
- Many code cleanups.
- dumpdistribconf wasn't working.
- genhdlist has new switches --md5sum, --list and --subdir. --headersdir has
  been removed since it uses File::Temp now.
- Remove build dependency on MDK::Common (Buchan Milne)

* Wed Sep 14 2005 Olivier Thauvin <nanardon@zarb.org> 5.0.24-1mdk
- 5.0.24 (gendistrib improvement && s/mandrake/mandriva/)

* Tue Aug 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.23-1mdk
- packdrake: fix bug in urpmq --headers (17245)

* Mon Aug 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.22-1mdk
- Minor code fixes and better error messages

* Mon Jun 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.21-1mdk
- Create tempfiles in $TMPDIR instead of $TMP
- Nits in error message reporting

* Tue May 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 5.0.20-2mdk
- Rebuild for rpm 4.4

* Mon Apr 04 2005 Pixel <pixel@mandrakesoft.com> 5.0.20-1mdk
- packdrake: remove dirty message when decompressing without Compress::Zlib

* Tue Mar 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.19-1mdk
- gendistrib: fix a bug in creation of media_info directories

* Mon Mar 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.18-1mdk
- gendistrib: build hdlists in a temporary file first, to reduce the window
  where the hdlists are corrupted

* Mon Mar 07 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.17-1mdk
- gendistrib: fix generation of per-media MD5SUM files. Plus doc nits.

* Tue Mar 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.16-1mdk
- packdrake: report size of toc (for rpmdrake's search progress bar)
- parsehdlist: add support to output SQL statements (Leon Brooks)

* Tue Feb 22 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.15-1mdk
- generate VERSION
- split Distribconf with Build
- gendistrib: --skipmissingdir
- gendistrib: perform little check

* Mon Feb 21 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.14-1mdk
- fix undefined handle in write_hdlists

* Mon Feb 21 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.13-1mdk
- Distribconf manage pubkey
- use lowercase name to generate filename (hdlist,synthesis,pubkey)
- rpmtools conflict packdrake < 5.0.10 (man page, thx Warly)

* Mon Feb 21 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.12-1mdk
- gendistrib skip media if suppl or askmedia is set

* Sun Feb 20 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.11-1mdk
- add Distribconf.pm and dumpdistribconf to manage distrib config
- gendistrib use Distribconf.pm

* Thu Feb 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.10-1mdk
- gendistrib:
  - Generate hdlists and synthesis as hard links in <name>/media_info
    subdirectories
  - Handle new hdlists format
  - Generate MD5SUM files

* Mon Jan 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.9-1mdk
- genhdlist now follows symlinks
- minor fixes in Packdrakeng

* Mon Jan 03 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.8-1mdk
- Fix the previous speedup
- BuildRequires perl-Compress-Zlib

* Thu Dec 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.7-1mdk
- speedup uncompress function

* Fri Dec 17 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.6-1mdk
- Ensure Packdrakeng::zlib loads properly, and is not used if Compress::Zlib
  is not available. Remove Compress::Zlib from BuildRequires
- packdrake: show a warning when an archive can't be found
- more docs

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.5-1mdk
- Fix the "quiet" option of packdrake (so urpmq and other tools don't produce
  warnings)

* Tue Dec 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.4-1mdk
- extract_archive() function in packdrake should do nothing if no file list
  is specified
- drop the requirement of packdrake on Compress::Zlib

* Mon Dec 13 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.3-1mdk
- don't use File::* modules (light for gi)
- conflict rpmtools <= 5.0.0 (split package)

* Mon Dec 13 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.2-1mdk
- add missing Packdrake/zlib.pm

* Mon Dec 13 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.1-1mdk
- split package

* Sun Dec 12 2004 Stefan van der Eijk <stefan@eijk.nu> 5.0.0-3mdk
- BuildRequires

* Thu Dec 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.0.0-2mdk
- Mostly doc fixes

* Mon Dec 06 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 5.0.0-1mdk
- 5.0.0
- Packdrakeng, new code

* Thu Sep 02 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-25mdk
- Make rpm tools handle new keywords in hdlists file.

* Wed Aug 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-24mdk
- Add rpm2cpio.pl

* Wed Aug 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-23mdk
- Don't include internal dependencies of the rpmlib in the parsehdlist output

* Thu Jul 22 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-22mdk
- Updates for the new media layout in cooker

* Mon Jul 05 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-21mdk
- Minor changes

* Fri Apr 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 4.5-20mdk
- add a --quiet option to packdrake
- rebuild for perl 5.8.4, and add a dependency on perl-base

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.5-19mdk
- rebuild for perl 5.8.3

* Fri Jan 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.5-18mdk
- Fix genhdlist without arg

* Fri Jan 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.5-17mdk
- add --dest option to genhdlist
- fix dir parsing (Thx Pascal Terjan)

* Fri Jan 09 2004 Warly <warly@mandrakesoft.com> 4.5-16mdk
- add provides perl(packdrake)

* Mon Jan 05 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 4.5-15mdk
- add some options to gendistrib/genhdlist

* Tue Dec 09 2003 François Pons <fpons@mandrakesoft.com> 4.5-14mdk
- added compability with RH 7.3.

* Thu Aug 28 2003 François Pons <fpons@mandrakesoft.com> 4.5-13mdk
- added support for %%{ARCH} in gendistrib.
- removing remaining MD5SUM files when running gendistrib.

