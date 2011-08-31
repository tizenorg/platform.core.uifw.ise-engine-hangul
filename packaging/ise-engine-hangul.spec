Name:       ise-engine-hangul
Summary:    Hangul Input Method Engine for ISF
Version:    1.3.2
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO_BE/FILLED_IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(isf)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libhangul)

%description
Hangul Input Method Engine enables isf to input Hangul (Korean)
characters from the keyboard using the plugin modules and the data files.


%prep
%setup -q

%build

./bootstrap
%configure --prefix=%{_prefix} --disable-static

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_datadir}/scim/icons/scim-hangul.png
%{_datadir}/scim/hangul/symbol.txt
%{_datadir}/locale/*/LC_MESSAGES/*
%{_libdir}/scim-1.0/1.4.0/IMEngine/hangul.so

