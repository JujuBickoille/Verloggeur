## Process this file with automake to produce Makefile.in
## Created by Anjuta

SUBDIRS = src 

verloggeurdocdir = ${prefix}/doc/verloggeur
verloggeurdoc_DATA = \
	README\
	COPYING\
	AUTHORS\
	ChangeLog\
	INSTALL\
	NEWS


EXTRA_DIST = $(verloggeurdoc_DATA)


# Remove doc directory on uninstall
uninstall-local:
	-rm -r $(verloggeurdocdir)
