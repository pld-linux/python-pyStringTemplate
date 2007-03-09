%define	pp_subname	PyStringTemplate
Summary:	Template engine for generating any formatted text output
Summary(pl.UTF-8):	Silnik szablonów do generowania dowolnie sformatowanego wyjścia tekstowego
Name:		python-%{pp_subname}
Version:	2.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://www.antlr.org/download/%{pp_subname}-%{version}.tar.gz
# Source0-md5:	c94060929bc03425181284a961968e5f
URL:		http://www.stringtemplate.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-antlr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StringTemplate is a template engine for generating source code, web
pages, emails, or any other formatted text output. StringTemplate is
particularly good at multi-targeted code generators, multiple site
skins, and internationalization/localization. It evolved over years of
effort developing jGuru.com (Java version). StringTemplate also
generates its own website and powers the ANTLR v3 code generator. Its
distinguishing characteristic is that it strictly enforces model-view
separation unlike other engines.

%description -l pl.UTF-8
StringTemplate to silnik szablonów do generowania kodu źródłowego,
stron WWW, e-maili i dowolnego innego sformatowanego wyjścia
tekstowego. StringTemplate jest dobry szczególnie do generatorów
kodu o wielu przeznaczeniach, wielu skórkach stron oraz
internacjonalizacji/lokalizacji. Wyewoluował przez lata starań przy
tworzeniu jGuru.com (w wersji w Javie). StringTemplate generuje także
własną stronę i zasila generator kodu ANTLR v3. Jego cechą
charakterystyczną jest to, że w przeciwieństwie do innych silników
ściśle narzuca rozdzielenie model-widok.

%prep
%setup -q -n %{pp_subname}-%{version}

%build
cd src
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

cd src
python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{py_sitescriptdir}/stringtemplate
%{py_sitescriptdir}/*egg-info