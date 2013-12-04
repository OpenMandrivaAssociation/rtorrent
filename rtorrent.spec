%define	libtorrentver	0.13.3
%define	release	1

Name:		rtorrent
Version:	0.9.3
Release:	%{release}
Epoch:		1
Summary:	Curses based BitTorrent client
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://libtorrent.rakshasa.no/
Source0:	http://libtorrent.rakshasa.no/downloads/%name-%{version}.tar.gz

BuildRequires:	pkgconfig(libtorrent) >= %{libtorrentver}
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(xmlrpc)
BuildRequires:	pkgconfig(sigc++-2.0)

Requires:	libtorrent >= %{libtorrentver}

%description
This is a text mode BitTorrent client with a curses interface based on 
libtorrent.

%prep
%setup -q

%build
export CPPFLAGS=-I%{_includedir}/ncursesw
export LIBS="-lpthread -lxmlrpc -lxmlrpc_util"

%configure2_5x --with-xmlrpc-c
%make


%install 
%makeinstall_std


%files
%doc README AUTHORS doc/rtorrent.rc
%{_bindir}/rtorrent


