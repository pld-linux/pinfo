if [ ! -x /usr/bin/info ]; then
	alias info="pinfo"
fi

if [ ! -x /usr/bin/man ]; then
	alias man="pinfo -m"
fi
