%define	fontname	jomolhari

Name:		%{fontname}-fonts
Version:	0.003
Release:	8.1%{?dist}
Summary:	Jomolhari a Bhutanese style font for Tibetan and Dzongkha

Group:		User Interface/X
License:	OFL
URL:		http://chris.fynn.googlepages.com/jomolhari
Source0:	http://chris.fynn.googlepages.com/jomolhari-alpha003c.zip
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Jomolhari is an TrueType OpenType Bhutanese style font for Dzongkha and
Tibetan text. It is based on Bhutanese manuscript examples, supports the
Unicode and the Chinese encoding for Tibetan.
The font supports the standard combinations used in most texts.

%prep
%setup -q -c

%build
# Empty build section

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

for i in FONTLOG.txt OFL-FAQ.txt OFL.txt
do
	tr -d '\r' < $i > ${i}.tmp
	mv -f ${i}.tmp $i
done

%clean
rm -fr %{buildroot}

%_font_pkg *.ttf
%doc FONTLOG.txt OFL-FAQ.txt OFL.txt
%dir %{_fontdir}

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.003-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 0.003-7
- Update to new fonts guidelines, thanks to Rajeesh K Nambiar (#477403)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 29 2008 Marcin Garski <mgarski[AT]post.pl> 0.003-5
- Update URL

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-4
- Fix license tag

* Fri Apr 06 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-3
- Update to 0.003c
- Change license from GPL to OFL

* Fri Mar 23 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-2
- Extend description section

* Mon Mar 12 2007 Marcin Garski <mgarski[AT]post.pl> 0.003-1
- Initial specfile
