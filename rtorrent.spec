%define	libtorrentver	0.13.2
%define	release	%mkrel	1

Name:		rtorrent
Version:	0.9.2
Release:	%release
Epoch:		1
Summary:	Curses based BitTorrent client
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://libtorrent.rakshasa.no/
Source0:	http://libtorrent.rakshasa.no/downloads/%name-%{version}.tar.gz
Requires:	libtorrent >= %libtorrentver
BuildRequires:	libtorrent-devel >= %libtorrentver
BuildRequires:	libcurl-devel >= 7.12.0
BuildRequires:	ncursesw-devel
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	xmlrpc-c-devel
BuildRequires:  cppunit-devel

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%setup -q

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)

#gw add flags for the ncursesw headers
export CPPFLAGS=-I%_includedir/ncursesw

#add hack to fix build on BS, for some reason build fails with iurt on x86_64 without this,
#local build on BS works without this hack, though (wally 03/2010)
export LIBS="-lxmlrpc -lxmlrpc_util -lpthread"


%configure2_5x --with-xmlrpc-c
%make
cd doc
db2html faq.xml

%install 
rm -rf $RPM_BUILD_ROOT;
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc README AUTHORS doc/faq doc/rtorrent.rc
%{_bindir}/rtorrent
#gw it was outdated:
#%_mandir/man1/rtorrent.1*


%changelog
* Fri Jun 01 2012 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.9.2-1
+ Revision: 801720
- bump libtorrent dep
- update to new version 0.9.2

* Thu Apr 05 2012 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.9.1-1
+ Revision: 789338
- bump libtorrent dep
- update build deps
- update to new version 0.9.1

* Fri Dec 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.9.0-1
+ Revision: 748255
- new version
- bump libtorrent dep
- fix build
- update file list

* Fri Jun 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.9-1
+ Revision: 686872
- new version
- bump libtorrent dep

* Mon May 09 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.8-1
+ Revision: 673063
- new version
- bump libtorrent dep
- drop patch

* Thu Mar 03 2011 Jani VÃ¤limaa <wally@mandriva.org> 1:0.8.7-2
+ Revision: 641412
- add patch mentioned upstream bug ticket (#2511) to fix crash on startup
  after ncurses 5.8 update

* Mon Nov 01 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.7-1mdv2011.0
+ Revision: 591456
- new version
- bump libtorrent dep
- remove old man page

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1:0.8.6-3mdv2010.1
+ Revision: 533658
- use correct ldflags

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1:0.8.6-2mdv2010.1
+ Revision: 533655
- rebuild for openssl 1.0

  + Sandro Cazzaniga <kharec@mandriva.org>
    - clean spec, not bump release

* Mon Dec 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.6-1mdv2010.1
+ Revision: 474399
- new version
- bump libtorrent dep
- drop patch

* Tue Jun 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.5-1mdv2010.0
+ Revision: 388791
- new version
- fix format string
- bump libtorrent dep

* Fri Nov 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.4-1mdv2009.1
+ Revision: 305445
- new version
- bump deps

* Thu Sep 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.3-1mdv2009.0
+ Revision: 285631
- new version
- bump dep
- drop all patches

* Sun Sep 07 2008 GaÃ«tan Lehmann <glehmann@mandriva.org> 1:0.8.2-4mdv2009.0
+ Revision: 282118
- enable scgi support

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:0.8.2-3mdv2009.0
+ Revision: 269225
- rebuild early 2009.0 package (before pixel changes)

* Fri Aug 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.2-2mdv2009.0
+ Revision: 268228
- sync patches with Gentoo
- update license

* Fri May 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.2-1mdv2009.0
+ Revision: 204987
- new version
- bump libtorrent dep

* Wed Apr 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.1-1mdv2009.0
+ Revision: 196740
- new version

* Tue Jan 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.8.0-1mdv2008.1
+ Revision: 159988
- new version
- bump deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Funda Wang <fwang@mandriva.org> 1:0.7.9-1mdv2008.1
+ Revision: 102268
- removed unapplied
- New version 0.7.9

* Tue Oct 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.8-1mdv2008.1
+ Revision: 96273
- new version
- bump deps

* Mon Aug 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.7-1mdv2008.0
+ Revision: 67303
- new version
- bump deps
- patch for rearranged sigc++2.0 headers

* Thu Aug 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.6-1mdv2008.0
+ Revision: 58092
- new version
- bump deps

* Tue Jul 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.5-1mdv2008.0
+ Revision: 47398
- new version
- bump deps


* Thu Mar 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.4-1mdv2007.1
+ Revision: 149306
- new version
- bump deps
- remove build fix

* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.2-1mdv2007.1
+ Revision: 114600
- new version
- bump deps

* Sun Dec 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.1-1mdv2007.1
+ Revision: 102963
- new version
- bump deps

* Sat Dec 16 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.0-3mdv2007.1
+ Revision: 98173
- fix build
- switch to libncursesw

* Thu Dec 14 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.7.0-2mdv2007.1
+ Revision: 96734
- bot rebuild
- new version
- bump deps

* Wed Nov 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.6.4-2mdv2007.0
+ Revision: 78122
- fix optimization flags

* Sun Oct 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.6.4-1mdv2007.1
+ Revision: 73633
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.6.3-2mdv2006.0
+ Revision: 63780
- rebuild
- Import rtorrent

* Thu Oct 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.6.3-1mdv2007.1
- New version 0.6.3

* Fri Sep 29 2006 Götz Waschk <waschk@mandriva.org> 1:0.6.2-1mdv2007.0
- New version 0.6.2

* Tue Aug 22 2006 Götz Waschk <waschk@mandriva.org> 1:0.6.1-1mdv2007.0
- bump deps
- New release 0.6.1

* Tue Jul 18 2006 Götz Waschk <waschk@mandriva.org> 1:0.6.0-1mdv2007.0
- fix build
- bump deps
- New release 0.6.0

* Thu May 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.5.3-1mdk
- New release 0.5.3

* Mon May 22 2006 Götz Waschk <waschk@mandriva.org> 1:0.5.2-1mdk
- drop patch
- New release 0.5.2

* Mon May 08 2006 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdk
- patch to fix the build
- bump deps
- New release 0.5.1

* Mon Apr 10 2006 Götz Waschk <waschk@mandriva.org> 1:0.5.0-1mdk
- bump deps
- New release 0.5.0

* Mon Feb 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.5-1mdk
- New release 0.4.5

* Mon Jan 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:0.4.3-1mdk
- New release 0.4.3

* Thu Jan 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.2-1mdk
- New release 0.4.2

* Wed Dec 21 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.1-1mdk
- New release 0.4.1

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 1:0.4.0-1mdk
- bump deps
- New release 0.4.0

* Thu Oct 20 2005 Götz Waschk <waschk@mandriva.org> 01:.3.6-1mdk
- bump deps
- New release 0.3.6

* Sat Oct 01 2005 Götz Waschk <waschk@mandriva.org> 1:0.3.5-1mdk
- bump deps
- New release 0.3.5

* Mon Sep 19 2005 Götz Waschk <waschk@mandriva.org>  1:0.3.4-1mdk
- bump deps
- New release 0.3.4

* Tue Sep 06 2005 Götz Waschk <waschk@mandriva.org> 1:0.3.3-1mdk
- bump deps
- New release 0.3.3

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdk
- bump deps
- New release 0.3.2

* Thu Jul 21 2005 Götz Waschk <waschk@mandriva.org> 1:0.3.0-1mdk
- mkrel
- bump deps
- New release 0.3.0

* Thu Jul 14 2005 Götz Waschk <waschk@mandriva.org> 1:0.2.7-2mdk
- fix buildrequires

* Thu Jul 14 2005 Götz Waschk <waschk@mandriva.org> 1:0.2.7-1mdk
- add more docs
- bump deps
- New release 0.2.7

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 0.2.6-1mdk
- update file list
- bump deps
- New release 0.2.6

* Tue Jun 21 2005 Götz Waschk <waschk@mandriva.org> 1:0.2.5-1mdk
- bump deps
- New release 0.2.5

* Thu Jun 09 2005 Götz Waschk <waschk@mandriva.org> 0.2.4-1mdk
- bump deps
- New release 0.2.4

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 1:0.2.3-1mdk
- bump deps
- New release 0.2.3

* Sat May 07 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdk
- bump deps
- New release 0.2.2

* Sat Apr 30 2005 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdk
- bump deps
- New release 0.2.1

* Sun Apr 24 2005 Götz Waschk <waschk@mandriva.org> 0.2.0-2mdk
- force dep on the right library version

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdk
- requires new libtorrent
- New release 0.2.0

* Sat Apr 16 2005 Götz Waschk <waschk@linux-mandrake.com> 0.1.5-1mdk
- bump deps
- New release 0.1.5

* Wed Mar 30 2005 Götz Waschk <waschk@linux-mandrake.com> 0.1.4-1mdk
- requires new libtorrent
- New release 0.1.4

* Wed Mar 09 2005 Götz Waschk <waschk@linux-mandrake.com> 1:0.1.2-1mdk
- split from the libtorrent package

* Wed Mar 09 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.5.1-1mdk
- New release 0.5.1

* Sun Feb 27 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.0-1mdk
- New release 0.5.0

* Sun Feb 20 2005 Götz Waschk <waschk@linux-mandrake.com> 0.4.11-1mdk
- initial mdk package

* Sat Dec 18 2004 - darix@irssi.org
- initial package

