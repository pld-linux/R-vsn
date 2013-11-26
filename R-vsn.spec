%define		packname	vsn

Summary:	Variance stabilization and calibration for microarray data
Name:		R-%{packname}
Version:	3.30.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	81388e1ba615aeac7566847a3bc5fc23
URL:		http://bioconductor.org/packages/release/bioc/html/vsn.html
BuildRequires:	R
BuildRequires:	R-Biobase
BuildRequires:	R-limma
BuildRequires:	R-affy
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-Biobase
Requires:	R-limma
Requires:	R-affy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package implements a method for normalising microarray
intensities, both between colours within array, and between arrays.
The method uses a robust variant of the maximum-likelihood estimator
for the stochastic model of microarray data described in
the references (see vignette). The model incorporates data calibration
(a.k.a. normalization), a model for the dependence of the variance on
the mean intensity, and a variance stabilizing data transformation.
Differences between transformed intensities are analogous to
"normalized log-ratios". However, in contrast to the latter, their
variance is independent of the mean, and they are usually more
sensitive and specific in detecting differential transcription.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/vsn.so
