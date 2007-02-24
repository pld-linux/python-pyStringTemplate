%define	pp_subname	PyStringTemplate
Summary:	Template engine for generating any formatted text output
Name:		python-%{pp_subname}
Version:	2.2
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://www.antlr.org/download/%{pp_subname}-%{version}.tar.gz
# Source0-md5:	c94060929bc03425181284a961968e5f
URL:		http://www.stringtemplate.org/
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
StringTemplate is a template engine for generating source code, web pages,
emails, or any other formatted text output. StringTemplate is particularly
good at multi-targeted code generators, multiple site skins, and
internationalization/localization. It evolved over years of effort
developing jGuru.com (Java version). StringTemplate also generates this
website and powers the ANTLR v3 code generator. Its distinguishing
characteristic is that it strictly enforces model-view separation unlike
other engines. There are currently about 600 StringTemplate source
downloads a month. 


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
