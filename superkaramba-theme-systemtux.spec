%define		theme	systemtux

Summary:	superkaramba - Systemtux theme
Summary(pl.UTF-8):   superkaramba - motyw Systemtux
Name:		superkaramba-theme-%{theme}
Version:	1.3
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dillenburg.dyndns.org/~jan/kde-look/systemtux_%{version}.tar.gz
# Source0-md5:	3738d2298616970bc681f8d7874ef4f3
Patch0:		%{theme}-theme.patch
URL:		http://www.kde-look.org/content/show.php?content=16265
Requires:	superkaramba
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systemtux theme for superkaramba. Features:
- Time / Date Output
- CPU Model / Clockspeed / Cache Detection
- CPU Usage Stats
- RAM / Swapfile Usage
- Network Traffic Monitor
- IP Address Output
- Hard Disk Drive Monitor
- XMMS Controls - Skip back, Play, Stop, Pause and Skip Forward
- Kernel Version Output
- Architecture Output

%description -l pl.UTF-8
Motyw systemtux do superkaramby. Wyświetlane informacje:
- Czas / Data
- Model procesora / Prędkość zegara
- Statystyki wykorzystania procesora
- Wykorzystanie pamięci RAM / pliku wymiany SWAP
- Monitor ruchu sieciowego
- Adres IP
- Monitor dysku twardego
- Przyciski XMMS - Poprzedni, Odtwarzaj, Stop, Pauza i Następny
- Wersja kernela
- Architektura komputera

%prep
%setup -q -c
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/systemtux/image

install systemtux_%{version}/*.theme $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/systemtux
install systemtux_%{version}/image/*.png $RPM_BUILD_ROOT%{_datadir}/themes/superkaramba/systemtux/image

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/superkaramba/systemtux
