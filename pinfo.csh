if ( ! -x /usr/bin/info ) then
	alias info "pinfo"
endif

if ( ! -x /usr/bin/man ) then
	alias man "pinfo -m"
endif
