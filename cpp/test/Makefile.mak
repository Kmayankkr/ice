# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

top_srcdir	= ..

!include $(top_srcdir)/config/Make.rules.mak

SUBDIRS		= IceUtil \
		  Slice \
		  Ice \
                  IceSSL \
		  Glacier2 \
		  Freeze \
		  IceStorm \
		  FreezeScript \
		  IceGrid

!if "$(BCPLUSPLUS)" != "yes" && "$(CPP_COMPILER)" != "VC60"
SUBDIRS		= $(SUBDIRS) \
		  IceBox
!endif

$(EVERYTHING)::
	@for %i in ( $(SUBDIRS) ) do \
	    @echo "making $@ in %i" && \
	    cmd /c "cd %i && $(MAKE) -nologo -f Makefile.mak $@" || exit 1
